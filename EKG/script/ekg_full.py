import numpy as np
import pylab as py
import scipy.signal as ss

### constants

Fs = 512.0
ms15=51200/15

### loading signals

print "Loading data..."
resting_signal = np.fromfile('./data/resting_ekg.raw',dtype='float32')
hr_01_signal = np.fromfile('./data/ekg_hr_01.raw',dtype='float32')
hr_02_signal = np.fromfile('./data/ekg_hr_02.raw',dtype='float32')
print "Data loaded."

### making channels

print "Making channels..."
resting_channel1=[]
resting_channel2=[]
resting_channel3=[]
resting_channel4=[]

hr01_channel1=[]
hr01_channel2=[]
hr01_channel3=[]
hr01_channel4=[]

hr02_channel1=[]
hr02_channel2=[]
hr02_channel3=[]
hr02_channel4=[]

print "Channels created."

### Spliting data

print "Spliting data..."
i = 0
while i < len(resting_signal):
	resting_channel1.append(resting_signal[i])
	resting_channel2.append(resting_signal[i+1])
	resting_channel3.append(resting_signal[i+2])
	resting_channel4.append(resting_signal[i+3])
	i+=4

i = 0
while i < len(hr_01_signal):
	hr01_channel1.append(hr_01_signal[i])
	hr01_channel2.append(hr_01_signal[i+1])
	hr01_channel3.append(hr_01_signal[i+2])
	hr01_channel4.append(hr_01_signal[i+3])
	i+=4

i = 0
while i < len(hr_02_signal):
	hr02_channel1.append(hr_02_signal[i])
	hr02_channel2.append(hr_02_signal[i+1])
	hr02_channel3.append(hr_02_signal[i+2])
	hr02_channel4.append(hr_02_signal[i+3])
	i+=4
print "Data splited."

### Einthoven montage

    # resting signal

print "Making resting montage..."
resting_montage1 = [] # left hand - right hand
resting_montage2 = [] # foot - right hand
resting_montage3 = [] # foot - left hand
resting_montage4 = [] # bipolar electrode

for i in range(len(resting_channel1)):
    resting_montage1.append(resting_channel1[i]-resting_channel2[i])
    resting_montage2.append(resting_channel3[i]-resting_channel2[i])
    resting_montage3.append(resting_channel3[i]-resting_channel1[i])
    resting_montage4.append(resting_channel4[i])
print "Resting montage done."

    # HR 1 signal

print "Making hr01 montage..."
montage_hr_01_1 = [] # lewa reka - prawa reka
montage_hr_01_2 = [] # stopa - prawa reka
montage_hr_01_3 = [] # stopa - lewa reka
montage_hr_01_4 = [] # elektroda bipolarna

for i in range(len(hr01_channel1)):
    montage_hr_01_1.append(hr01_channel1[i]-hr01_channel2[i])
    montage_hr_01_2.append(hr01_channel3[i]-hr01_channel2[i])
    montage_hr_01_3.append(hr01_channel3[i]-hr01_channel1[i])
    montage_hr_01_4.append(hr01_channel4[i])
print "hr01 montage done."

    # HR 2 signal

print "Making hr02 montage..."
montage_hr_02_1 = [] # left hand - right hand
montage_hr_02_2 = [] # foot - right hand
montage_hr_02_3 = [] # foot - left hand
montage_hr_02_4 = [] # bipolar electrode

for i in range(len(hr02_channel1)):
    montage_hr_02_1.append(hr02_channel1[i]-hr02_channel2[i])
    montage_hr_02_2.append(hr02_channel3[i]-hr02_channel2[i])
    montage_hr_02_3.append(hr02_channel3[i]-hr02_channel1[i])
    montage_hr_02_4.append(hr02_channel4[i])
print "hr02 montage done."

### highpass filter

print "Making filter..."
b, a = ss.butter(10, 10.0/(Fs/2.0), 'highpass')
print "Filter done."

    # filtering montages with resting EKG

