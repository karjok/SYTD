B
    ª½\&;  ã            
   @   sl  d Z dZdZdZdZdZdZdZdZd	d
l	Z	d	d
l
Z
d	d
lZd	d
lZd	d
lZd	d
lZyd	d
lZW n, ek
r   ejdgdejejd Y nX y>e d¡ eed  ej d¡Zeed  eed  W n ejjk
rö   ee d  e  Y n` ek
r    ee d e  e  Y n6 ek
rT Z zee e  e  W d
d
Z[X Y nX dd Z dd Z!y2ej"de dZ#e# $¡  xe# %¡ re!  qW W n` ek
rÄ   ee d e  e  Y n6 ek
rø Z zee e  e  W d
d
Z[X Y nX dd Z&dd Z'dd  Z(d!d" Z)d#d$ Z*d%d& Z+d'd( Z,d)d* Z-d+d, Z.d-d. Z/d/d0 Ze0d1krhe+  e,  d
S )2z[91mz[92mz[97mz[90mz[0mz[93mz[3mz[23mz[30mé    Nzcd && pip install pytubeT)ÚshellÚstdoutÚstderrÚclearz
# Checking the connection..zhttps://m.facebook.comu   # Connection OK âz¹# Preparing the required module..
  If you use it in first time,
  It may takes few minutes depends your connection speed.
  Cancelling this process maybe give you
  an error in future.znConnection error detected !
SYTD program need an internet connection.
Please check it before use this program.z	
Canceledc           	   C   sn   y>ydd l } W n, tk
r:   tjdgdtjtjd Y nX W n* tk
rh   ttd t	  t
  Y nX d S )Nr   zcd && pip install pytubeT)r   r   r   z	
Canceled)ÚpytubeÚImportErrorÚ
subprocessÚcallÚDEVNULLÚSTDOUTÚKeyboardInterruptÚprintÚlrÚxÚexit)r   © r   úyt.pyÚupdt.   s    "r   c           
   C   s¶   t d td t  d td t d t  d td t d t d t d t d t d t d t d t d t d td g	} x6| D ].}ttd	 | d
df tj ¡  t 	d¡ qW d S )Nu   â¢     u   â¢ u   â¢   u   â¢u    â¢ u     â¢ u       â¢ u    â¢   z# Processing Ú )ÚendgÉ?)
ÚwÚgrÚirr   ÚlgÚsysr   ÚflushÚtimeÚsleep)ÚsÚanr   r   r   Úanim1>   s
    z
 
 r    Zupdating)ÚnameÚtargetc               C   sF   yt jdtd W n. tk
r@   ttd  t  t ¡  Y nX d S )NÚResults)ÚfilenamezKPermission error.
Please restart and give SYTD permission to access storage)ÚstÚdownloadÚnamafileÚPermissionErrorr   r   r   r   r   r   r   r   ÚprossvU   s    r)   c              C   sò   yVt jdtd dt d t d t d } tj| dtjtjd t d	t d
 ¡ W n t	k
rì } zxt
td t d t  y0ttd t }|dkr¢t  nt  t  W n* tk
rÚ   t
td t  t  Y nX W d d }~X Y nX d S )Nr#   )r$   zffmpeg -i Results/z.mp4 -f mp3 z.mp3 && mv z.mp3 ResultsT)r   r   r   zcd Results && rm z.mp4z0Package ffmpeg not installed.
Please install it z$pkg install ffmpegz   Want to try gain ? (y/n): Úyz	
Canceled)r%   r&   r'   r   r	   r
   r   ÚosÚsystemÚ	Exceptionr   r   Úylr   Úinputr   ÚmainÚbannÚmenur   r   )ZffÚeÚtar   r   r   Úprossm^   s     
r5   c              C   s^   dddg} xN| D ]F}t td t d t d t d | dd	f tj ¡  t d
¡ qW d S )Nz .   z ..  z ... z[õ   Ãú]ZDownloadingr   )r   gÙ?)	r   r   r   r   r   r   r   r   r   )Úkr   r   r   r   Úanims   s
    

. 
 r9   c              C   s0  d} d}d}d}yòt jdtd}| ¡  x| ¡ r:t  q*W td|  d | d	 |  d
 | d  t| d | d	 |  d
 | td  d | d t td   y0t	| d | }|dkrÆt
  nt  t  W n* tk
