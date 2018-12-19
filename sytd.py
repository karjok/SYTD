B
    \-  γ            
   @   s  d Z dZdZdZdZdZdZdZdd	lZdd	l	Z	dd	l
Z
dd	lZdd	lZdd	lZy¬eed
  ej d‘Zeed  eed e  ydd	lZW n, ek
rΎ   ejdgdejejd Y nX e d‘ ejdgdejejd ejdgdejejd W nΆ ek
r*   ejdgdejejd Y n ejjk
rT   ee d  e  Y n` ek
r~   ee d e  e  Y n6 ek
r² Z zee e  e  W d	d	Z[X Y nX dd Zdd Z dd Z!dd Z"dd  Z#d!d" Z$d#d$ Z%d%d& Z&d'd( Z'd)d* Ze(d+kre$  e%  d	S ),z[91mz[92mz[97mz[90mz[0mz[93mz[3mz[23mι    Nz
# Checking the connection..zhttps://m.facebook.comu   # Connection OK βzV# update the program.
  this may take a few minutes, don't be cancel !
  Please wait..zcd && pip install pytubeT)ΪshellΪstdoutΪstderrzcd && rm -rf SYTDz.cd && git clone https://github.com/karjok/SYTDzpkg install ffmpegzpip install pytubeznConnection error detected !
SYTD program need an internet connection.
Please check it before use this program.z	
Canceledc               C   s   t jdtd d S )Nz/sdcard)Ϊfilename)ΪstΪdownloadΪnamafile© r	   r	   ϊyt.pyΪprossv1   s    r   c              C   sN   t jdtd dt d t d } tj| dtjtjd t dt d	 ‘ d S )
Nz/sdcard)r   zffmpeg -i /sdcard/z.mp4 -f mp3 z.mp3T)r   r   r   zcd /sdcard && rm z.mp4)	r   r   r   Ϊ
subprocessΪcallΪDEVNULLΪSTDOUTΪosΪsystem)Zffr	   r	   r
   Ϊprossm5   s    r   c              C   s^   dddg} xN| D ]F}t td t d t d t d | dd	f tj ‘  t d
‘ qW d S )Nz .   z ..  z ... z[υ   Γϊ]ZDownloadingΪ )ΪendgΩ?)	ΪprintΪlrΪwΪlgΪsysr   ΪflushΪtimeΪsleep)ΪkZanr	   r	   r
   Ϊanim<   s
    

. 
 r    c              C   s  d} d}d}d}t jdtd}| ‘  x| ‘ r8t  q(W td|  d | d	 |  d
 | d  t| d | d	 |  d
 | td  d | d t td   y0t	| d | }|dkrΔt
  nt  t  W n* tk
rό   t| d |  t  Y nX d S )Nz[91mz[92mz[97mz[0mZsantay)ΪnameΪtargetΪ
ϊ[r   r   zDownload completed !!r   z file saved in:z	 /sdcard/ι   z   Want to try gain ? (y/n): Ϊyz	
Canceled)Ϊ	threadingZThreadΪtrgΪstartZisAliver    r   Ϊfrmtr   ΪinputΪmainΪbannΪmenuΪKeyboardInterruptΪexit)r   r   r   ΪxZtrΪtar	   r	   r
   Ϊtrd@   s&    

(@
r3   c              C   s  da g ayNttd t d t d t d t } x@| dkrtttd  ttd t d t d t d t } q6W ttd t d t d t d t  dd	‘attd t d t d t d
 t d t d t d t d t }xL|dkr:|dkr:ttd  ttd t d t d t d t }qπW |dkrTddgat	a nddgat
a tdkrpdan ttd t d t d t d  yt | ‘}|j ‘ aW n’ tjjk
rN   ttd t d t d t d t  y2ttd t }|dkrt  nt  t  W n, tk
rH   ttd t  t  Y nX Y nX t  W n, tk
r   ttd t  t  Y nX d S )Nr   r$   r   r   zYoutube video url: z   Url don't be blankzOutput file name: ϊ Ϊ_zOutput file type Ϊvz(video) or Ϊmz	(music): zJust v(video) or m(mp3) onlyz'Output file type v(video) or m(music): ZVideoz.mp4ZMusicz.mp3Z	SYTD_FILEz,Connecting to the Youtube.com, please wait..z'Download failed. Please check your url.z   Want to try gain ? (y/n): r&   z	
Canceled)r(   r*   r+   r   r   r   r   Ϊreplacer   r   r   ΪpytubeZYouTubeZstreamsΪfirstr   Ϊ
exceptionsZRegexMatchErrorr1   r,   r-   r.   r/   r0   r3   )ZlinkZvmr&   r2   r	   r	   r
   r,   V   sP    (
,0H,

$

(


r,   c              C   sf   t d } t d‘ x$| D ]}t|ddf t d‘ qW tt d  ttd d‘  tt d  d S )	Nuθ  
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
Ϊclearr   )r   ga2U0*©3?z7=======================================================z1S I M P L E   Y O U T U B E   D O W N L O A D E Rι7   )r   r   r   r   r   r   r   Ϊcenter)r1   Ϊir	   r	   r
   r-   €   s    

 r-   c              C   sΌ  t td t d t d t d  t td t d t d t d  t td t d t d t d	  t td t d
 t d t d  yϊttd t d t d t } xn| dkr | dkr | dkr | d
kr | dkr t td |  d t  ttd t d t d t } q΄W | dkr@t td  t  nH| dkrRt  n6| dkrdt  n$| d
krvt	  nt td  t	  W n, t
k
rΆ   t td t  t	  Y nX d S )Nz
[Ϊ1r   z Startr$   Ϊ2z AboutΪ3z Quick TutorialΪ0z Exit
ZSYTDϊ/z> r   zOption z is not in the menu list.z7=======================================================z
Blank input detected !z	
Canceled)r   r   r   r   r+   r1   r,   ΪaboutΪtutorialr0   r/   )Zopsr	   r	   r
   r.   Α   s.    $$$$ 4$




r.   c               C   sΰ   t td  t td t d t d t d t d t d t d t d	 t d
 t d t d t d t d t d t d t d t d t d t d t d t d  t td  ttd  t  t	  d S )Nz7=======================================================z
Name         :z Simple Youtube Downloader
zVersion      :z 2.0 ϊ(z>last updated on
               December 15th, 2018; 9:45AM WIBz)
zDate         :z" December 12th, 2018; 12:17PM WIB
zAuthor       :z  Karjok Pangesty
               zhttps://t.me/om_karjokzTeam         :z. Cracker Noob Squads Indonesia
               zhttps://t.me/CRABS_IDzThanks to    :z Allah SWT, my Agustinna Pangesty,
               all member of CRABS, and all who have
               supported and bullying me.
      zPres enter to back to menu)
r   r   r   r1   ΪgrΪitΪixr+   r-   r.   r	   r	   r	   r
   rE   Ϋ   s    	’rE   c               C   s\   t td  t td t d t d t d  t td  ttd t  t  t  d S )Nz7=======================================================z
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
zPress enter to back to menu)r   r   r   r1   r+   r-   r.   r	   r	   r	   r
   rF   π   s    rF   c               C   s4   t td t t d t t d t  t ‘  d S )NzRIf you have any problem or questions with this tool,
Please contact the Author at zhttps://t.me/om_karjok
zExit !
)r   r   rI   r   rJ   r1   r   r0   r	   r	   r	   r
   r0     s    (r0   Ϊ__main__))r   r   r   rH   r1   ZylrI   rJ   r   r   r'   r   r   Zurllib.requestZurllibr   ZrequestZurlopenZrqr9   ΪImportErrorr   r   r   r   ΪerrorZURLErrorr0   r/   Ϊ	ExceptionΪer   r   r    r3   r,   r-   r.   rE   rF   Ϊ__name__r	   r	   r	   r
   Ϊ<module>	   sX   0


N	