print "Filtering montages with resting EKG..."
resting_montage1 = ss.filtfilt(b, a, resting_montage1)
resting_montage2 = ss.filtfilt(b, a, resting_montage2)
resting_montage3 = ss.filtfilt(b, a, resting_montage3)
resting_montage4 = ss.filtfilt(b, a, resting_montage4)
print "Resting EKG montages filtered."

    # filtering montages with EKG HR 1

print "Filtering montages with hr01..."
montage_hr_01_1 = ss.filtfilt(b, a, montage_hr_01_1)
montage_hr_01_2 = ss.filtfilt(b, a, montage_hr_01_2)
montage_hr_01_3 = ss.filtfilt(b, a, montage_hr_01_3)
montage_hr_01_4 = ss.filtfilt(b, a, montage_hr_01_4)
print "hr01 monteges filtered."

    # filtering montages with z EKG HR 2

print "Filtering montages with hr02..."
montage_hr_02_1 = ss.filtfilt(b, a, montage_hr_02_1)
montage_hr_02_2 = ss.filtfilt(b, a, montage_hr_02_2)
montage_hr_02_3 = ss.filtfilt(b, a, montage_hr_02_3)
montage_hr_02_4 = ss.filtfilt(b, a, montage_hr_02_4)
print "hr02 montages filtered."

### means

    # mean of resting EKG

print "Searching candidats for maximum..."

candidats_max_2x_resting_1=[0]
candidats_max_2y_resting_1=[0]
candidats_max_2x_resting_2=[0]
candidats_max_2y_resting_2=[0]
candidats_max_2x_resting_3=[0]
candidats_max_2y_resting_3=[0]
candidats_max_2x_resting_4=[0]
candidats_max_2y_resting_4=[0]

for i in range(1, len(resting_montage1)-1, 1):
    if(resting_montage1[i-1] < resting_montage1[i] and resting_montage1[i+1] < resting_montage1[i] and resting_montage1[i]>2700):
        if(i-(candidats_max_2x_resting_1[-1])>300):
            candidats_max_2y_resting_1.append(resting_montage1[i])
            candidats_max_2x_resting_1.append(i)
    if(resting_montage2[i-1] < resting_montage2[i] and resting_montage2[i+1] < resting_montage2[i] and resting_montage2[i]>4000):
        if(i-(candidats_max_2x_resting_2[-1])>300):
            candidats_max_2y_resting_2.append(resting_montage2[i])
            candidats_max_2x_resting_2.append(i)
    if(resting_montage3[i-1] < resting_montage3[i] and resting_montage3[i+1] < resting_montage3[i] and resting_montage3[i]>4000):
        if(i-(candidats_max_2x_resting_3[-1])>300):
            candidats_max_2y_resting_3.append(resting_montage3[i])
            candidats_max_2x_resting_3.append(i)
    if(resting_montage4[i-1] < resting_montage4[i] and resting_montage4[i+1] < resting_montage4[i] and resting_montage4[i]>3000):
        if(i-(candidats_max_2x_resting_4[-1])>300):
            candidats_max_2y_resting_4.append(resting_montage4[i])
            candidats_max_2x_resting_4.append(i)

candidats_max_2x_hr_01_1=[0]
candidats_max_2y_hr_01_1=[0]
candidats_max_2x_hr_01_2=[0]
candidats_max_2y_hr_01_2=[0]
candidats_max_2x_hr_01_3=[0]
candidats_max_2y_hr_01_3=[0]
candidats_max_2x_hr_01_4=[0]
candidats_max_2y_hr_01_4=[0]

