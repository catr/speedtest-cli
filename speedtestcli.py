{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "IndexError",
     "evalue": "list index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-17c43703bec2>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     10\u001b[0m \u001b[0mupload\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mre\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfindall\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Upload:\\s(.*?)\\s'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mre\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mMULTILINE\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     11\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 12\u001b[1;33m \u001b[0mping\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mping\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mreplace\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m','\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'.'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     13\u001b[0m \u001b[0mdownload\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdownload\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mreplace\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m','\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'.'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     14\u001b[0m \u001b[0mupload\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mupload\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mreplace\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m','\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'.'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mIndexError\u001b[0m: list index out of range"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import re\n",
    "import subprocess\n",
    "import time\n",
    "\n",
    "response = subprocess.Popen('/usr/local/bin/speedtest-cli --simple', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')\n",
    "\n",
    "ping = re.findall('Ping:\\s(.*?)\\s', response, re.MULTILINE)\n",
    "download = re.findall('Download:\\s(.*?)\\s', response, re.MULTILINE)\n",
    "upload = re.findall('Upload:\\s(.*?)\\s', response, re.MULTILINE)\n",
    "\n",
    "ping = ping[0].replace(',', '.')\n",
    "download = download[0].replace(',', '.')\n",
    "upload = upload[0].replace(',', '.')\n",
    "\n",
    "try:\n",
    "    f = open('/home/cayo/speedtest/speedtestcli.csv', 'a+')\n",
    "    if os.stat('/home/cayo/speedtest/speedtestcli.csv').st_size == 0:\n",
    "            f.write('Date,Time,Ping (ms),Download (Mbit/s),Upload (Mbit/s)\\r\\n')\n",
    "except:\n",
    "    pass\n",
    "\n",
    "f.write('{},{},{},{},{}\\r\\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), ping, download, upload))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
