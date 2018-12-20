
#12 Desember 2018, 12:17PM
#SYTD
#Karjok Pangesty
# @CRABS_ID



lr = '\033[91m'
lg = '\033[92m'
w  = '\033[97m'
gr = '\033[90m'
x  = '\033[0m'
yl = '\033[93m'
it = '\x1B[3m'
ix = '\x1B[23m'
ir = '\033[30m'
import time,sys,threading,os,subprocess,urllib.request
try:
      import pytube
except ImportError:
      subprocess.call(['cd && pip install pytube'],shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)    

try:
      os.system('clear')
      # checking the connection.
      print (yl+'\n# Checking the connection..')
      rq = urllib.request.urlopen('https://m.facebook.com')
      print (lg+'# Connection OK ✓')
      print (yl+'# Preparing the required module..\n  If you use it in first time,\n  It may takes few minutes depends your connection speed.\n  Cancelling this process maybe give you\n  an error in future.')
#      print (yl+"# update the program.\n  this may take a few minutes, don't be cancel !\n  Please wait.."+x)
      #import required modul
except urllib.error.URLError:
      print  (lr+'Connection error detected !\nSYTD program need an internet connection.\nPlease check it before use this program.')
      exit()
except KeyboardInterrupt:
      print (lr+'\nCanceled'+x)
      exit()
except Exception as e:
      print (lr+e)
      exit()

#animation


def updt():
      try:
            try:
                  import pytube
            except ImportError:
#                  print (yl+"# Installing required module")
                  subprocess.call(['cd && pip install pytube'],shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)    
      #updating program from repository
      # installing ffmpeg package
#            subprocess.call(['pkg install ffmpeg -y'], shell= True, stdout= subprocess.DEVNULL, stderr= subprocess.STDOUT)
#except ImportError:
#     print (lr+"Required module is not installed.\nSYTD trying to installing it. Please wait.."+x)
#      subprocess.call(['pip install pytube'], shell= True, stdout= subprocess.DEVNULL, stderr= subprocess.STDOUT)
      except KeyboardInterrupt:
            print (lr+'\nCanceled'+x)
            exit()
def anim1():
#      k = [' .   ',' ..  ',' ... ']
      s = [w+"•     ",gr+"• "+w+"•   ",ir+"•"+gr+" • "+w+"• ",ir+"  • "+gr+"• ",w+"    • ",w+"  • "+gr+"• ",w+"• "+gr+"• "+ir+"• ",w+"•"+ir+" •   ",gr+"•     "]

      for an in s:
            print(lg+'\r# Processing '+an,end=''),;sys.stdout.flush();time.sleep(0.2)


# threading for loading. hehe
try:
      tred = threading.Thread(name='updating',target=updt)
      tred.start()
      while tred.isAlive():
            anim1()
except KeyboardInterrupt:
      print (lr+'\nCanceled'+x)
      exit()
except Exception as e:
      print (lr+e)
      exit()    



def prossv():
      global st
#      os.system('cd && termux-setup-storage')
      try:
            st.download('Results',filename=namafile)
      except PermissionError:
            print (lr+'Permission error.\nPlease restart and give SYTD permission to access storage')
            exit()
            sys.exit()
def prossm():
      global st