for i in range(1, len(montage_hr_01_1)-1, 1):
    if(montage_hr_01_1[i-1] < montage_hr_01_1[i] and montage_hr_01_1[i+1] < montage_hr_01_1[i] and montage_hr_01_1[i]>4000):
        if(i-(candidats_max_2x_hr_01_1[-1])>300):
            candidats_max_2y_hr_01_1.append(montage_hr_01_1[i])
            candidats_max_2x_hr_01_1.append(i)
    if(montage_hr_01_2[i-1] < montage_hr_01_2[i] and montage_hr_01_2[i+1] < montage_hr_01_2[i] and montage_hr_01_2[i]>4000):
        if(i-(candidats_max_2x_hr_01_2[-1])>300):
            candidats_max_2y_hr_01_2.append(montage_hr_01_2[i])
            candidats_max_2x_hr_01_2.append(i)
    if(montage_hr_01_3[i-1] < montage_hr_01_3[i] and montage_hr_01_3[i+1] < montage_hr_01_3[i] and montage_hr_01_3[i]>4000):
        if(i-(candidats_max_2x_hr_01_3[-1])>300):
            candidats_max_2y_hr_01_3.append(montage_hr_01_3[i])
            candidats_max_2x_hr_01_3.append(i)
    if(montage_hr_01_4[i-1] < montage_hr_01_4[i] and montage_hr_01_4[i+1] < montage_hr_01_4[i] and montage_hr_01_4[i]>3000):
        if(i-(candidats_max_2x_hr_01_4[-1])>300):
            candidats_max_2y_hr_01_4.append(montage_hr_01_4[i])
            candidats_max_2x_hr_01_4.append(i)

candidats_max_2x_hr_02_1=[0]
candidats_max_2y_hr_02_1=[0]
candidats_max_2x_hr_02_2=[0]
candidats_max_2y_hr_02_2=[0]
candidats_max_2x_hr_02_3=[0]
candidats_max_2y_hr_02_3=[0]
candidats_max_2x_hr_02_4=[0]
candidats_max_2y_hr_02_4=[0]

for i in range(1, len(montage_hr_02_1)-1, 1):
    if(montage_hr_02_1[i-1] < montage_hr_02_1[i] and montage_hr_02_1[i+1] < montage_hr_02_1[i] and montage_hr_02_1[i]>3000):
        if(i-(candidats_max_2x_hr_02_1[-1])>300):
            candidats_max_2y_hr_02_1.append(montage_hr_02_1[i])
            candidats_max_2x_hr_02_1.append(i)
    if(montage_hr_02_2[i-1] < montage_hr_02_2[i] and montage_hr_02_2[i+1] < montage_hr_02_2[i] and montage_hr_02_2[i]>4000):
        if(i-(candidats_max_2x_hr_02_2[-1])>300):
            candidats_max_2y_hr_02_2.append(montage_hr_02_2[i])
            candidats_max_2x_hr_02_2.append(i)
    if(montage_hr_02_3[i-1] < montage_hr_02_3[i] and montage_hr_02_3[i+1] < montage_hr_02_3[i] and montage_hr_02_3[i]>3000):
        if(i-(candidats_max_2x_hr_02_3[-1])>300):
            candidats_max_2y_hr_02_3.append(montage_hr_02_3[i])
            candidats_max_2x_hr_02_3.append(i)
    if(montage_hr_02_4[i-1] < montage_hr_02_4[i] and montage_hr_02_4[i+1] < montage_hr_02_4[i] and montage_hr_02_4[i]>4000):
        if(i-(candidats_max_2x_hr_02_4[-1])>300):
            candidats_max_2y_hr_02_4.append(montage_hr_02_4[i])
            candidats_max_2x_hr_02_4.append(i)


print "Searching for maximum candidats done."


print "Calculating differences with HR..."    

resting_differences_1 = []
resting_differences_2 = []
resting_differences_3 = []
resting_differences_4 = []

hr_differences_01_1 = []
hr_differences_01_2 = []
hr_differences_01_3 = []
hr_differences_01_4 = []

hr_differences_02_1 = []
hr_differences_02_2 = []
hr_differences_02_3 = []
hr_differences_02_4 = []

for i in range(0,len(candidats_max_2x_resting_1)-1):
    resting_differences_1.append((candidats_max_2x_resting_1[i+1]-candidats_max_2x_resting_1[i])/512.)
