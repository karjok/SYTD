B

    Ӻ\�  �            	   @   s�   d Z dZdZdZdZdZddlZddlZddlZddl	Z	ddl
Z
yddlZW n< ek
r�   e
e d e � e
jd	gd
e
je
jd� Y nX dd
� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zedkr�e�  dS )z[91mz[92mz[97mz[0mz[3mz[23m�    NzFModul 'pytube' not installed. SYTD trying to install it. Please wait..zpip install pytubeT)�shell�stdout�stderrc               C   s"   t jtd� t�dt d � d S )N)�filenamezmv z.mp4 Results)�st�download�namafile�os�system� r   r   �yt.py�prossv   s    r
   c           
   C   s�   y^t jtd� dt d t d } tj| dtjtjd� t�dt d � t�d	t d
 � W nP t	k
r� } z2tjdgdtjtjd� t
td t � t
�  W d d }~X Y nX d S )
N)r   z
ffmpeg -i z.mp4 -f mp3 z.mp3T)r   r   r   zmv z.mp3 Resultszrm z.mp4zpkg install ffmpegzX  Package 'ffmpeg' not installed, but now was done installed it. 
  Restart the program.)r   r   r   �
subprocess�call�DEVNULL�STDOUTr	   r
   �	Exception�print�lr�x�exit)Zff�er   r   r   �prossm   s    r   c              C   s^   dddg} xN| D ]F}t td t d t d t d | dd	�f tj��  t�d
� qW d S )Nz .   z ..  z ... z
[�   ×�]ZDownloading� )�endg�������?)	r   r   �w�lg�sysr   �flush�time�sleep)�kZanr   r   r   �anim#   s
    

. 
 r$   c              C   s^  d} d}d}d}t jdtd�}|��  x|�� r8t�  q(W td|  d | d	 |  d
 | d � t| d | d	 |  d
 | td  d
 | d t td  � yRt	| d | �}|dkr�t
�  n.t| d | d	 |  d
 |  d | � t�  W nd tk
�rX   t| d | d	 |  d
 |  d |  d | d	 |  d
 |  d | � t�  Y nX d S )Nz[91mz[92mz[97mz[0mZsantay)�name�target�
�[r   r   zDownload completed !!r   z file saved in:z	 Results/�   z   Want to try gain ? (y/n): �y�Exitz  Canceled
)
�	threadingZThread�trg�startZisAliver$   r   �frmtr   �input�mainr   �KeyboardInterrupt)r   r   r   r   Ztrr   r   r   �trd'   s&    

(@(
Hr3   c           
   C   s�  da g a�yttd t d t d t d t �} x@| dkrtttd � ttd t d t d t d t �} q6W ttd t d t d t d t ��dd	�attd t d t d t d
 t d t d t d
 t d t �}xL|dk�r:|d
k�r:ttd � ttd t d t d t d t �}q�W |dk�rTddgat	a nddgat
a tdk�rpdan ttd t d t d t d � yt�d� W n t
k
�r�   Y nX yt�| �}|j�� aW nH tjjk
�r   ttd t d t d t d t � t�  Y nX t�  W n� tk
�r�   ttd t d t d t d t d t d t d t d t � t�  Y nr tk
�r� } zRttd t d t d t d t d t d t d t d t � t�  W d d }~X Y nX d S )Nr   r(   r   r   zYoutube video url: z   Url don't be blankzOutput file name: � �_zOutput file type �vz(video) or �mz	(music): zJust v(video) or m(mp3) onlyz%Output file type v(video) or m(mp3): ZVideoz.mp4ZMusicz.mp3Z	SYTD_FILEz,Connecting to the Youtube.com, please wait..ZResultsz(
Download failed. Please check your url.z	Canceled
r+   z2Connections error. Please check your connections.
)r-   r/   r0   r   r   r   r   �replacer   r
   r   r	   �mkdir�OSError�pytubeZYouTubeZstreams�firstr   �
exceptionsZRegexMatchErrorr   r   r3   r2   r   )ZlinkZvmr*   r   r   r   r   r1   =   sJ    (
,0H,

$
(
H
Hr1   c              C   sp   t d t d } t�d� x$| D ]}t|dd�f t�d� q W tt d � ttd�d	� � td
� t	�  d S )Nu�  
  ⠀▕▄▊▆▆▅▃▏ ⠬▍▆▙▊▂ ⠀⢚▂▆▛▆ ▕█▜▜▜▜▛▛▙▛▜▟▆▋  ▅▆▆▆▅▃
 ⡝▌▉▇▇▇▇▇▇▉ ▃▂▆▇▉▀⠀ ⣐▓▉▇▊  ▁▅▇▇▇▇▇▇▇▇▇    ▇▇▇▇▇▇▇▇▇▉▋
