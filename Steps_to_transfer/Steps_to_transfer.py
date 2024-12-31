from flask import Flask, request, send_file
app = Flask(__name__)
@app.route('/downloadfile/<path:filename>', methods=['GET'])
def downloadfile(filename):
    #file_path = '/path/to/file.pdf'
   #return send_from_directory(directory=uploads, filename=filename)
   filename = 'uploads/' + filename
   return send_file(filename, as_attachment=True)

@app.route('/download')
def download():
   import os
   path = "uploads"
   files = os.listdir( path )

   head = '''<!DOCTYPE html>
 <head>
   <title>Flask File Upload/Download</title>
 </head>
 <body>
<center>
<h2>What do you want to download?<h2>'''
   body = ""
   for file in files: body = body + file + '\t=====>>>>>\t' + f'<a href="downloadfile/{file}">' + file + '</a>' + '\n'
   tail = '''<h2>Or to <a href ="http://127.0.0.1:8080">upload</a>?<h2>
</center>
 </body>
</html>'''
   return head+body+tail

@app.route('/')
def hello():
   return '''<!DOCTYPE html>
 <head>
   <title>Flask File Upload/Download</title>
 </head>
 <body>
<center>
<h2>What do you want to upload</a>?<h2>
   <form action="/upload" method="post" enctype="multipart/form-data">
     <input type="file" name="file" />
     <input type="submit" value="Upload" />
   </form>
<h2>Or to <a href ="http://127.0.0.1:8080/download">download</a>?<h2>
</center>
 </body>
</html>'''
@app.route('/upload', methods=['POST'])
def upload():
   if request.method == 'POST':
      file = request.files['file']
      file.save('uploads/' + file.filename)
      return 'File uploaded and saved.\n' # this can use oneline... later

   else: abort(405) # curl -T is put, use curl -X

@app.route('/oneline', methods=['GET'])
def oneline():
   
   return '''https://googledownloads.cn/android/repository/android-ndk-r27c-linux.zip<br>
https://googledownloads.cn/android/repository/commandlinetools-linux-11076708_latest.zip<br>
https://redirector.gvt1.com/edgedl/android/studio/ide-zips/2024.2.1.11/android-studio-2024.2.1.11-linux.tar.gz<br>
<pre>
export ANDROIDSDK="$HOME/Documents/android-sdk-27"
export ANDROIDNDK="$HOME/Documents/android-ndk-r27c"
export ANDROIDAPI="27"  # Target API version of your application
export NDKAPI="27"  # Minimum supported API version of your application
export ANDROIDNDKVER="r27c"  # Version of the NDK you installed

export SDK_DIR="$HOME/Documents"
$SDK_DIR/cmdline-tools/tools/bin/sdkmanager "platforms;android-27"
$SDK_DIR/cmdline-tools/tools/bin/sdkmanager "build-tools;27.0.2"

tar -xvzf filename.tar.gz

https://github.com/mLynn1710/HelloWorld.git

mirrors.cloud.tencent.com/gradle

https://github.com/mLynn1710/HelloWorld.git
wget https://dl.google.com/dl/android/studio/ide-zips/2022.1.1.19/android-studio-2022.1.1.19-linux.tar.gz

</pre>
'''

   
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=8080)