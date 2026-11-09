$pdf_mode = 5;
$xelatex = 'xelatex -interaction=nonstopmode -file-line-error %O %S';

# Regenerate both presentations from the same authoritative register.
# Fail the build rather than compile stale constraints.
system("python3", "scripts/render_mcr_editions.py") == 0
  or die "Could not synchronize MCR editions\n";