for i in range(0,len(candidats_max_2x_resting_2)-1):
    resting_differences_2.append((candidats_max_2x_resting_2[i+1]-candidats_max_2x_resting_2[i])/512.)
for i in range(0,len(candidats_max_2x_resting_3)-1):    
    resting_differences_3.append((candidats_max_2x_resting_3[i+1]-candidats_max_2x_resting_3[i])/512.)
for i in range(0,len(candidats_max_2x_resting_1)-1):    
    resting_differences_4.append((candidats_max_2x_resting_4[i+1]-candidats_max_2x_resting_4[i])/512.)

for i in range(0,len(candidats_max_2x_hr_01_1)-1):
    hr_differences_01_1.append((candidats_max_2x_hr_01_1[i+1]-candidats_max_2x_hr_01_1[i])/512.)
for i in range(0,len(candidats_max_2x_hr_01_2)-1):
    hr_differences_01_2.append((candidats_max_2x_hr_01_2[i+1]-candidats_max_2x_hr_01_2[i])/512.)
for i in range(0,len(candidats_max_2x_hr_01_3)-1):
    hr_differences_01_3.append((candidats_max_2x_hr_01_3[i+1]-candidats_max_2x_hr_01_3[i])/512.)
for i in range(0,len(candidats_max_2x_hr_01_4)-1):
    hr_differences_01_4.append((candidats_max_2x_hr_01_4[i+1]-candidats_max_2x_hr_01_4[i])/512.)

for i in range(0,len(candidats_max_2x_hr_02_1)-1):
    hr_differences_02_1.append((candidats_max_2x_hr_02_1[i+1]-candidats_max_2x_hr_02_1[i])/512.)
for i in range(0,len(candidats_max_2x_hr_02_2)-1):    
    hr_differences_02_2.append((candidats_max_2x_hr_02_2[i+1]-candidats_max_2x_hr_02_2[i])/512.)
for i in range(0,len(candidats_max_2x_hr_02_3)-1):
    hr_differences_02_3.append((candidats_max_2x_hr_02_3[i+1]-candidats_max_2x_hr_02_3[i])/512.)
for i in range(0,len(candidats_max_2x_hr_02_4)-1):
    hr_differences_02_4.append((candidats_max_2x_hr_02_4[i+1]-candidats_max_2x_hr_02_4[i])/512.)

print "Differences calculations done."

### plotting graphs with differences
print "Plotting graphs with differences in time..."
py.subplot(4, 1, 1)
py.title("Graph with HR in time, resting EKG")
py.ylabel("HR montage 1")
py.plot(resting_differences_1)
py.ylim([np.min(resting_differences_1),np.max(resting_differences_1)])
py.xlim([0,len(resting_differences_1)-1])

py.subplot(4, 1, 2)
py.ylabel("HR montage 2")
py.plot(resting_differences_2)
py.ylim([np.min(resting_differences_2),np.max(resting_differences_2)])
py.xlim([0,len(resting_differences_2)-1])

py.subplot(4, 1, 3)
py.ylabel("HR montage 3")
py.plot(resting_differences_3)
py.ylim([np.min(resting_differences_3),np.max(resting_differences_3)])
py.xlim([0,len(resting_differences_3)-1])

py.subplot(4, 1, 4)
py.ylabel("HR montage 4")
py.plot(resting_differences_4)
py.ylim([np.min(resting_differences_4),np.max(resting_differences_4)])
py.xlim([0,len(resting_differences_4)-1])
py.xlabel("Time [s]")
py.show()



py.subplot(4, 1, 1)
py.title("Graph with HR in time, training EKG 1")
py.ylabel("HR montage 1")
py.plot(hr_differences_01_1)
py.ylim([np.min(hr_differences_01_1),np.max(hr_differences_01_1)])
py.xlim([0,len(hr_differences_01_1)-1])

