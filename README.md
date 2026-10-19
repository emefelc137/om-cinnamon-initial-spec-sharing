# om-cinnamon-initial-spec-sharing
Sharing spec files so that things may be built locally, and tested by those on Cooker.

Build and Install Order:

xapps  
python-xapp  
cinnamon-desktop  
muffin  
cjs  
cinnamon-settings-daemon  
cinnamon-session                                  
cinnamon-translations                  
cinnamon-menus                
cinnamon-control-center                  
cinnamon-screensaver                  
nemo                             
cinnamon                         
xapp-symbolic-icons                                    
mint-x-icons                                        
mint-y-icons                                       
mint-themes                                        
xed                            
xreader  
pix                      
xviewer  

Build Notes
===========  

Spec files have been shared here for ease at this stage, but each one truly lives in its own repo under this account according to package name ie. xapps.spec lives in emefelc137/xapps.  Likewise, where other files such as patches are required by the spec files, they can be found in those repos.                 

Testing/Other Notes    
===================

Out of scope: Wayland session (still experimental), Cinnamon sounds (not downloadable from github, and other reasons), Bluetooth-related packages (just for right now), Display manager-related packages (I'm assuming people are going to test side-by-side with what they have ie. KDE/GNOME, which has been tested as working without issues.)

Known issues: Resizing of Brave browser windows is improper and right-click menus sometimes don't appear visually (Brave provided rpm and official Flatpak have the issues), but natively packaged browsers to OM ie. Firefox and Helium work perfectly so this is more of an informative since I know many people use Brave within the userbase.

Directional: Everything for the desktop is provided as it is now with the ethos of the desktop in mind, while also looking toward the future.  All pre-existing packages are at the latest stable versions, some new have been added (with many more on the way), and the apps provided are following the path being carved by the xapp-project.  Additional apps, tools, configurations, and administrative tightening up of packaging are planned as well install tasks, and a spin iso.


Thank You, and Have Fun!