#      os.system('cd && termux-setup-storage')
      try:
            st.download('Results',filename=namafile)
            ff= ('ffmpeg -i Results/'+namafile+'.mp4 -f mp3 '+namafile+'.mp3 && mv '+namafile+'.mp3 Results')
            subprocess.call(ff,shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            #os.system('mv '+namafile+'.mp3 /sdcard')
            os.system('cd Results && rm '+namafile+'.mp4')
      except Exception as e:
            print (lr+'Package ffmpeg not installed.\nPlease install it '+yl+'$pkg install ffmpeg'+x)
            try:
                  ta = input(lr+'   Want to try gain ? (y/n): '+w)
                  if ta == 'y':
                        main()
                  else:
                        bann()
                        menu()                 
            except KeyboardInterrupt:
                  print (lr+'\nCanceled'+x)
                  exit()
def anim():
      k = [' .   ',' ..  ',' ... ']
      for an in k:
            print(lr+'\r['+w+'×'+lr+']'+lg+'Downloading'+an,end=''),;sys.stdout.flush();time.sleep(0.4)

def trd():
      lr = '\033[91m'
      lg = '\033[92m'
      w  = '\033[97m'
      x  = '\033[0m'
      try:
            tr = threading.Thread(name='santay',target=trg)
            tr.start()
            while tr.isAlive():
                  anim()
            print ('\n'+lr+'['+w+'×'+lr+']'+lg+'Download completed !!')
            print (lr+'['+w+'×'+lr+']'+lg+frmt[0]+' file saved in:'+w+' Results/'+namafile+frmt[1])
            try:
                  ta = input(lr+'   Want to try gain ? (y/n): '+w)
                  if ta == 'y':
                        main()
                  else:
                        bann()
                        menu()                 
            except KeyboardInterrupt:
                  print (lr+'\nCanceled'+x)
                  exit()
      except PermissionError:
            print (lr+'Storage error.\nplease restart and give SYTD permission to access storage')
            exit()

def main():
      try:
            import pytube
      except ImportError:
            subprocess.call(['cd && pip install pytube'],shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)    
 
      global st,namafile,trg,frmt
      trg =""
      frmt=[]
      try:
            link = input(lr+'['+w+'×'+lr+']'+lg+'Youtube video url: '+w)
            while link == '':
                  print (lr+"   Url don't be blank")
                  link = input(lr+'['+w+'×'+lr+']'+lg+'Youtube video url: '+w)
            namafile= input(lr+'['+w+'×'+lr+']'+lg+'Output file name: '+w).replace(' ','_')
            vm = input(lr+'['+w+'×'+lr+']'+lg+'Output file type '+w+'v'+lg+'(video) or '+w+'m'+lg+'(music): '+w)
            while vm != 'v' and vm !='m':
                  print (lr+'Just v(video) or m(mp3) only')
                  vm = input(lr+'['+w+'×'+lr+']'+lg+'Output file type v(video) or m(music): '+w)
            if vm =='v':
                  frmt=['Video','.mp4']
                  trg=prossv
                  
            else:
                  frmt=['Music','.mp3']
                  trg=prossm
                  
                  
            if namafile =='':
                  namafile = 'SYTD_FILE'
            else:
                  pass
            try:
                  os.mkdir('Results')
            except:
                  pass
            print (lr+'['+w+'×'+lr+']'+lg+'Connecting to the Youtube.com, please wait..')
            '''
            try:
                  
                  os.chdir('/sdcard') && os.mkdir('/sdcard/SYTD/')
                  
            except OSError:
                  pass'''
            try:
                  y= pytube.YouTube(link)
                  st= y.streams.first()
                  '''
                  for itg in strm:
                        print (itg)
                  it_g = input ('pilih : ')
                  st = y.streams.get_by_itag(it_g)'''
                         
            except pytube.exceptions.RegexMatchError:
                  print (lr+'['+w+'×'+lr+']'+lr+'Download failed. Please check your url.'+x)
                  try:
                        ta = input(lr+'   Want to try gain ? (y/n): '+w)
                        if ta == 'y':
                              main()
                        else:
                              bann()
                              menu()                 
                  except KeyboardInterrupt:
                        print (lr+'\nCanceled'+x)
                        exit()

            trd()
      except KeyboardInterrupt:
            print (lr+'\nCanceled'+x)
            exit()
            
    #  except Exception as e:
            print (lr+'['+w+'×'+lr+']',e)
#            print (lr+'['+w+'×'+lr+']'+lr+'Connections error. Please check your connections.\n'+lr+'['+w+'×'+lr+']'+lr+'Exit'+x)
            try:
                  ta = input(lr+'   Want to try gain ? (y/n): '+w)
                  if ta == 'y':
                              main()
                  else:
                              bann()
                              menu()                 
            except KeyboardInterrupt:
                  print (lr+'\nCanceled'+x)
                  exit()
                  
      
def bann():
      x=lr+'''
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
'''
      os.system('clear')
      for i in x:
            print (i,end=''),;time.sleep(0.0003)
      print(lr+'='*55)
      print(lg+'S I M P L E   Y O U T U B E   D O W N L O A D E R'.center(55))
      print(lr+'='*55)
 #     print (w+'K A R J O K  P A N G E S T Y'.center(60))
 #     print ('\nTIPS: Copy the Youtube video url, and paste here.'+x)
      
def menu():
      print (lr+'\n['+w+'1'+lr+']'+lg+' Start')
      print (lr+'['+w+'2'+lr+']'+lg+' About')
      print (lr+'['+w+'3'+lr+']'+lg+' Quick Tutorial')
      print (lr+'['+w+'4'+lr+']'+lg+' Update '+lr+'('+yl+'new'+lr+')')
      print (lr+'['+w+'0'+lr+']'+lg+' Exit\n')
      try:
            ops = input(lr+'SYTD'+w+'/'+lg+'> '+x)
            while ops != '1' and ops !='2' and ops !='3' and ops!='4' and ops != '0' and ops!= '':
                  print(lr+'Option '+ops+' is not in the menu list.'+x)
                  ops = input(lr+'SYTD'+w+'/'+lg+'> '+x)
            if ops == '1':
                        print (lr+'='*55)
                        main()
            elif ops == '2':
                        about()
            elif ops == '3':
                        tutorial()
            elif ops == '4':
                  update()
            elif ops == '0':
                        exit()    
            else:
                        print (lr+'\nBlank input detected !')
                        exit()
            
      except KeyboardInterrupt:
            print (lr+'\nCanceled'+x)
            exit()
def about():
      print (lr+'='*55)
      print(
   lg+'''\nName         :'''+x+''' Simple Youtube Downloader\n'''
   +lg+'''Version      :'''+x+''' 2.5 '''+gr+'''('''+it+'''last updated on
               December 19th, 2018; 2:09PM WIB'''+ix+''')\n'''
   +lg+'''Date         :'''+x+''' December 12th, 2018; 12:17PM WIB\n'''
   +lg+'''Author       :'''+x+''' Karjok Pangesty
               '''+gr+'''('''+it+'''https://t.me/om_karjok'''+ix+''')\n'''
   +lg+'''Team         :'''+x+''' Cracker Noob Squads Indonesia
               '''+gr+'''('''+it+'''https://t.me/CRABS_ID'''+ix+''')\n'''
   +lg+'''Thanks to    :'''+x+''' Allah SWT, my Agustinna Pangesty,
               all member of CRABS, and all who have
               supported and bullying me.
      ''')
      
      print (lr+'='*55)
      input (lr+'Pres enter to back to menu')
      bann()
      menu()
      
def tutorial():
      print (lr+'='*55)
      print(lg+'''
What Is This ?
--------------'''+x+'''
SYTD (Simple Youtube Downloader) is a simple tool\nfor download youtube video and convert it \ninto video or music file.'''+lg+'''
\nHow To Use It ?
---------------'''+x+'''
Copy the link of video wich you want to download.\nIf you use Youtube App,\nopen the video, then tap on share button,\nand select copy to the clipboard.\n
Open SYTD program, and then select number 1\nand press enter.\nPaste link on the form, and press enter.\n
Chose your output file format.\n'v' for video and 'm' for music.\n
Wait for few minutes\nuntil downloading process is done.\n
If downloading is successfullly,\nthe file save in /sdcard directory.
''')
      print (lr+'='*55)
      input(lr+'Press enter to back to menu'+x)
      bann()
      menu()
              
def update():
      print (lr+'='*55)
      print (yl+'\nChecking the connection..')
      try:
            rq = urllib.request.urlopen('https://m.facebook.com')
            print(lg+'Connection OK ✓')
            print (yl+"Updating the program..")
            print (yl+"This may take a few minutes, don't be cancel !\nPlease wait.."+x)
            os.system('cd && rm -rf SYTD')
            subprocess.call(['cd && git clone https://github.com/karjok/SYTD'],shell=True, stdout=subprocess.DEVNULL, stderr = subprocess.STDOUT)
            print (lg+'Restarting the program..')
            time.sleep(0.5)
            os.system('cd ../SYTD && python sytd.py') 
      except urllib.error.URLError:
            print (lr+'Connection error detected !\nSYTD program need an internet connection.\nPlease check it before use this program.')
            input(lr+'Press enter to back to menu')
            bann()
            menu()
                    

def exit():
      print(lr+'If you have any problem or questions with this tool,\nPlease contact the Author at '+it+lg+'https://t.me/om_karjok\n'+ix+lr+'Exit !\n'+x)
      sys.exit()
         
      
      
      
      
      
if __name__=='__main__':
      
      bann()
      menu()
      