⢘▃▇▇▇▇▇▇▇▇▊ ▝▎█▇▇▊ ⠀⣼▙▇▇▃⡧ ▅▇▇▇▇▇▇▇▇▇▇    ▇▇▇▇▇▇▇▇▇▇▅
▔▜▇▇▅▒⣯⣕▏▂▒⡗ ⢺▍▉▇▙▒⣈▒▇▇▉▏⣸⠀⠀   ▃▇▇▅⠀ ⠀⠀   ▁▇▇▇▕░▒█▉▇▉▃⠏
▔▇▇▇▎⢼ ⠀⠀⠀  ⠀⠀▒▊▇▉▃⡏▋▇▇▅▔⠀⠀⠀   ▃▇▇▅⠀    ⠀ ▁▇▇▇▁  ⢩▓▉▇▊▖
▔▉▇▇▓▁⠀ ⠀ ⠀   ⡿▃▇▉▅▁▟▇▇▗⡑      ▃▇▇▅⠀     ⠀▔▇▇▇▔ ⠀⠀▂▛▇▙▃
▔▊▇▇▇▜▃▕⣝⠚    ⠀▝▜▇▛▍▇▇▆⡟ ⠀   ⠀ ▃▇▇▅       ▁▇▇▇▁   ▏▊▇▉▄
⠚▕▉▇▇▇▇▉▆▃▔ ⠀⠀ ▔▄▇▇▉▇▇▃⢦⠀     ⠀▃▇▇▅       ▔▇▇▇▔⠀ ⠀▔▅▇▇▋
⠈ ▔▋▙▇▇▇▇▇▊▂⢪   ▒▉▇▇▇▜⣏⠀    ⠀  ▃▇▇▅       ▔▇▇▇▁⠀⠀⠀⠎▅▇▇▐
⠀⠀⠀⢼⡧▘▅▉▇▇▇▊▒ ⠀⠀▔█▇▇▇▃⠰  ⠀     ▃▇▇▅      ⠀▁▇▇▇▁   ▔▅▇▇▋
⠀⠀ ⠀   ▕█▉▇▉▃⠀ ⠀⡠▝▇▇▉⠽ ⠀⠀ ⠀  ⠀⠀▃▇▇▅⠀      ▔▇▇▇▁ ⠀ ▒▆▇▉▃
⠀⠀  ⠀ ⠀⠀▔▅▇▇▋   ⠀▒▇▇▉     ⠀⠀⠀⠀⠀▃▇▇▅⠀     ⠀▔▇▇▇▔⠀ ⠀▃▙▇▙▍
⠐▕▍⣂⠀⠀ ⠀▒▊▇▇▀  ⠀ ▒▇▇▉⠀⠀⠀  ⠀⠀⠀ ⠀▃▇▇▅       ▁▇▇▇▁  ▝▆▇▇█▕
⣗▄▇▛▌▖▎▍▆▇▇▉▃  ⠀ ▒▇▇▉⠀    ⠀⠀   ▃▇▇▅⠀    ⠀ ▔▇▇▇▒▝█▉▇▇▙▂
▔▟▇▇▇▇▇▇▇▇▉█▁  ⠀ ▒▇▇▉⠀    ⠀ ⠀⠀⠀▃▇▇▅     ⠀⠀▁▇▇▇▇▇▇▇▇▟▍⣲
⠏▃▛▉▇▇▇▇▉▟▃▔⠀    ▒▇▇▉⠀   ⠀    ⠀▃▇▇▅       ▔▉▉▇▇▇▉▜▅
 ⠀⣂▔▏▎▎▕▔⣖⣘⠀  ⠀⠀⠀⣂▎▕▕⠀     ⠀ ⠀⠀⡿▕▎▔ ⠀     ⠹▁▔▕▏▕▔⡏⠜
    u3   S I M P L E  Y O U T U B E⠀  D O W N L O A D E R
�clearr   )r   g���Mb@?z7=======================================================zK A R J O K  P A N G E S T Y�<   r'   )
r   r   r	   r
   r   r!   r"   r   �centerr1   )r   �ir   r   r   �bannk   s    


 rB   c               C   s$   t td t t d t t � d S )NzJIf you have any problem or questions with this tool,
Please contact me at zhttps://t.me/om_karjok)r   r   �itr   �ixr   r   r   r   r   r   �   s    r   �__main__)r   r   r   r   rC   rD   r!   r   r,   r	   r   r;   �ImportErrorr   r   r   r   r
   r   r$   r3   r1   rB   r   �__name__r   r   r   r   �<module>   s(   (.
