# fpsCounterRealTime
Untuk menghitung berapa FPS dari gambar / video yang diambil secara real-time

FPS Realtime ini dibutuhkan pada saat ketika kita ingin mengetahui berapa fps yang ditangkap oleh video secara real-time

FPS Count sebenarnya sudah dapat kita jumpai pada library opencv, dengan coding:

import time
timer = cv2.getTickCount()
fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
cv2.putText and so on..

tapi dibeberapa kondisiku, ini tidak bekerja, makanya saya membuat sendiri FPS Counter
