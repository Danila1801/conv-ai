# Export Group7-v3.pptx to PDF with PowerPoint itself (fonts embedded exactly as PowerPoint draws them)
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$pp = New-Object -ComObject PowerPoint.Application
$deck = $pp.Presentations.Open((Join-Path $here 'Group7-v3.pptx'), $true, $false, $false)
$deck.SaveAs((Join-Path $here 'Group7-v3.pdf'), 32)  # 32 = ppSaveAsPDF
$deck.Close()
$pp.Quit()
Write-Output 'exported Group7-v3.pdf'