py.subplot(4, 1, 2)
py.ylabel("HR montage 2")
py.plot(hr_differences_01_2)
py.ylim([np.min(hr_differences_01_2),np.max(hr_differences_01_2)])
py.xlim([0,len(hr_differences_01_2)-1])

py.subplot(4, 1, 3)
py.ylabel("HR montage 3")
py.plot(hr_differences_01_3)
py.ylim([np.min(hr_differences_01_3),np.max(hr_differences_01_3)])
py.xlim([0,len(hr_differences_01_3)-1])

py.subplot(4, 1, 4)
py.ylabel("HR montage 4")
py.plot(hr_differences_01_4)
py.ylim([np.min(hr_differences_01_4),np.max(hr_differences_01_4)])
py.xlim([0,len(hr_differences_01_4)-1])
py.xlabel("Time [s]")
py.show()



py.subplot(4, 1, 1)
py.title("Graph with HR in time, training EKG 2")
py.ylabel("HR montage 1")
py.plot(hr_differences_02_1)
py.ylim([np.min(hr_differences_02_1),np.max(hr_differences_02_1)])
py.xlim([0,len(hr_differences_02_1)-1])

py.subplot(4, 1, 2)
py.ylabel("HR montage 2")
py.plot(hr_differences_02_2)
py.ylim([np.min(hr_differences_02_2),np.max(hr_differences_02_2)])
py.xlim([0,len(hr_differences_02_2)-1])

py.subplot(4, 1, 3)
py.ylabel("HR montage 3")
py.plot(hr_differences_02_3)
py.ylim([np.min(hr_differences_02_3),np.max(hr_differences_02_3)])
py.xlim([0,len(hr_differences_02_3)-1])

py.subplot(4, 1, 4)
py.ylabel("HR montage 4")
py.plot(hr_differences_02_4)
py.ylim([np.min(hr_differences_02_4),np.max(hr_differences_02_4)])
py.xlim([0,len(hr_differences_02_4)-1])
py.xlabel("Time[x]")
py.show()
print "Plotting graphs with differences done."


### Plotting signals in every montage

print "Plotting signals in every montage..."

    # resting EKG

for i in range(0,len(resting_montage1), 20000):
    f = py.figure()
    f.text(.5, .95, "Resting EKG, montage 1, page "+str(int(i/20000.)+1), horizontalalignment='center')     
    for j in range(4):
        py.subplot(4,1,j+1)
        py.plot(resting_montage1)
        py.plot(candidats_max_2x_resting_1, candidats_max_2y_resting_1, '*')
        py.xlim([i+(j*5000),i+(j*5000)+5000])
        py.ylim([-7000,7900])
    py.show()

for i in range(0,len(resting_montage2), 20000):
    f = py.figure()
    f.text(.5, .95, "Resting EKG, montage 2, page "+str(int(i/20000.)+1), horizontalalignment='center')     
    for j in range(4):
        py.subplot(4,1,j+1)
        py.plot(resting_montage2)
        py.plot(candidats_max_2x_resting_2, candidats_max_2y_resting_2, '*')
        py.xlim([i+(j*5000),i+(j*5000)+5000])
        py.ylim([-7000,9000])
    py.show()

for i in range(0,len(resting_montage3), 20000):
    f = py.figure()
    f.text(.5, .95, "Resting EKG, montage 3, page "+str(int(i/20000.)+1), horizontalalignment='center')     
    for j in range(4):
        py.subplot(4,1,j+1)
        py.plot(resting_montage3)
        py.plot(candidats_max_2x_resting_3, candidats_max_2y_resting_3, '*')
        py.xlim([i+(j*5000),i+(j*5000)+5000])
        py.ylim([-7000,9500])
    py.show()

for i in range(0,len(resting_montage4), 20000):
    f = py.figure()
    f.text(.5, .95, "Resting EKG, montage 4, page "+str(int(i/20000.)+1), horizontalalignment='center')     
    for j in range(4):
        py.subplot(4,1,j+1)
        py.plot(resting_montage4)        
        py.plot(candidats_max_2x_resting_4, candidats_max_2y_resting_4, '*')
        py.xlim([i+(j*5000),i+(j*5000)+5000])
        py.ylim([-7000,7900])
    py.show()

    # EKG HR 1