rþ   t| d |  t  Y nX W n( tk
r*   t| d  t  Y nX d S )Nz[91mz[92mz[97mz[0mZsantay)r!   r"   Ú
ú[r6   r7   zDownload completed !!r   z file saved in:z	 Results/é   z   Want to try gain ? (y/n): r*   z	
CanceledzHStorage error.
please restart and give SYTD permission to access storage)Ú	threadingÚThreadÚtrgÚstartÚisAliver9   r   Úfrmtr'   r/   r0   r1   r2   r   r   r(   )r   r   r   r   Ztrr4   r   r   r   Útrdx   s.    

(@
rC   c              C   s  ydd l } W n, tk
r8   tjdgdtjtjd Y nX dag ayltt	d t
 d t	 d t d	 t
 }x@|dkr®tt	d
  tt	d t
 d t	 d t d	 t
 }qpW tt	d t
 d t	 d t d t
  dd¡att	d t
 d t	 d t d t
 d t d t
 d t d t
 }xN|dkrv|dkrvtt	d  tt	d t
 d t	 d t d t
 }q*W |dkrddgatanddgatatdkr¬dan yt d¡ W n   Y nX tt	d t
 d t	 d t d  y|  |¡}|j ¡ aW n¢ | jjk
r¦   tt	d t
 d t	 d t	 d t  y2tt	d t
 }|dkrft  nt  t  W n, tk
r    tt	d t  t  Y nX Y nX t  W nÌ tk
rÜ   tt	d t  t  Y n¢ t k
r| } ztt	d t
 d t	 d | y2tt	d t
 }|dkr0t  nt  t  W n, tk
rj   tt	d t  t  Y nX W d d }~X Y nX d S ) Nr   zcd && pip install pytubeT)r   r   r   r   r;   r6   r7   zYoutube video url: z   Url don't be blankzOutput file name: ú Ú_zOutput file type Úvz(video) or Úmz	(music): zJust v(video) or m(mp3) onlyz'Output file type v(video) or m(music): ZVideoz.mp4ZMusicz.mp3Z	SYTD_FILEr#   z,Connecting to the Youtube.com, please wait..z'Download failed. Please check your url.z   Want to try gain ? (y/n): r*   z	
Canceled)!r   r   r   r	   r
   r   r?   rB   r/   r   r   r   r   Úreplacer'   r)   r5   r+   ÚmkdirZYouTubeZstreamsÚfirstr%   Ú
exceptionsZRegexMatchErrorr   r0   r1   r2   r   r   rC   r-   )r   ZlinkZvmr*   r4   r3   r   r   r   r0      st    (
,0H.

$

(





r0   c              C   sf   t d } t d¡ x$| D ]}t|ddf t d¡ qW tt d  ttd d¡  tt d  d S )	Nuè  
  â ââââââââ â ¬âââââ â â¢ââââ ââââââââââââââ  ââââââ
 â¡âââââââââ âââââââ  â£ââââ  âââââââââââ    âââââââââââ
â¢ââââââââââ ââââââ â â£¼âââââ¡§ âââââââââââ    âââââââââââ
âââââââ£¯â£ââââ¡ â¢ºââââââ£ââââââ£¸â â    âââââ  â â    âââââââââââââ 
ââââââ¢¼ â â â   â â ââââââ¡ââââââ â â    âââââ     â  âââââ  â¢©âââââ
âââââââ  â  â    â¡¿ââââââââââ¡      âââââ      â âââââ â â âââââ
âââââââââ£â     â âââââââââ¡ â    â  ââââ       âââââ   âââââ
â ââââââââââ â â  âââââââââ¢¦â      â ââââ       ââââââ  â âââââ
â  âââââââââââ¢ª   âââââââ£â     â   ââââ       ââââââ â â â ââââ
â â â â¢¼â¡§ââââââââ â â âââââââ °  â      ââââ      â âââââ   âââââ
â â  â    âââââââ  â â¡ âââââ ½ â â  â   â â âââââ       âââââ â  âââââ
â â   â  â â âââââ   â ââââ     â â â â â âââââ      â ââââââ  â âââââ
â âââ£â â  â âââââ  â  âââââ â â   â â â  â ââââ       âââââ  ââââââ
â£ââââââââââââ  â  âââââ     â â    âââââ     â  ââââââââââââ
âââââââââââââ  â  âââââ     â  â â â ââââ     â â ââââââââââââ£²
â ââââââââââââ     âââââ    â     â ââââ       âââââââââ
 â â£âââââââ£â£â   â â â â£ââââ      â  â â â¡¿âââ â      â ¹âââââââ¡â 
