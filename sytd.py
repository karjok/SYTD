B
    É\=  ã            
   @   st  d Z dZdZdZdZdZdZdZdZd	d
l	Z	d	d
l
Z
d	d
lZd	d
lZd	d
lZd	d
lZyd	d
lZW n, ek
r   ejdgdejejd Y nX d	d
lZy>e d¡ eed  ej d¡Zeed  eed  W n ejjk
rþ   ee d  e  Y n` ek
r(   ee d e  e  Y n6 ek
r\ Z zee e  e  W d
d
Z[X Y nX dd Z dd Z!y2ej"de dZ#e# $¡  xe# %¡ re!  qW W n` ek
rÌ   ee d e  e  Y n6 ek
r  Z zee e  e  W d
d
Z[X Y nX dd Z&dd Z'dd  Z(d!d" Z)d#d$ Z*d%d& Z+d'd( Z,d)d* Z-d+d, Z.d-d. Z/d/d0 Ze0d1krpe+  e,  d
S )2z[91mz[92mz[97mz[90mz[0mz[93mz[3mz[23mz[30mé    Nzcd && pip install pytubeT)ÚshellÚstdoutÚstderrÚclearz
# Checking the connection..zhttps://m.facebook.comu   # Connection OK âz!# Preparing the required module..znConnection error detected !
SYTD program need an internet connection.
Please check it before use this program.z	
Canceledc           	   C   sf   ydd l } W nT tk
r8   tjdgdtjtjd Y n* tk
r`   ttd t	  t
  Y nX d S )Nr   zpip install pytubeT)r   r   r   z	
Canceled)ÚpytubeÚModuleNotFoundErrorÚ
subprocessÚcallÚDEVNULLÚSTDOUTÚKeyboardInterruptÚprintÚlrÚxÚexit)r   © r   úyt.pyÚupdt0   s    r   c           
   C   s¶   t d td t  d td t d t  d td t d t d t d t d t d t d t d t d t d td g	} x6| D ].}ttd	 | d
df tj ¡  t 	d¡ qW d S )Nu   â¢     u   â¢ u   â¢   u   â¢u    â¢ u     â¢ u       â¢ u    â¢   z# Processing Ú )ÚendgÉ?)
ÚwÚgrÚirr   ÚlgÚsysr   ÚflushÚtimeÚsleep)ÚsÚanr   r   r   Úanim19   s
    z
 
 r    Zupdating)ÚnameÚtargetc               C   sV   y"t j tt ¡jdtd d W n. tk
rP   tt	d  t
  t 
¡  Y nX d S )NÚResultsZ_video)ÚfilenamezKPermission error.
Please restart and give SYTD permission to access storage)ÚyÚstreamsÚget_by_itagÚitgÚpiÚdownloadÚnamafileÚPermissionErrorr   r   r   r   r   r   r   r   ÚprossvM   s    "r-   c              C   sÐ   y<t j tt ¡jdtd d t dt d t d ¡ W n t	k
rÊ }  zpt
t|  t  y0ttd t }|dkrt  nt  t  W n* tk
r¸   t
td	 t  t  Y nX W d d } ~ X Y nX d S )
Nr#   Z_music)r$   zcd Results && mv z_music.mp4 z
_music.mp3z   Want to try gain ? (y/n): r%   z	
Canceled)r%   r&   r'   r(   r)   r*   r+   ÚosÚsystemÚ	Exceptionr   r   r   Úinputr   ÚmainÚbannÚmenur   r   )ÚeÚtar   r   r   ÚprossmU   s    
r7   c              C   s^   dddg} xN| D ]F}t td t d t d t d | dd	f tj ¡  t d
¡ qW d S )Nz .   z ..  z ... z[õ   Ãú]ZDownloadingr   )r   gÙ?)	r   r   r   r   r   r   r   r   r   )Úkr   r   r   r   Úanimh   s
    

. 
 r;   c              C   s0  d} d}d}d}yòt jdtd}| ¡  x| ¡ r:t  q*W td|  d | d	 |  d
 | d  t| d | d	 |  d
 | td  d | d t td   y0t	| d | }|dkrÆt
  nt  t  W n* tk
rþ   t| d |  t  Y nX W n( tk
r*   t| d  t  Y nX d S )Nz[91mz[92mz[97mz[0mZsantay)r!   r"   Ú
ú[r8   r9   zDownload completed !!r   z file saved in:z	 Results/é   z   Want to try gain ? (y/n): r%   z	
CanceledzHStorage error.
please restart and give SYTD permission to access storage)Ú	threadingÚThreadÚtrgÚstartÚisAliver;   r   Úfrmtr+   r1   r2   r3   r4   r   r   r,   )r   r   r   r   Ztrr6   r   r   r   Útrdm   s.    

(@
rE   c              C   sj  da g ayttd t d t d t d t } x@| dkrtttd  ttd t d t d t d t } q6W ttd t d t d t d t  dd	¡attd t d t d t d
 t d t d t d t d t }xL|dkr:|dkr:ttd  ttd t d t d t d t }qðW tdkrLdan yt	 
d¡ W n   Y nX ttd t d t d t d  |dkrddgata yÈd}g at | ¡atjjdd ¡ }xR|D ]J}|d7 }t |j¡ ttd t |td t d t|jtdt|j	 qÎW tttd t d t d t d t d t d t d  t d! t aW n¢ tjjk
r   ttd t d t d t d" t  y2ttd# t }|d$krÌt  nt  t  W n, t k
r   ttd% t  t!  Y nX Y nX t"  n~d&d'gat#a yÈd}g at | ¡atjjdd( ¡ }xR|D ]J}t |j¡ |d7 }ttd t |td t d t|jtd)t|j$	 qPW tttd t d t d t d* t d t d t d  t d! t aW n¢ tjjk
r   ttd t d t d t d" t  y2ttd# t }|d$krNt  nt  t  W n, t k
r   ttd% t  t!  Y nX Y nX t"  W nÌ t k
rÄ   ttd% t  t!  Y n¢ t%k
rd } zttd t d t d | y2ttd# t }|d$krt  nt  t  W n, t k
rR   ttd% t  t!  Y nX W d d }~X Y nX d S )+Nr   r=   r8   r9   zYoutube video url: z   Url don't be blankzOutput file name: ú Ú_zOutput file type Úvz(video) or Úmz	(music): zJust v(video) or m(mp3) onlyz'Output file type v(video) or m(music): Z	SYTD_FILEr#   z,Connecting to the Youtube.com, please wait..ZVideoz
_video.mp4éÿÿÿÿT)Zprogressiver>   z   [zFormat type :zResolution :zSelect the quality ú(Únewú)z: z'Download failed. Please check your url.z   Want to try gain ? (y/n): r%   z	
CanceledZMusicz
_music.mp3)Z
only_audioz	Bitrate :zSelect the quality)&rA   rD   r1   r   r   r   r   Úreplacer+   r.   Úmkdirr-   r(   r   ZYouTuber%   r&   ÚfilterÚallÚappendZitagÚylZ	mime_typeÚ
resolutionÚintr   r)   Ú
exceptionsZRegexMatchErrorr2   r3   r4   r   r   rE   r7   Zabrr0   )ZlinkZvmZnoZvidÚir6   Zaur5   r   r   r   r2      s¤    (
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
r2   c              C   sf   t d } t d¡ x$| D ]}t|ddf t d¡ qW tt d  ttd d¡  tt d  d S )	Nuè  
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
r   r   )r   ga2U0*©3?z7=======================================================z1S I M P L E   Y O U T U B E   D O W N L O A D E Ré7   )r   r.   r/   r   r   r   r   Úcenter)r   rW   r   r   r   r3   ì   s    

 r3   c              C   s  t td t d t d t d  t td t d t d t d  t td t d t d t d	  t td t d
 t d t d t d t d t d  t td t d t d t d  yttd t d t d t } xx| dkrh| dkrh| dkrh| d
krh| dkrh| dkrht td |  d t  ttd t d t d t } qòW | dkrt td  t  nZ| dkrt  nH| dkr¬t	  n6| d
kr¾t
  n$| dkrÐt  nt td  t  W n, tk
r   t td t  t  Y nX d S )Nz
[Ú1r9   z Startr=   Ú2z AboutÚ3z Quick TutorialÚ4z Update rK   rL   rM   Ú0z Exit
ZSYTDú/z> r   zOption z is not in the menu list.z7=======================================================z
Blank input detected !z	
Canceled)r   r   r   r   rS   r1   r   r2   ÚaboutÚtutorialÚupdater   r   )Úopsr   r   r   r4   	  s4    $$$<$ >$





r4   c               C   sà   t td  t td t d t d t d t d t d t d t d	 t d
 t d t d t d t d t d t d t d t d t d t d t d t d  t td  ttd  t  t	  d S )Nz7=======================================================z
Name         :z Simple Youtube Downloader
zVersion      :z 3.0 rK   z?last updated on
               December 21st, 2018; 11:25PM WIBz)
zDate         :z" December 12th, 2018; 12:17PM WIB
zAuthor       :z  Karjok Pangesty
               zhttps://t.me/om_karjokzTeam         :z. Cracker Noob Squads Indonesia
               zhttps://t.me/CRABS_IDzThanks to    :z Allah SWT, my Agustinna Pangesty,
               all member of CRABS, and all who have
               supported and bullying me.
      zPres enter to back to menu)
r   r   r   r   r   ÚitÚixr1   r3   r4   r   r   r   r   r`   &  s    	¢r`   c               C   s\   t td  t td t d t d t d  t td  ttd t  t  t  d S )Nz7=======================================================z
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
zPress enter to back to menu)r   r   r   r   r1   r3   r4   r   r   r   r   ra   ;  s    ra   c              C   sÔ   t td  t td  yztj d¡} t td  t td  t td t  t 	d¡ t
jdgd	t
jt
jd
 t td  t d¡ t 	d¡ W n< tjjk
rÎ   t td  ttd  t  t  Y nX d S )Nz7=======================================================z
Checking the connection..zhttps://m.facebook.comu   Connection OK âzUpdating the program..z<This may take a few minutes, don't be cancel !
Please wait..zcd && rm -rf SYTDz.cd && git clone https://github.com/karjok/SYTDT)r   r   r   zRestarting the program..g      à?zcd ../SYTD && python sytd.pyznConnection error detected !
SYTD program need an internet connection.
Please check it before use this program.zPress enter to back to menu)r   r   rS   ÚurllibÚrequestÚurlopenr   r   r.   r/   r   r	   r
   r   r   r   ÚerrorÚURLErrorr1   r3   r4   )Úrqr   r   r   rb   N  s"    

rb   c               C   s4   t td t t d t t d t  t ¡  d S )NzRIf you have any problem or questions with this tool,
Please contact the Author at zhttps://t.me/om_karjok
zExit !
)r   r   rd   r   re   r   r   r   r   r   r   r   r   b  s    (r   Ú__main__)1r   r   r   r   r   rS   rd   re   r   r   r   r?   r.   r   Zurllib.requestrf   r   r   r	   r
   r   r/   r   rg   rh   rk   ri   rj   r   r   r0   r5   r   r    r@   ZtredrB   rC   r-   r7   r;   rE   r2   r3   r4   r`   ra   rb   Ú__name__r   r   r   r   Ú<module>	   sp   0


	
e	