for i in range(0,len(montage_hr_01_1), 20000):
    f = py.figure()
    f.text(.5, .95, "Training EKG 1, montage 1, page "+str(int(i/20000.)+1), horizontalalignment='center')     
    for j in range(4):
        py.subplot(4,1,j+1)
        py.plot(montage_hr_01_1)        
        py.plot(candidats_max_2x_hr_01_1, candidats_max_2y_hr_01_1, '*')
        py.xlim([i+(j*5000),i+(j*5000)+5000])
        py.ylim([-7000,8500])
    py.show()

for i in range(0,len(montage_hr_01_2), 20000):
    f = py.figure()
    f.text(.5, .95, "Training EKG 1, montage 2, page "+str(int(i/20000.)+1), horizontalalignment='center')     
    for j in range(4):
        py.subplot(4,1,j+1)
        py.plot(montage_hr_01_2)
        py.plot(candidats_max_2x_hr_01_2, candidats_max_2y_hr_01_2, '*')
        py.xlim([i+(j*5000),i+(j*5000)+5000])
        py.ylim([-7000,9500])
    py.show()

for i in range(0,len(montage_hr_01_3), 20000):
    f = py.figure()
    f.text(.5, .95, "Wykres EKG pobudzanego 1, montaz 3, strona "+str(int(i/20000.)+1), horizontalalignment='center')     
    for j in range(4):
        py.subplot(4,1,j+1)
        py.plot(montage_hr_01_3)
        py.plot(candidats_max_2x_hr_01_3, candidats_max_2y_hr_01_3, '*')
        py.xlim([i+(j*5000),i+(j*5000)+5000])
        py.ylim([-7000,9500])
    py.show()

for i in range(0,len(montage_hr_01_4), 20000):
    f = py.figure()
    f.text(.5, .95, "Training EKG 1, montage 4, page "+str(int(i/20000.)+1), horizontalalignment='center')     
    for j in range(4):
        py.subplot(4,1,j+1)
        py.plot(montage_hr_01_4)        
        py.plot(candidats_max_2x_hr_01_4, candidats_max_2y_hr_01_4, '*')
        py.xlim([i+(j*5000),i+(j*5000)+5000])
        py.ylim([-7000,7900])
    py.show()

    # EKG HR 2

for i in range(0,len(montage_hr_02_1), 20000):
    f = py.figure()
    f.text(.5, .95, "Training EKG 2, montage 1, page "+str(int(i/20000.)+1), horizontalalignment='center')     
    for j in range(4):
        py.subplot(4,1,j+1)
        py.plot(montage_hr_02_1)
        py.plot(candidats_max_2x_hr_02_1, candidats_max_2y_hr_02_1, '*')
        py.xlim([i+(j*5000),i+(j*5000)+5000])
        py.ylim([-7000,7900])
    py.show()

for i in range(0,len(montage_hr_02_2), 20000):
    f = py.figure()
    f.text(.5, .95, "Training EKG 2, montage 2, page "+str(int(i/20000.)+1), horizontalalignment='center')     
    for j in range(4):
        py.subplot(4,1,j+1)
        py.plot(montage_hr_02_2)
        py.plot(candidats_max_2x_hr_02_2, candidats_max_2y_hr_02_2, '*')
        py.xlim([i+(j*5000),i+(j*5000)+5000])
        py.ylim([-7000,10000])
    py.show()

for i in range(0,len(montage_hr_02_3), 20000):
    f = py.figure()
    f.text(.5, .95, "Training EKG 2, montage 3, page "+str(int(i/20000.)+1), horizontalalignment='center')     
    for j in range(4):
        py.subplot(4,1,j+1)
        py.plot(montage_hr_02_3)
        py.plot(candidats_max_2x_hr_02_3, candidats_max_2y_hr_02_3, '*')
        py.xlim([i+(j*5000),i+(j*5000)+5000])
        py.ylim([-7000,10500])
    py.show()

