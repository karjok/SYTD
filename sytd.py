B
    ζUP\Τ  γ               @   s   d dl Z ee  d‘ dS )ι    Ns2  γ            
   @   sά  d Z dZdZdZdZdZdZdZdZd	d
l	Z	d	d
l
Z
d	d
lZd	d
lZd	d
lZd	d
lZye d‘ eed  ej d‘Zeed  eed  yd	d
lZW n4 ek
rΠ   ejdgdejejd d	d
lZY nX e	 d‘ W n ejjk
r
   ee d  e  Y n` ek
r4   ee d e  e  Y n6 ek
rh Z  zee e   e  W d
d
Z [ X Y nX dd Z!dd Z"dd Z#dd Z$dd Z%d d! Z&d"d# Z'd$d% Z(d&d' Z)d(d) Z*d*d+ Ze+d,krΨe&  e'  d
S )-z[91mz[92mz[97mz[90mz[0mz[93mz[3mz[23mz[30mι    NΪclearz
# Checking the connection..zhttps://m.facebook.comu   # Connection OK βz!# Preparing the required module..zcd && pip install pytubeT)ΪshellΪstdoutΪstderrg      ΰ?znConnection error detected !
SYTD program need an internet connection.
Please check it before use this program.z	
Canceledc               C   s"   t j tt ‘jdtd d d S )NΪResultsZ_video)Ϊfilename)ΪyΪstreamsΪget_by_itagΪitgΪpiΪdownloadΪnamafile© r   r   ϊ<script>Ϊprossv,   s    r   c               C   s<   t j tt ‘jdtd d t dt d t d ‘ d S )Nr   Z_music)r   zcd Results && mv z_music.mp4 z
_music.mp3)	r   r	   r
   r   r   r   r   ΪosΪsystemr   r   r   r   Ϊprossm@   s    r   c              C   s^   dddg} xN| D ]F}t td t d t d t d | dd	f tj ‘  t d
‘ qW d S )Nz .   z ..  z ... z[υ   Γϊ]ZDownloadingΪ )ΪendgΩ?)	ΪprintΪlrΪwΪlgΪsysr   ΪflushΪtimeΪsleep)ΪkZanr   r   r   ΪanimQ   s
    

. 
 r"   c              C   sf   d} d}d}d}y.t jdtd}| ‘  x| ‘ r:t  q*W W n" tk
r`   td t  Y nX d S )Nz[91mz[92mz[97mz[0mZsantay)ΪnameΪtargetzkoneksi error)	Ϊ	threadingZThreadΪtrgΪstartZisAliver"   ΪConnectionAbortedErrorr   Ϊexit)r   r   r   ΪxZtrr   r   r   ΪtrdV   s    
r+   c        	      C   s^  da g ayttd t d t d t d t } xH| dksFd| kr|ttd  ttd t d t d t d t } q6W ttd t d t d t d t  d	d
‘attd t d t d t d t d t d t d t d t }xL|dkrB|dkrBttd  ttd t d t d t d t }qψW tdkrTdan yt	 
d‘ W n   Y nX ttd t d t d t d  |dkrddgata yRd}g }g at | ‘atjjdd ‘ }x\|D ]T}|d7 }| |‘ t |j‘ ttd t |td t d t|jtdt|j	 qάW ttd t d t d t d t d t d  t d! t d" t axrtdkstt|krξttd#  ttd t d t d t d t d t d  t d! t d" t aq~W ttd aW n’ tjjk
r    ttd t d t d t d$ t  y2ttd% t }|d&kr`t  nt  t   W n, t!k
r   ttd' t  t"  Y nX Y nX y
t#  W n   td( t$ "‘  Y nX td)t d t d t d t d*  ttd t d t d t td  d+ t d, t td   y2ttd% t }|d&krVt  nt  t   W n, t!k
r   ttd' t  t"  Y nX nτd-d.gat%a yRd}g }g at | ‘atjjdd/ ‘ }x\|D ]T}t |j‘ | |‘ |d7 }ttd t |td t d t|jtd0t|j&	 qΤW ttd t d t d t d1 t d t d  t d! t d" t axrtdkstt|krζttd#  ttd t d t d t d1 t d t d  t d! t d" t aqvW ttd aW n’ tjjk
r   ttd t d t d t d$ t  y2ttd% t }|d&krXt  nt  t   W n, t!k
r   ttd' t  t"  Y nX Y nX y
t#  W n   td( t$ "‘  Y nX td)t d t d t d t d*  ttd t d t d t td  d+ t d, t td   y2ttd% t }|d&krNt  nt  t   W n, t!k
r   ttd' t  t"  Y nX W nΜ t!k
rΈ   ttd' t  t"  Y n’ t'k
rX } zttd t d t d | y2ttd% t }|d&krt  nt  t   W n, t!k
rF   ttd' t  t"  Y nX W d d }~X Y nX d S )2Nr   ϊ[r   r   zYoutube video url: zhttps://z    A valid youtube link expectedzOutput file name: ϊ Ϊ_zOutput file type Ϊvz(video) or Ϊmz	(music): zJust v(video) or m(mp3) onlyz'Output file type v(video) or m(music): Z	SYTD_FILEr   z,Connecting to the Youtube.com, please wait..ZVideoz
_video.mp4r   T)Zprogressiveι   z   [zFormat type :zResolution :zSelect the quality ϊ(Ϊnewϊ)z: z   Invalid inputz'Download failed. Please check your url.z   Want to try gain ? (y/n): r   z	
CanceledZerorΪ
zDownload completed !!z file saved in:z	 Results/ZMusicz
_music.mp3)Z
only_audioz	Bitrate :zSelect the quality)(r&   ZfrmtΪinputr   r   r   r   Ϊreplacer   r   Ϊmkdirr   r   ΪpytubeZYouTuber   r	   ΪfilterΪallΪappendZitagΪylZ	mime_typeZ
resolutionr*   r   ΪstrΪintZ
exceptionsZRegexMatchErrorΪmainΪbannΪmenuΪKeyboardInterruptr)   r+   r   r   ZabrΪ	Exception)	ZlinkZvmZnoΪrngZvidΪiZtaZauΪer   r   r   r@   j   sψ    (,0H,
$



6HN(


(@




6HN(


(@




r@   c              C   sf   t d } t d‘ x$| D ]}t|ddf t d‘ qW tt d  ttd d‘  tt d  d S )	Nuθ  
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
r   r   )r   ga2U0*©3?z7=======================================================z1S I M P L E   Y O U T U B E   D O W N L O A D E Rι7   )r   r   r   r   r   r    r   Ϊcenter)r*   rF   r   r   r   rA     s    

 rA   c              C   s  t td t d t d t d  t td t d t d t d  t td t d t d t d	  t td t d
 t d t d t d t d t d  t td t d t d t d  yttd t d t d t } xx| dkrh| dkrh| dkrh| d
krh| dkrh| dkrht td |  d t  ttd t d t d t } qςW | dkrt td  t  nZ| dkrt  nH| dkr¬t	  n6| d
krΎt
  n$| dkrΠt  nt td  t  W n, tk
r   t td t  t  Y nX d S )Nz
[Ϊ1r   z Startr,   Ϊ2z AboutΪ3z Quick TutorialΪ4z Update r2   r3   r4   Ϊ0z Exit
ZSYTDϊ/z> r   zOption z is not in the menu list.z7=======================================================z
Blank input detected !z	
Canceled)r   r   r   r   r=   r6   r*   r@   ΪaboutΪtutorialΪupdater)   rC   )Zopsr   r   r   rB      s4    $$$<$ >$





rB   c               C   sΰ   t td  t td t d t d t d t d t d t d t d	 t d
 t d t d t d t d t d t d t d t d t d t d t d t d  t td  ttd  t  t	  d S )Nz7=======================================================z
Name         :z Simple Youtube Downloader
zVersion      :z 3.2 r2   z=last updated on
               January 29th, 2019; 8:16PM WIBz)
zDate         :z" December 12th, 2018; 12:17PM WIB
zAuthor       :z  Karjok Pangesty
               zhttps://t.me/om_karjokzTeam         :z. Cracker Noob Squads Indonesia
               zhttps://t.me/CRABS_IDzThanks to    :z Allah SWT, my Agustinna Pangesty,
               all member of CRABS, and all who have
               supported and bullying me.
      zPres enter to back to menu)
r   r   r   r=   ΪgrΪitΪixr6   rA   rB   r   r   r   r   rP   =  s    	’rP   c               C   s\   t td  t td t d t d t d  t td  ttd t  t  t  d S )Nz7=======================================================z
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
the file save in Results directory.
zPress enter to back to menu)r   r   r   r=   r6   r*   rA   rB   r   r   r   r   rQ   R  s    rQ   c              C   s  t td  t td  t td  ttd t } | dkrHt  t  t td  yzt	j
 d‘}t td  t td	  t td
 t  t d‘ tjdgdtjtjd t td  t d‘ t d‘ W n> t	jjk
r   t td  ttd  t  t  Y nX d S )Nz7=======================================================z4After this operation, all SYTD data will be deleted.z_Tips: Move all file that you download
      (in Results directory) to other folder for safe it.zContinue ? y/n : Ϊnz
# Checking the connection..zhttps://m.facebook.comu   Connection OK βz
# Updating the program..z<This may take a few minutes, don't be cancel !
Please wait..zcd && rm -rf SYTDz.cd && git clone https://github.com/karjok/SYTDT)r   r   r   z
# Restarting the program..g      ΰ?zcd ../SYTD && python sytd.pyznConnection error detected !
SYTD program need an internet connection.
Please check it before use this program.zPress enter to back to menu)r   r   r=   rS   r6   r   r*   rA   rB   ΪurllibΪrequestΪurlopenr   r   Ϊ
subprocessΪcallΪDEVNULLΪSTDOUTr   r    ΪerrorΪURLError)ZcntΪrqr   r   r   rR   e  s.    

rR   c               C   s4   t td t t d t t d t  t ‘  d S )NzRIf you have any problem or questions with this tool,
Please contact the Author at zhttps://t.me/om_karjok
zExit !
)r   r   rT   r   rU   r*   r   r)   r   r   r   r   r)     s    (r)   Ϊ__main__),r   r   r   rS   r*   r=   rT   rU   Zirr   r   r%   r   rZ   Zurllib.requestrW   r   r   rX   rY   r`   r9   ΪModuleNotFoundErrorr[   r\   r]   r    r^   r_   r)   rC   rD   rG   r   r   r"   r+   r@   rA   rB   rP   rQ   rR   Ϊ__name__r   r   r   r   Ϊ<module>	   sZ   0


 	
)ΪmarshalΪexecΪloads© r   r   ϊsytd.pyΪ<module>   s   