r   r   )r   ga2U0*©3?z7=======================================================z1S I M P L E   Y O U T U B E   D O W N L O A D E Ré7   )r   r+   r,   r   r   r   r   Úcenter)r   Úir   r   r   r1   è   s    

 r1   c              C   s  t td t d t d t d  t td t d t d t d  t td t d t d t d	  t td t d
 t d t d t d t d t d  t td t d t d t d  yttd t d t d t } xx| dkrh| dkrh| dkrh| d
krh| dkrh| dkrht td |  d t  ttd t d t d t } qòW | dkrt td  t  nZ| dkrt  nH| dkr¬t	  n6| d
kr¾t
  n$| dkrÐt  nt td  t  W n, tk
r   t td t  t  Y nX d S )Nz
[Ú1r7   z Startr;   Ú2z AboutÚ3z Quick TutorialÚ4z Update ú(Únewú)Ú0z Exit
ZSYTDú/z> r   zOption z is not in the menu list.z7=======================================================z
Blank input detected !z	
Canceled)r   r   r   r   r.   r/   r   r0   ÚaboutÚtutorialÚupdater   r   )Úopsr   r   r   r2     s4    $$$<$ >$





r2   c               C   sà   t td  t td t d t d t d t d t d t d t d	 t d
 t d t d t d t d t d t d t d t d t d t d t d t d  t td  ttd  t  t	  d S )Nz7=======================================================z
Name         :z Simple Youtube Downloader
zVersion      :z 2.5 rS   z>last updated on
               December 19th, 2018; 2:09PM WIBz)
zDate         :z" December 12th, 2018; 12:17PM WIB
zAuthor       :z  Karjok Pangesty
               zhttps://t.me/om_karjokzTeam         :z. Cracker Noob Squads Indonesia
               zhttps://t.me/CRABS_IDzThanks to    :z Allah SWT, my Agustinna Pangesty,
               all member of CRABS, and all who have
               supported and bullying me.
      zPres enter to back to menu)
r   r   r   r   r   ÚitÚixr/   r1   r2   r   r   r   r   rX   "  s    	¢rX   c               C   s\   t td  t td t d t d t d  t td  ttd t  t  t  d S )Nz7=======================================================z
What Is This ?
--------------zw
SYTD (Simple Youtube Downloader) is a simple tool
for download youtube video and convert it 
into video or music file.z!

How To Use It ?
---------------a¾  
Copy the link of video wich you want to download.
If you use Youtube App,
open the video, then tap on share button,
and select copy to the clipboard.

Open SYTD program, and then select number 1
and press enter.
Paste link on the form, and press enter.

Chose your output file format.
'v' for video and 'm' for music.

Wait for few minutes
until downloading process is done.

If downloading is successfullly,
the file save in /sdcard directory.
zPress enter to back to menu)r   r   r   r   r/   r1   r2   r   r   r   r   rY   7  s    rY   c              C   sÔ   t td  t td  yztj d¡} t td  t td  t td t  t 	d¡ t
jdgd	t
jt
jd
 t td  t d¡ t 	d¡ W n< tjjk
rÎ   t td  ttd  t  t  Y nX d S )Nz7=======================================================z
Checking the connection..zhttps://m.facebook.comu   Connection OK âzUpdating the program..z<This may take a few minutes, don't be cancel !
Please wait..zcd && rm -rf SYTDz.cd && git clone https://github.com/karjok/SYTDT)r   r   r   zRestarting the program..g      à?zcd ../SYTD && python sytd.pyznConnection error detected !
SYTD program need an internet connection.
Please check it before use this program.zPress enter to back to menu)r   r   r.   ÚurllibÚrequestÚurlopenr   r   r+   r,   r   r	   r
   r   r   r   ÚerrorÚURLErrorr/   r1   r2   )Úrqr   r   r   rZ   J  s"    

rZ   c               C   s4   t td t t d t t d t  t ¡  d S )NzRIf you have any problem or questions with this tool,
Please contact the Author at zhttps://t.me/om_karjok
zExit !
)r   r   r\   r   r]   r   r   r   r   r   r   r   r   ^  s    (r   Ú__main__)1r   r   r   r   r   r.   r\   r]   r   r   r   r=   r+   r   Zurllib.requestr^   r   r   r	   r
   r   r,   r   r_   r`   rc   ra   rb   r   r   r-   r3   r   r    r>   Ztredr@   rA   r)   r5   r9   rC   r0   r1   r2   rX   rY   rZ   Ú__name__r   r   r   r   Ú<module>	   sn   0


	
	V	
