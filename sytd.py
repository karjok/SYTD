B
    %Έ\Ω9  γ            
   @   s0  d Z dZdZdZdZdZdZdZdZd	d
l	Z	d	d
l
Z
d	d
lZd	d
lZd	d
lZd	d
lZy>e d‘ eed  ej d‘Zeed  eed  W n ejjk
rΌ   ee d  e  Y n^ ek
rδ   ee d e  e  Y n6 ek
r Z zee e  e  W d
d
Z[X Y nX dd Zdd Zy2ejdedZe ‘  xe  ‘ rXe  qDW W n` ek
r   ee d e  e  Y n6 ek
rΌ Z zee e  e  W d
d
Z[X Y nX dd Z!dd Z"dd Z#dd Z$d d! Z%d"d# Z&d$d% Z'd&d' Z(d(d) Z)d*d+ Z*d,d- Ze+d.kr,e&  e'  d
S )/z[91mz[92mz[97mz[90mz[0mz[93mz[3mz[23mz[30mι    NΪclearz
# Checking the connection..zhttps://m.facebook.comu   # Connection OK βzΉ# Preparing the required module..
  If you use it in first time,
  It may takes few minutes depends your connection speed.
  Cancelling this process maybe give you
  an error in future.znConnection error detected !
SYTD program need an internet connection.
Please check it before use this program.z	
Canceledc           	   C   sz   yJydd l } W n8 tk
rF   ttd  tjdgdtjtjd Y nX W n* tk
rt   tt	d t
  t  Y nX d S )Nr   z# Installing required modulezcd && pip install pytubeT)ΪshellΪstdoutΪstderrz	
Canceled)ΪpytubeΪImportErrorΪprintΪylΪ
subprocessΪcallΪDEVNULLΪSTDOUTΪKeyboardInterruptΪlrΪxΪexit)r   © r   ϊyt.pyΪupdt*   s    "r   c           
   C   sΆ   t d td t  d td t d t  d td t d t d t d t d t d t d t d t d t d td g	} x6| D ].}ttd	 | d
df tj ‘  t 	d‘ qW d S )Nu   β’     u   β’ u   β’   u   β’u    β’ u     β’ u       β’ u    β’   z# Processing Ϊ )ΪendgΙ?)
ΪwΪgrΪirr   ΪlgΪsysr   ΪflushΪtimeΪsleep)ΪsΪanr   r   r   Ϊanim1:   s
    z
 
 r!   Zupdating)ΪnameΪtargetc               C   sF   yt jdtd W n. tk
r@   ttd  t  t ‘  Y nX d S )NΪResults)ΪfilenamezKPermission error.
Please restart and give SYTD permission to access storage)ΪstΪdownloadΪnamafileΪPermissionErrorr   r   r   r   r   r   r   r   ΪprossvQ   s    r*   c              C   sς   yVt jdtd dt d t d t d } tj| dtjtjd t d	t d
 ‘ W n t	k
rμ } zxt
td t d t  y0ttd t }|dkr’t  nt  t  W n* tk
rΪ   t
td t  t  Y nX W d d }~X Y nX d S )Nr$   )r%   zffmpeg -i Results/z.mp4 -f mp3 z.mp3 && mv z.mp3 ResultsT)r   r   r   zcd Results && rm z.mp4z0Package ffmpeg not installed.
Please install it z$pkg install ffmpegz   Want to try gain ? (y/n): Ϊyz	
Canceled)r&   r'   r(   r
   r   r   r   ΪosΪsystemΪ	Exceptionr   r   r	   r   Ϊinputr   ΪmainΪbannΪmenur   r   )ZffΪeΪtar   r   r   ΪprossmZ   s     
r5   c              C   s^   dddg} xN| D ]F}t td t d t d t d | dd	f tj ‘  t d
‘ qW d S )Nz .   z ..  z ... z[υ   Γϊ]ZDownloadingr   )r   gΩ?)	r   r   r   r   r   r   r   r   r   )Ϊkr    r   r   r   Ϊanimo   s
    

. 
 r9   c              C   s0  d} d}d}d}yςt jdtd}| ‘  x| ‘ r:t  q*W td|  d | d	 |  d
 | d  t| d | d	 |  d
 | td  d | d t td   y0t	| d | }|dkrΖt
  nt  t  W n* tk
rώ   t| d |  t  Y nX W n( tk
r*   t| d  t  Y nX d S )Nz[91mz[92mz[97mz[0mZsantay)r"   r#   Ϊ
ϊ[r6   r7   zDownload completed !!r   z file saved in:z	 Results/ι   z   Want to try gain ? (y/n): r+   z	
CanceledzHStorage error.
please restart and give SYTD permission to access storage)Ϊ	threadingΪThreadΪtrgΪstartΪisAliver9   r   Ϊfrmtr(   r/   r0   r1   r2   r   r   r)   )r   r   r   r   Ztrr4   r   r   r   Ϊtrdt   s.    

(@
rC   c              C   sN  dd l } dag ayjttd t d t d t d t }x@|dkr|ttd  ttd t d t d t d t }q>W ttd t d t d t d t  d	d
‘a	ttd t d t d t d t d t d t d t d t }xL|dkrB|dkrBttd  ttd t d t d t d t }qψW |dkr\ddgat
anddgatat	dkrxda	n yt d‘ W n   Y nX ttd t d t d t d  y|  |‘}|j ‘ aW n’ | jjk
rr   ttd t d t d t d t  y2ttd t }|dkr2t  nt  t  W n, tk
rl   ttd t  t  Y nX Y nX t  W nΜ tk
r¨   ttd t  t  Y n’ tk
rH } zttd t d t d | y2ttd t }|dkrόt  nt  t  W n, tk
r6   ttd t  t  Y nX W d d }~X Y nX d S )Nr   r   r;   r6   r7   zYoutube video url: z   Url don't be blankzOutput file name: ϊ Ϊ_zOutput file type Ϊvz(video) or Ϊmz	(music): zJust v(video) or m(mp3) onlyz'Output file type v(video) or m(music): ZVideoz.mp4ZMusicz.mp3Z	SYTD_FILEr$   z,Connecting to the Youtube.com, please wait..z'Download failed. Please check your url.z   Want to try gain ? (y/n): r+   z	
Canceled)r   r?   rB   r/   r   r   r   r   Ϊreplacer(   r*   r5   r,   ΪmkdirZYouTubeZstreamsΪfirstr&   Ϊ
exceptionsZRegexMatchErrorr   r0   r1   r2   r   r   rC   r.   )r   ZlinkZvmr+   r4   r3   r   r   r   r0      sn    (
,0H,

$

(





r0   c              C   sf   t d } t d‘ x$| D ]}t|ddf t d‘ qW tt d  ttd d‘  tt d  d S )	Nuθ  
  β ββββββββ β ¬βββββ β β’ββββ ββββββββββββββ  ββββββ
 β‘βββββββββ βββββββ  β£ββββ  βββββββββββ    βββββββββββ
β’ββββββββββ ββββββ β β£Όβββββ‘§ βββββββββββ    βββββββββββ
βββββββ£―β£ββββ‘ β’Ίββββββ£ββββββ£Έβ β    βββββ  β β    βββββββββββββ 
ββββββ’Ό β β β   β β ββββββ‘ββββββ β β    βββββ     β  βββββ  β’©βββββ
βββββββ  β  β    β‘Ώββββββββββ‘      βββββ      β βββββ β β βββββ
βββββββββ£β     β βββββββββ‘ β    β  ββββ       βββββ   βββββ
β ββββββββββ β β  βββββββββ’¦β      β ββββ       ββββββ  β βββββ
β  βββββββββββ’ͺ   βββββββ£β     β   ββββ       ββββββ β β β ββββ
β β β β’Όβ‘§ββββββββ β β βββββββ °  β      ββββ      β βββββ   βββββ
β β  β    βββββββ  β β‘ βββββ ½ β β  β   β β βββββ       βββββ β  βββββ
β β   β  β β βββββ   β ββββ     β β β β β βββββ      β ββββββ  β βββββ
β βββ£β β  β βββββ  β  βββββ β β   β β β  β ββββ       βββββ  ββββββ
β£ββββββββββββ  β  βββββ     β β    βββββ     β  ββββββββββββ
βββββββββββββ  β  βββββ     β  β β β ββββ     β β ββββββββββββ£²
β ββββββββββββ     βββββ    β     β ββββ       βββββββββ
 β β£βββββββ£β£β   β β β β£ββββ      β  β β β‘Ώβββ β      β Ήβββββββ‘β 
r   r   )r   ga2U0*©3?z7=======================================================z1S I M P L E   Y O U T U B E   D O W N L O A D E Rι7   )r   r,   r-   r   r   r   r   Ϊcenter)r   Ϊir   r   r   r1   ΰ   s    

 r1   c              C   s  t td t d t d t d  t td t d t d t d  t td t d t d t d	  t td t d
 t d t d t d t d t d  t td t d t d t d  yttd t d t d t } xx| dkrh| dkrh| dkrh| d
krh| dkrh| dkrht td |  d t  ttd t d t d t } qςW | dkrt td  t  nZ| dkrt  nH| dkr¬t	  n6| d
krΎt
  n$| dkrΠt  nt td  t  W n, tk
r   t td t  t  Y nX d S )Nz
[Ϊ1r7   z Startr;   Ϊ2z AboutΪ3z Quick TutorialΪ4z Update ϊ(Ϊnewϊ)Ϊ0z Exit
ZSYTDϊ/z> r   zOption z is not in the menu list.z7=======================================================z
Blank input detected !z	
Canceled)r   r   r   r   r	   r/   r   r0   ΪaboutΪtutorialΪupdater   r   )Ϊopsr   r   r   r2   ύ   s4    $$$<$ >$





r2   c               C   sΰ   t td  t td t d t d t d t d t d t d t d	 t d
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
r   r   r   r   r   ΪitΪixr/   r1   r2   r   r   r   r   rX     s    	’rX   c               C   s\   t td  t td t d t d t d  t td  ttd t  t  t  d S )Nz7=======================================================z
What Is This ?
--------------zw
SYTD (Simple Youtube Downloader) is a simple tool
for download youtube video and convert it 
into video or music file.z!

How To Use It ?
---------------aΎ  
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
zPress enter to back to menu)r   r   r   r   r/   r1   r2   r   r   r   r   rY   /  s    rY   c              C   sΤ   t td  t td  yztj d‘} t td  t td  t td t  t 	d‘ t
jdgd	t
jt
jd
 t td  t d‘ t 	d‘ W n< tjjk
rΞ   t td  ttd  t  t  Y nX d S )Nz7=======================================================z
Checking the connection..zhttps://m.facebook.comu   Connection OK βzUpdating the program..z<This may take a few minutes, don't be cancel !
Please wait..zcd && rm -rf SYTDz.cd && git clone https://github.com/karjok/SYTDT)r   r   r   zRestarting the program..g      ΰ?zcd ../SYTD && python sytd.pyznConnection error detected !
SYTD program need an internet connection.
Please check it before use this program.zPress enter to back to menu)r   r   r	   ΪurllibΪrequestΪurlopenr   r   r,   r-   r
   r   r   r   r   r   ΪerrorΪURLErrorr/   r1   r2   )Ϊrqr   r   r   rZ   B  s"    

rZ   c               C   s4   t td t t d t t d t  t ‘  d S )NzRIf you have any problem or questions with this tool,
Please contact the Author at zhttps://t.me/om_karjok
zExit !
)r   r   r\   r   r]   r   r   r   r   r   r   r   r   V  s    (r   Ϊ__main__),r   r   r   r   r   r	   r\   r]   r   r   r   r=   r,   r
   Zurllib.requestr^   r-   r   r_   r`   rc   ra   rb   r   r   r.   r3   r   r!   r>   Ztredr@   rA   r*   r5   r9   rC   r0   r1   r2   rX   rY   rZ   Ϊ__name__r   r   r   r   Ϊ<module>	   sf   0


	
	R	
