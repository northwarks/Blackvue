# Blackvue Movie Downloader
Blackvue Camera Movie Downloader
So, like many I had a want/need to to download in-car footage from the Blackvue 750 without using the Blackvue Cloud. I wanted something that would download the movies overnight to my Synology NAS direct over my Wi-Fi. Blackvue don't make this easy but its possible to do. Ideally I'd have used something like RSync to keep a local and remote folder up to date but thats not possible as far as I can tell.

This was inspired by the post here:https://www.bjornsblog.nl/tips-and-tricks/download-all-files-from-blackvue-dashcam-to-your-synology-wifi/

The code is in Python, it works, its not fancy by any stretch of the imagination and I'm no developer! So use this at your own risk and tweak to your needs !

Note:
The Blackvue 750 in sport mode setting saves 1 minute files, for me these are ~90mb each, I've found the Wi=Fi is slow at best, when I first started this I had over 600 files saved on the camera, it's best to format a start again so you are playing with a few files to start with.

What it does:
1 - Checks to see if the Camera is connested - I've allocated a fixed IP 'cus I can via my DHCP setup.
2 - Gets a list of files off the device
3 - Compares that to what it has allready locally and if some files are missing it creates a download list
4 - It goes ahead and downloads the files ---- slowly :)
5 - It updates AN EXISTING log file with progress and updates

Unless you have endless diskspace you will need some form of control of the movies it downloads as they can build up very quickly, 2 or 3 days of commuting for me is over 600 x 90mb movies.

========= xxx ==========
