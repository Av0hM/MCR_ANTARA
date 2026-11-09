import numpy as np
import pandas as pd
import pytest
from scripts.validate_simulation_evidence import intervals,boolean,weighted,completion,soc,vector,temperature_c,censored_completion,compare_configuration,read_csv

def frame():return pd.DataFrame(dict(time_sec=[0.,2.,7.],interval_duration_sec=[2.,5.,0.],state_time_sec=[2.,7.,7.],terminal_snapshot=[False,False,True]))
def test_weights():assert weighted([10,20,999],intervals(frame()))==pytest.approx(120/7)
def test_terminal_no_time():assert intervals(frame()).sum()==7
@pytest.mark.parametrize('field,value',[('time_sec',0.),('state_time_sec',8.),('interval_duration_sec',-1.)])
def test_bad_time(field,value):
    f=frame();f.loc[1,field]=value
    with pytest.raises(ValueError):intervals(f)
def test_gap():
    f=frame();f.loc[1,'time_sec']=3
    with pytest.raises(ValueError):intervals(f)
def test_false_string():assert not boolean(['False'])[0]
def test_invalid_bool():
    with pytest.raises(ValueError):boolean(['maybe'])
def test_terminal_invalid():
    f=frame();f.loc[0,'terminal_snapshot']=True
    with pytest.raises(ValueError):intervals(f)
def test_short_preset():assert 'NOT EXPECTED' in completion(0,3600,True,86400)
def test_no_terminal():assert 'INCOMPLETE' in completion(0,31536000,False,31536000)
def test_complete():assert completion(0,86400,True,86400)=='COMPLETE EXPECTED HORIZON'
def test_missing_start():assert 'missing beginning' in completion(2,86400,True,86400)
def test_soc():assert soc(15,25)==60
def test_bad_soc_capacity():
    with pytest.raises(ValueError):soc(15,0)
def test_temperature():np.testing.assert_allclose(temperature_c([273.15,293.15],[0,20]),[0,20])
def test_bad_temperature():
    with pytest.raises(ValueError):temperature_c([273.15],[273.15])
def test_censoring():assert censored_completion([1,0],[10,np.inf])=={'n':2,'successes':1,'nonconverged':1,'successful_median_s':10.}
def test_failed_only():assert censored_completion([0],[np.inf])['successful_median_s'] is None
def test_false_success():
    with pytest.raises(ValueError):censored_completion([1],[np.inf])
def test_vector_formats():np.testing.assert_array_equal(vector('[1, 2]'),vector('[1 2\n]'))
def test_invalid_vector():
    with pytest.raises(ValueError):vector('[1 ... 2]')
def test_histogram_exposure_conservation():assert vector('[2 3]').sum()*4==20
def test_config_unknown():assert compare_configuration({'epoch':'UNKNOWN'},{'epoch':2029},['epoch'])=='INSUFFICIENT EVIDENCE'
def test_config_difference():assert compare_configuration({'epoch':2000},{'epoch':2029},['epoch'])=='INCOMPATIBLE CONFIGURATION'
def test_config_equal():assert compare_configuration({'epoch':2029},{'epoch':2029},['epoch'])=='DIRECTLY COMPARABLE'
def test_empty_event(tmp_path):
    p=tmp_path/'empty.csv';p.write_text('\n');assert read_csv(p).empty
def test_duplicate_headers(tmp_path):
    p=tmp_path/'bad.csv';p.write_text('t,t\n1,1\n')
    with pytest.raises(ValueError):read_csv(p)
def test_gross_not_actual():
    capacity_mbit=.0192*348
    recorded_source_mb=.00518798828125
    assert capacity_mbit>recorded_source_mb*8