for i in range(0,len(montage_hr_02_4), 20000):
    f = py.figure()
    f.text(.5, .95, "Training EKG 2, montage 4, page "+str(int(i/20000.)+1), horizontalalignment='center')     
    for j in range(4):
        py.subplot(4,1,j+1)
        py.plot(montage_hr_02_4)
        py.plot(candidats_max_2x_hr_02_4, candidats_max_2y_hr_02_4, '*')
        py.xlim([i+(j*5000),i+(j*5000)+5000])
        py.ylim([-7000,7900])
    py.show()

print "Calculating HR in particular areas..."
print "Mean resting HR - whole, montage 1", np.mean(resting_differences_1), "+/-", np.std(resting_differences_1)
print "Mean resting HR - whole, montage 2", np.mean(resting_differences_2), "+/-", np.std(resting_differences_2)
print "Mean resting HR - whole, montage 3", np.mean(resting_differences_3), "+/-", np.std(resting_differences_3)
print "Mean resting HR - whole, montage 4", np.mean(resting_differences_4), "+/-", np.std(resting_differences_4)

print "Mean resting HR - without laugh, montage 1", np.mean(resting_differences_1[0:140]+resting_differences_1[150:]), "+/-", np.std(resting_differences_1[0:140]+resting_differences_1[150:])
print "Mean resting HR - without laugh, montage 2", np.mean(resting_differences_2[0:140]+resting_differences_2[150:]), "+/-", np.std(resting_differences_2[0:140]+resting_differences_2[150:])
print "Mean resting HR - without laugh, montage 3", np.mean(resting_differences_3[0:140]+resting_differences_3[150:]), "+/-", np.std(resting_differences_3[0:140]+resting_differences_3[150:])
print "Mean resting HR - without laugh, montage 4", np.mean(resting_differences_4[0:140]+resting_differences_4[150:]), "+/-", np.std(resting_differences_4[0:140]+resting_differences_4[150:])

print "Mean resting HR - with laugh, montage 1", np.mean(resting_differences_1[140:150]), "+/-", np.std(resting_differences_1[140:150])
print "Mean resting HR - with laugh, montage 2", np.mean(resting_differences_2[140:150]), "+/-", np.std(resting_differences_2[140:150])
print "Mean resting HR - with laugh, montage 3", np.mean(resting_differences_3[140:150]), "+/-", np.std(resting_differences_3[140:150])
print "Mean resting HR - with laugh, montage 4", np.mean(resting_differences_4[140:150]), "+/-", np.std(resting_differences_4[140:150])

print "Mean training HR 1 - resting segment, montage 1", np.mean(hr_differences_01_1[0:30]+hr_differences_01_1[45:]), "+/-", np.std(hr_differences_01_1[0:30]+hr_differences_01_1[45:])
print "Mean training HR 1 - resting segment, montage 2", np.mean(hr_differences_01_2[0:30]+hr_differences_01_2[45:]), "+/-", np.std(hr_differences_01_2[0:30]+hr_differences_01_2[45:])
print "Mean training HR 1 - resting segment, montage 3", np.mean(hr_differences_01_3[0:30]+hr_differences_01_3[45:]), "+/-", np.std(hr_differences_01_3[0:30]+hr_differences_01_3[45:])
print "Mean training HR 1 - resting segment, montage 4", np.mean(hr_differences_01_4[0:30]+hr_differences_01_4[45:]), "+/-", np.std(hr_differences_01_4[0:30]+hr_differences_01_4[45:])

