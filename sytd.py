B
    s\ <  ã            
   @   s®  d Z dZdZdZdZdZdZdZdZd	d
l	Z	d	d
l
Z
d	d
lZd	d
lZd	d
lZd	d
lZejdgdejejd d	d
lZy>e d¡ eed  ej d¡Zeed  eed  W n ejjk
rÜ   ee d  e  Y n` ek
r   ee d e  e  Y n6 ek
r: Z zee e  e  W d
d
Z[X Y nX dd Zdd Z dd Z!dd Z"dd Z#dd  Z$d!d" Z%d#d$ Z&d%d& Z'd'd( Z(d)d* Ze)d+krªe$  e%  d
S ),z[91mz[92mz[97mz[90mz[0mz[93mz[3mz[23mz[30mé    Nzcd && pip install pytubeT)ÚshellÚstdoutÚstderrÚclearz
# Checking the connection..zhttps://m.facebook.comu   # Connection OK âz!# Preparing the required module..znConnection error detected !
SYTD program need an internet connection.
Please check it before use this program.z	
Canceledc               C   sV   y"t j tt ¡jdtd d W n. tk
rP   tt	d  t
  t 
¡  Y nX d S )NÚResultsZ_video)ÚfilenamezKPermission error.
Please restart and give SYTD permission to access storage)ÚyÚstreamsÚget_by_itagÚitgÚpiÚdownloadÚnamafileÚPermissionErrorÚprintÚlrÚexitÚsys© r   r   úyt.pyÚprossvC   s    "r   c              C   sÐ   y<t j tt ¡jdtd d t dt d t d ¡ W n t	k
rÊ }  zpt
t|  t  y0ttd t }|dkrt  nt  t  W n* tk
r¸   t
td	 t  t  Y nX W d d } ~ X Y nX d S )
Nr   Z_music)r   zcd Results && mv z_music.mp4 z
_music.mp3z   Want to try gain ? (y/n): r   z	
Canceled)r   r	   r
   r   r   r   r   ÚosÚsystemÚ	Exceptionr   r   ÚxÚinputÚwÚmainÚbannÚmenuÚKeyboardInterruptr   )ÚeÚtar   r   r   ÚprossmK   s    
r#   c              C   s^   dddg} xN| D ]F}t td t d t d t d | dd	f tj ¡  t d
¡ qW d S )Nz .   z ..  z ... z[õ   Ãú]ZDownloadingÚ )ÚendgÙ?)	r   r   r   Úlgr   r   ÚflushÚtimeÚsleep)ÚkZanr   r   r   Úanim^   s
    

. 
 r-   c              C   s0  d} d}d}d}yòt jdtd}| ¡  x| ¡ r:t  q*W td|  d | d	 |  d
 | d  t| d | d	 |  d
 | td  d | d t td   y0t	| d | }|dkrÆt
  nt  t  W n* tk
rþ   t| d |  t  Y nX W n( tk
r*   t| d  t  Y nX d S )Nz[91mz[92mz[97mz[0mZsantay)ÚnameÚtargetÚ
ú[r$   r%   zDownload completed !!r   z file saved in:z	 Results/é   z   Want to try gain ? (y/n): r   z	
CanceledzHStorage error.
please restart and give SYTD permission to access storage)Ú	threadingÚThreadÚtrgÚstartÚisAliver-   r   Úfrmtr   r   r   r   r   r    r   r   )r   r(   r   r   Ztrr"   r   r   r   Útrdc   s.    

(@
r9   c              C   sj  da g ayttd t d t d t d t } x@| dkrtttd  ttd t d t d t d t } q6W ttd t d t d t d t  dd	¡attd t d t d t d
 t d t d t d t d t }xL|dkr:|dkr:ttd  ttd t d t d t d t }qðW tdkrLdan yt	 
d¡ W n   Y nX ttd t d t d t d  |dkrddgata yÈd}g at | ¡atjjdd ¡ }xR|D ]J}|d7 }t |j¡ ttd t |td t d t|jtdt|j	 qÎW tttd t d t d t d t d t d t d  t d! t aW n¢ tjjk
r   ttd t d t d t d" t  y2ttd# t }|d$krÌt  nt  t  W n, t k
r   ttd% t  t!  Y nX Y nX t"  n~d&d'gat#a yÈd}g at | ¡atjjdd( ¡ }xR|D ]J}t |j¡ |d7 }ttd t |td t d t|jtd)t|j$	 qPW tttd t d t d t d* t d t d t d  t d! t aW n¢ tjjk
r   ttd t d t d t d" t  y2ttd# t }|d$krNt  nt  t  W n, t k
r   ttd% t  t!  Y nX Y nX t"  W nÌ t k
rÄ   ttd% t  t!  Y n¢ t%k
rd } zttd t d t d | y2ttd# t }|d$krt  nt  t  W n, t k
rR   ttd% t  t!  Y nX W d d }~X Y nX d S )+Nr&   r1   r$   r%   zYoutube video url: z   Url don't be blankzOutput file name: ú Ú_zOutput file type Úvz(video) or Úmz	(music): zJust v(video) or m(mp3) onlyz'Output file type v(video) or m(music): Z	SYTD_FILEr   z,Connecting to the Youtube.com, please wait..ZVideoz
_video.mp4éÿÿÿÿT)Zprogressiver2   z   [zFormat type :zResolution :zSelect the quality ú(Únewú)z: z'Download failed. Please check your url.z   Want to try gain ? (y/n): r   z	
CanceledZMusicz
_music.mp3)Z
only_audioz	Bitrate :zSelect the quality)&r5   r8   r   r   r   r(   r   Úreplacer   r   Úmkdirr   r   ÚpytubeZYouTuber   r	   ÚfilterÚallÚappendZitagÚylZ	mime_typeÚ
resolutionÚintr   r   Ú
exceptionsZRegexMatchErrorr   r   r   r    r   r9   r#   Zabrr   )ZlinkZvmZnoZvidÚir"   Zaur!   r   r   r   r   }   s¤    (
,0H,
$


6P(




6P(





r   c              C   sf   t d } t d¡ x$| D ]}t|ddf t d¡ qW tt d  ttd d¡  tt d  d S )	Nuè  
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
r   r&   )r'   ga2U0*©3?z7=======================================================z1S I M P L E   Y O U T U B E   D O W N L O A D E Ré7   )r   r   r   r   r*   r+   r(   Úcenter)r   rL   r   r   r   r   â   s    

 r   c              C   s  t td t d t d t d  t td t d t d t d  t td t d t d t d	  t td t d
 t d t d t d t d t d  t td t d t d t d  yttd t d t d t } xx| dkrh| dkrh| dkrh| d
krh| dkrh| dkrht td |  d t  ttd t d t d t } qòW | dkrt td  t  nZ| dkrt  nH| dkr¬t	  n6| d
kr¾t
  n$| dkrÐt  nt td  t  W n, tk
r   t td t  t  Y nX d S )Nz
[Ú1r%   z Startr1   Ú2z AboutÚ3z Quick TutorialÚ4z Update r?   r@   rA   Ú0z Exit
ZSYTDú/z> r&   zOption z is not in the menu list.z7=======================================================z
Blank input detected !z	
Canceled)r   r   r   r(   rH   r   r   r   ÚaboutÚtutorialÚupdater   r    )Úopsr   r   r   r   ÿ   s4    $$$<$ >$





r   c               C   sà   t td  t td t d t d t d t d t d t d t d	 t d
 t d t d t d t d t d t d t d t d t d t d t d t d  t td  ttd  t  t	  d S )Nz7=======================================================z
Name         :z Simple Youtube Downloader
zVersion      :z 3.0 r?   z?last updated on
               December 21st, 2018; 11:25PM WIBz)
zDate         :z" December 12th, 2018; 12:17PM WIB
zAuthor       :z  Karjok Pangesty
               zhttps://t.me/om_karjokzTeam         :z. Cracker Noob Squads Indonesia
               zhttps://t.me/CRABS_IDzThanks to    :z Allah SWT, my Agustinna Pangesty,
               all member of CRABS, and all who have
               supported and bullying me.
      zPres enter to back to menu)
r   r   r(   r   ÚgrÚitÚixr   r   r   r   r   r   r   rU     s    	¢rU   c               C   s\   t td  t td t d t d t d  t td  ttd t  t  t  d S )Nz7=======================================================z
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
zPress enter to back to menu)r   r   r(   r   r   r   r   r   r   r   r   rV   1  s    rV   c              C   sÔ   t td  t td  yztj d¡} t td  t td  t td t  t 	d¡ t
jdgd	t
jt
jd
 t td  t d¡ t 	d¡ W n< tjjk
rÎ   t td  ttd  t  t  Y nX d S )Nz7=======================================================z
Checking the connection..zhttps://m.facebook.comu   Connection OK âzUpdating the program..z<This may take a few minutes, don't be cancel !
Please wait..zcd && rm -rf SYTDz.cd && git clone https://github.com/karjok/SYTDT)r   r   r   zRestarting the program..g      à?zcd ../SYTD && python sytd.pyznConnection error detected !
SYTD program need an internet connection.
Please check it before use this program.zPress enter to back to menu)r   r   rH   ÚurllibÚrequestÚurlopenr(   r   r   r   Ú
subprocessÚcallÚDEVNULLÚSTDOUTr*   r+   ÚerrorÚURLErrorr   r   r   )Úrqr   r   r   rW   D  s"    

rW   c               C   s4   t td t t d t t d t  t ¡  d S )NzRIf you have any problem or questions with this tool,
Please contact the Author at zhttps://t.me/om_karjok
zExit !
)r   r   rZ   r(   r[   r   r   r   r   r   r   r   r   X  s    (r   Ú__main__)*r   r(   r   rY   r   rH   rZ   r[   Zirr*   r   r3   r   r_   Zurllib.requestr\   r`   ra   rb   rD   r   r   r]   r^   re   rc   rd   r   r    r   r!   r   r#   r-   r9   r   r   r   rU   rV   rW   Ú__name__r   r   r   r   Ú<module>	   sP   0


e	