print "Mean training HR 1 - training segment, montage 1", np.mean(hr_differences_01_1[30:45]), "+/-", np.std(hr_differences_01_1[30:45])
print "Mean training HR 1 - training segment, montage 2", np.mean(hr_differences_01_2[30:45]), "+/-", np.std(hr_differences_01_2[30:45])
print "Mean training HR 1 - training segment, montage 3", np.mean(hr_differences_01_3[30:45]), "+/-", np.std(hr_differences_01_3[30:45])
print "Mean training HR 1 - training segment, montage 4", np.mean(hr_differences_01_4[30:45]), "+/-", np.std(hr_differences_01_4[30:45])

print "Mean training HR 2 - resting segment, montage 1", np.mean(hr_differences_02_1[0:40]+hr_differences_02_1[80:140]+hr_differences_02_1[180:280]+hr_differences_02_1[320:]), "+/-", np.std(hr_differences_02_1[0:30]+hr_differences_02_1[60:120]+hr_differences_02_1[160:230]+hr_differences_02_1[280:])
print "Mean training HR 2 - resting segment, montage 2", np.mean(hr_differences_02_2[0:40]+hr_differences_02_2[80:140]+hr_differences_02_2[180:280]+hr_differences_02_2[320:]), "+/-", np.std(hr_differences_02_2[0:30]+hr_differences_02_2[60:120]+hr_differences_02_2[160:230]+hr_differences_02_2[280:])
print "Mean training HR 2 - resting segment, montage 3", np.mean(hr_differences_02_3[0:40]+hr_differences_02_3[80:140]+hr_differences_02_3[180:280]+hr_differences_02_3[320:]), "+/-", np.std(hr_differences_02_3[0:30]+hr_differences_02_3[60:120]+hr_differences_02_3[160:230]+hr_differences_02_3[280:])
print "Mean training HR 2 - resting segment, montage 4", np.mean(hr_differences_02_4[0:40]+hr_differences_02_4[80:140]+hr_differences_02_4[180:280]+hr_differences_02_4[320:]), "+/-", np.std(hr_differences_02_4[0:30]+hr_differences_02_4[60:120]+hr_differences_02_4[160:230]+hr_differences_02_4[280:])

print "Mean training HR 2 - training segment 1, montage 1", np.mean(hr_differences_02_1[40:80]), "+/-", np.std(hr_differences_02_1[40:80])
print "Mean training HR 2 - training segment 1, montage 2", np.mean(hr_differences_02_2[40:80]), "+/-", np.std(hr_differences_02_2[40:80])
print "Mean training HR 2 - training segment 1, montage 3", np.mean(hr_differences_02_3[40:80]), "+/-", np.std(hr_differences_02_3[40:80])
print "Mean training HR 2 - training segment 1, montage 4", np.mean(hr_differences_02_4[40:80]), "+/-", np.std(hr_differences_02_4[40:80])

print "Mean training HR 2 - training segment 2, montage 1", np.mean(hr_differences_02_1[140:180]), "+/-", np.std(hr_differences_02_1[140:180])
print "Mean training HR 2 - training segment 2, montage 2", np.mean(hr_differences_02_2[140:180]), "+/-", np.std(hr_differences_02_2[140:180])
print "Mean training HR 2 - training segment 2, montage 3", np.mean(hr_differences_02_3[140:180]), "+/-", np.std(hr_differences_02_3[140:180])
print "Mean training HR 2 - training segment 2, montage 4", np.mean(hr_differences_02_4[140:180]), "+/-", np.std(hr_differences_02_4[140:180])

print "Mean training HR 2 - training segment 3, montage 1", np.mean(hr_differences_02_1[280:320]), "+/-", np.std(hr_differences_02_1[280:320])
print "Mean training HR 2 - training segment 3, montage 2", np.mean(hr_differences_02_2[280:320]), "+/-", np.std(hr_differences_02_2[280:320])
print "Mean training HR 2 - training segment 3, montage 3", np.mean(hr_differences_02_3[280:320]), "+/-", np.std(hr_differences_02_3[280:320])
print "Mean training HR 2 - training segment 3, montage 4", np.mean(hr_differences_02_4[283:320]), "+/-", np.std(hr_differences_02_4[280:320])

print "Calculating HR done."

print "All done."
