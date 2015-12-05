import numpy as np
import pylab as py
import scipy.signal as ss

data = np.fromfile('./clicks1.raw', dtype='float32')

Fs=1024.

channel1 = []
channel2 = []	#ground
channel3 = []	
channel4 = []	#bipolar
channel5 = []	#thumb
channel6 = []	#trigger

print 'doing montage'

i=0
while i < len(data):
	channel1.append(data[i])
	channel2.append(data[i+1])
	channel3.append(data[i+2])
	channel4.append(data[i+3])
	channel5.append(data[i+4])
	channel6.append(data[i+5])
	i+=6

for i in range(len(channel1)):
	channel1[i]-=channel2[i]
	#channel2[i]-=channel3[i]
	channel3[i]-=channel2[i]
	channel4[i]-=channel2[i]
	channel5[i]-=channel2[i]

print 'montage done'

print "creating filters and filtering data..."
b, a = ss.butter(3, [49.76/(Fs/2.0), 50.25/(Fs/2.0)], 'bandstop')

channel4 = ss.filtfilt(b, a, channel4)
channel1 = ss.filtfilt(b, a, channel1)
channel3 = ss.filtfilt(b, a, channel3)
channel5 = ss.filtfilt(b, a, channel5)

b, a = ss.butter(3, [99.9/(Fs/2.0), 100.1/(Fs/2.0)], 'bandstop')

channel4 = ss.filtfilt(b, a, channel4)
channel1 = ss.filtfilt(b, a, channel1)
channel3 = ss.filtfilt(b, a, channel3)
channel5 = ss.filtfilt(b, a, channel5)

b, a = ss.butter(3, [199.9/(Fs/2.0), 200.1/(Fs/2.0)], 'bandstop')

channel4 = ss.filtfilt(b, a, channel4)
channel1 = ss.filtfilt(b, a, channel1)
channel3 = ss.filtfilt(b, a, channel3)
channel5 = ss.filtfilt(b, a, channel5)

b, a = ss.butter(3, [149.9/(Fs/2.0), 150.1/(Fs/2.0)], 'bandstop')

channel4 = ss.filtfilt(b, a, channel4)
channel1 = ss.filtfilt(b, a, channel1)
channel3 = ss.filtfilt(b, a, channel3)
channel5 = ss.filtfilt(b, a, channel5)

b, a = ss.butter(3, [349.8/(Fs/2.0), 350.2/(Fs/2.0)], 'bandstop')

channel4 = ss.filtfilt(b, a, channel4)
channel1 = ss.filtfilt(b, a, channel1)
channel3 = ss.filtfilt(b, a, channel3)
channel5 = ss.filtfilt(b, a, channel5)

b, a = ss.butter(3, [249.8/(Fs/2.0), 250.2/(Fs/2.0)], 'bandstop')

channel4 = ss.filtfilt(b, a, channel4)
channel1 = ss.filtfilt(b, a, channel1)
channel3 = ss.filtfilt(b, a, channel3)
channel5 = ss.filtfilt(b, a, channel5)

b, a = ss.butter(3, [449.8/(Fs/2.0), 450.2/(Fs/2.0)], 'bandstop')

channel4 = ss.filtfilt(b, a, channel4)
channel1 = ss.filtfilt(b, a, channel1)
channel3 = ss.filtfilt(b, a, channel3)
channel5 = ss.filtfilt(b, a, channel5)

b, a = ss.butter(3, 2./(Fs/2.0), 'highpass')

channel4 = ss.filtfilt(b, a, channel4)
channel1 = ss.filtfilt(b, a, channel1)
channel3 = ss.filtfilt(b, a, channel3)
channel5 = ss.filtfilt(b, a, channel5)

print 'filtering done'

for i in range(0,len(channel1), 10000):
  f = py.figure()
  f.text(.5, .95, "Graph of filtered EMG with trigger 1, page "+str(int(i/10000)+1), horizontalalignment='center')     

  py.subplot(5, 1, 1)
  py.xlim([i,i+10000])
  py.plot(channel6)
  py.subplot(5, 1, 2)
  py.xlim([i,i+10000])
  py.plot(channel5)
  #py.plot(hilbert5)
  py.subplot(5, 1, 3)
  py.xlim([i,i+10000])
  py.ylabel(u'$Tension \\ [\mu V]$')
  py.plot(channel1)
  #py.plot(hilbert1)
  py.subplot(5, 1, 4)
  py.xlim([i,i+10000])
  py.plot(channel3)
  #py.plot(hilbert3)
  py.subplot(5, 1, 5)
  py.xlim([i,i+10000])
  py.plot(channel4)
  #py.plot(hilbert4)
  py.xlabel(u'$Trial \\ number$')
  py.show()

f = py.figure()
f.text(.5, .95, "Graph of filtered EMG with trigger 1", horizontalalignment='center')     

py.subplot(5, 1, 1)
py.plot(channel6)
py.subplot(5, 1, 2)
py.plot(channel5)
py.subplot(5, 1, 3)
py.ylabel(u'$Tension \\ [\mu V]$')
py.plot(channel1)
py.subplot(5, 1, 4)
py.plot(channel3)
py.subplot(5, 1, 5)
py.plot(channel4)
py.xlabel(u'$Trial \\ bumber$')
py.show()

#wyciecie pierszego piku

b, a = ss.butter(3, 10./(Fs/2.0), 'highpass')

channel4 = ss.filtfilt(b, a, channel4)
channel1 = ss.filtfilt(b, a, channel1)
channel3 = ss.filtfilt(b, a, channel3)
channel5 = ss.filtfilt(b, a, channel5)

print 'Welch calculating'

welchfreq5, welchpow5 = ss.welch(channel5, fs=Fs)
welchfreq1, welchpow1 = ss.welch(channel1, fs=Fs)
welchfreq3, welchpow3 = ss.welch(channel3, fs=Fs)
welchfreq4, welchpow4 = ss.welch(channel4, fs=Fs)

print 'Welch calculated'

print 'Calculating RMS and std'

RMS1 = 0.0
for i in range(len(channel1)):
  RMS1 += channel1[i]**2

RMS1 /= len(channel1)
RMS1 = RMS1**0.5

RMS3 = 0.0
for i in range(len(channel3)):
  RMS3 += channel3[i]**2

RMS3 /= len(channel3)
RMS3 = RMS3**0.5

RMS4 = 0.0
for i in range(len(channel4)):
  RMS4 += channel4[i]**2

RMS4 /= len(channel4)
RMS4 = RMS4**0.5

RMS5 = 0.0
for i in range(len(channel5)):
  RMS5 += channel5[i]**2

RMS5 /= len(channel5)
RMS5 = RMS5**0.5

stdrms1=0.0
stdrms3=0.0
stdrms4=0.0
stdrms5=0.0

for i in range(len(channel1)):
  stdrms1+=(RMS1-channel1[i])**2
stdrms1=stdrms1**0.5
stdrms1/=len(channel1)

for i in range(len(channel3)):
  stdrms3+=(RMS3-channel3[i])**2
stdrms3=stdrms3**0.5
stdrms3/=len(channel3)

for i in range(len(channel4)):
  stdrms4+=(RMS4-channel4[i])**2
stdrms4=stdrms4**0.5
stdrms4/=len(channel4)

for i in range(len(channel5)):
  stdrms5+=(RMS5-channel5[i])**2
stdrms5=stdrms5**0.5
stdrms5/=len(channel5)

print 'Mean effective tension channel1: ', RMS1, ' +/- ', stdrms1
print 'Mean effective tension channel3: ', RMS3, ' +/- ', stdrms3
print 'Mean effective tension channel4: ', RMS4, ' +/- ', stdrms4
print 'Mean effective tension channel5: ', RMS5, ' +/- ', stdrms5

print 'clearing signal'

welch5tab=[]
welch1tab=[]
welch3tab=[]
welch4tab=[]

for i in range(len(welchfreq5)):
  if welchpow5[i]>=(RMS5/2):
    welch5tab.append(RMS5/2)
  else:
    welch5tab.append(0.)

for i in range(len(welchfreq1)):
  if welchpow1[i]>=(RMS1):
    welch1tab.append(RMS1)
  else:
    welch1tab.append(0.)

for i in range(len(welchfreq3)):
  if welchpow3[i]>=(RMS3/2):
    welch3tab.append(RMS3/2)
  else:
    welch3tab.append(0.)

for i in range(len(welchfreq4)):
  if welchpow4[i]>=(RMS4/2.5):
    welch4tab.append(RMS4/2.5)
  else:
    welch4tab.append(0.)

print 'signal clear'

f = py.figure()
f.text(.5, .95, 'Power estimated Welchs method', horizontalalignment='center')

py.subplot(4, 1, 1)
py.plot( welchfreq5, welchpow5)
py.plot( welchfreq5, welch5tab)
py.subplot(4, 1, 2)
py.plot( welchfreq1, welchpow1)
py.plot( welchfreq1, welch1tab)
py.ylabel(u'$Power$')
py.subplot(4, 1, 3)
py.plot( welchfreq3, welchpow3)
py.plot( welchfreq3, welch3tab)
py.subplot(4, 1, 4)
py.plot( welchfreq4, welchpow4)
py.plot( welchfreq4, welch4tab)
py.xlabel(u'$Frequencies \\ [Hz]$')

py.show()

print 'Searching strongest power band'

tableft5 = []
tabright5 = []
for i in range(len(welch5tab)):
  if welch5tab[i] != 0 and welch5tab[i-1] == 0:
    tableft5.append(welchfreq5[i])
  if welch5tab[i] == 0 and welch5tab[i-1] != 0:
    tabright5.append(welchfreq5[i-1])

tableft1 = []
tabright1 = []
for i in range(len(welch1tab)):
  if welch1tab[i] != 0 and welch1tab[i-1] == 0:
    tableft1.append(welchfreq1[i])
  if welch1tab[i] == 0 and welch1tab[i-1] != 0:
    tabright1.append(welchfreq1[i-1])

tableft3 = []
tabright3 = []
for i in range(len(welch3tab)):
  if welch3tab[i] != 0 and welch3tab[i-1] == 0:
    tableft3.append(welchfreq3[i])
  if welch3tab[i] == 0 and welch3tab[i-1] != 0:
    tabright3.append(welchfreq3[i-1])

tableft4 = []
tabright4 = []
for i in range(len(welch4tab)):
  if welch4tab[i] != 0 and welch4tab[i-1] == 0:
    tableft4.append(welchfreq4[i])
  if welch4tab[i] == 0 and welch4tab[i-1] != 0:
    tabright4.append(welchfreq4[i-1])

print tableft5, tabright5
print tableft1, tabright1
print tableft3, tabright3
print tableft4, tabright4

print 'Deleting small powers'

for i in range(len(tableft5)):
  b, a = ss.ellip(3,  5, 40, [tableft5[i]/(Fs/2.0), tabright5[i]/(Fs/2.0)], 'bandpass')
  channel5 = ss.filtfilt(b, a, channel5)

for i in range(len(tableft1)):
  if tableft1[i] != tabright1[i]:
    b, a = ss.ellip(3,  5, 40, [tableft1[i]/(Fs/2.0), tabright1[i]/(Fs/2.0)], 'bandpass')
    channel1 = ss.filtfilt(b, a, channel1)

for i in range(len(tableft3)):
  b, a = ss.ellip(3,  5, 50, [tableft3[i]/(Fs/2.0), tabright3[i]/(Fs/2.0)], 'bandpass')
  channel3 = ss.filtfilt(b, a, channel3)

for i in range(len(tableft4)):
  b, a = ss.ellip(3,  5, 40, [tableft4[i]/(Fs/2.0), tabright4[i]/(Fs/2.0)], 'bandpass')
  channel4 = ss.filtfilt(b, a, channel4)

print 'small powers deleted'

print 'Calculating Hilbert transform'

hilbert5 = np.real(np.abs(ss.hilbert(channel5)))
hilbert1 = np.real(np.abs(ss.hilbert(channel1)))
hilbert3 = np.real(np.abs(ss.hilbert(channel3)))
hilbert4 = np.real(np.abs(ss.hilbert(channel4)))

print 'Hilbert transform calculated'

f = py.figure()
f.text(.5, .95, "Graph of filtered EMG with Hilbert ransform with trigger 1", horizontalalignment='center')     

py.subplot(5, 1, 1)
py.plot(channel6)
py.subplot(5, 1, 2)
py.plot(channel5)
py.plot(hilbert5)
py.subplot(5, 1, 3)
py.ylabel(u'$Tension \\ [\mu V]$')
py.plot(channel1)
py.plot(hilbert1)
py.subplot(5, 1, 4)
py.plot(channel3)
py.plot(hilbert3)
py.subplot(5, 1, 5)
py.plot(channel4)
py.plot(hilbert4)
py.xlabel(u'$Trial \\ number$')
py.show()

print 'Signal normalization after Hilbert transform'

normalised_hilbert5 = hilbert5/np.max(hilbert5)
normalised_hilbert1 = hilbert1/np.max(hilbert1)
normalised_hilbert3 = hilbert3/np.max(hilbert3)
normalised_hilbert4 = hilbert4/np.max(hilbert4)

print 'Normalization calculated. Showing'

f = py.figure()
f.text(.5, .95, "Graph of normalized Hilbert transform", horizontalalignment='center')     

py.subplot(4, 1, 1)
py.plot(normalised_hilbert5)
py.subplot(4, 1, 2)
py.plot(normalised_hilbert1)
py.ylabel(u'$Tension \\ [\mu V]$')
py.subplot(4, 1, 3)
py.plot(normalised_hilbert3)
py.subplot(4, 1, 4)
py.plot(normalised_hilbert4)
py.xlabel(u'$Trial \\ number$')
py.show()

print 'Calculation correlation between channels'

nor_cut_hil_5 = normalised_hilbert5[1024:len(normalised_hilbert5)-1024]
nor_cut_hil_1 = normalised_hilbert1[1024:len(normalised_hilbert1)-1024]
nor_cut_hil_3 = normalised_hilbert3[1024:len(normalised_hilbert3)-1024]
nor_cut_hil_4 = normalised_hilbert4[1024:len(normalised_hilbert4)-1024]

tab_cor_5 = []
tab_cor_1 = []
tab_cor_3 = []
tab_cor_4 = []

for i in range(2048):
  tab_cor_1.append(np.correlate(nor_cut_hil_5, normalised_hilbert1[i:len(nor_cut_hil_5)+i]))
  tab_cor_3.append(np.correlate(nor_cut_hil_1, normalised_hilbert3[i:len(nor_cut_hil_1)+i]))
  tab_cor_4.append(np.correlate(nor_cut_hil_3, normalised_hilbert4[i:len(nor_cut_hil_3)+i]))

print 'Correlation calculated'

py.title('Correlation graph')
py.plot(tab_cor_1)
py.plot(tab_cor_3)
py.plot(tab_cor_4)
py.xlabel(u'Location')
py.ylabel(u'Correlation')

#py.plot(np.where(tab_kor_hil5==np.max(tab_kor_hil5))[0][0], np.max(tab_kor_hil5), '*')
py.plot(np.where(tab_cor_1==np.max(tab_cor_1))[0][0], np.max(tab_cor_1), '*')
py.plot(np.where(tab_cor_3==np.max(tab_cor_3))[0][0], np.max(tab_cor_3), '*')
py.plot(np.where(tab_cor_4==np.max(tab_cor_4))[0][0], np.max(tab_cor_4), '*')

#print 1024-np.where(tab_kor_hil5==np.max(tab_kor_hil5))[0][0]
print 1024-np.where(tab_cor_1==np.max(tab_cor_1))[0][0]
print 1024-np.where(tab_cor_3==np.max(tab_cor_3))[0][0]
print 1024-np.where(tab_cor_4==np.max(tab_cor_4))[0][0]

py.show()

print 'Clicks analyze'

tab_polozen_trig = []

for i in range(len(channel6)-1):
  if channel6[i] == 0 and channel6[i+1] > 0:
    tab_polozen_trig.append(i+1)

tab_pol_max_5 = []
tab_pol_max_1 = []
tab_pol_max_3 = []
tab_pol_max_4 = []

for i in tab_polozen_trig:
  #tab_pol_max_5.append(np.where(normalised_hilbert5[i:i+128]==np.max(normalised_hilbert5[i:i+128]))[0][0]+i)
  #tab_pol_max_1.append(np.where(normalised_hilbert1[i:i+128]==np.max(normalised_hilbert1[i:i+128]))[0][0]+i)
  #tab_pol_max_3.append(np.where(normalised_hilbert3[i:i+128]==np.max(normalised_hilbert3[i:i+128]))[0][0]+i)
  #tab_pol_max_4.append(np.where(normalised_hilbert4[i:i+128]==np.max(normalised_hilbert4[i:i+128]))[0][0]+i)

  tab_pol_max_5.append(np.where(hilbert5[i-64:i+128]==np.max(hilbert5[i-64:i+128]))[0][0]+i)
  tab_pol_max_1.append(np.where(hilbert1[i-64:i+128]==np.max(hilbert1[i-64:i+128]))[0][0]+i)
  tab_pol_max_3.append(np.where(hilbert3[i-64:i+128]==np.max(hilbert3[i-64:i+128]))[0][0]+i)
  tab_pol_max_4.append(np.where(hilbert4[i-64:i+128]==np.max(hilbert4[i-64:i+128]))[0][0]+i)

print 'Clicks analyze done'

print 'Calculating time deltas'

delta5 = np.array(tab_pol_max_5) - np.array(tab_polozen_trig)
delta1 = np.array(tab_pol_max_1) - np.array(tab_polozen_trig)
delta3 = np.array(tab_pol_max_3) - np.array(tab_polozen_trig)
delta4 = np.array(tab_pol_max_4) - np.array(tab_polozen_trig)

print 'Delta 1 = ', np.mean(delta5), ' +/- ', np.std(delta5)
print 'Delta 2 = ', np.mean(delta1), ' +/- ', np.std(delta1)
print 'Delta 3 = ', np.mean(delta3), ' +/- ', np.std(delta3)
print 'Delta 4 = ', np.mean(delta4), ' +/- ', np.std(delta4)

#py.plot(tab_polozen_trig, np.ones(len(tab_polozen_trig)), '*')
#py.plot(channel6)
#py.plot(tab_pol_max_5, np.zeros(len(tab_pol_max_5)), 'x')
py.title(u'$Histogram \\ of \\ time \\ diffetences \\ \Delta_{1}t$')
py.hist(delta5)
py.show()
py.title(u'$Histogram\\ of \\ time \\ differences \\ \Delta_{2}t$')
py.hist(delta1)
py.show()
py.title(u'$Histogram \\ of \\ time \\ differences \\ \Delta_{3}t$')
py.hist(delta3)
py.show()
py.title(u'$Histogram \\ of \\ time \\ differences \\ \Delta_{4}t$')
py.hist(delta4)
py.show()

tab_dod_d5 = []
for i in range(len(delta5)):
	if (delta5[i] < np.mean(delta5) + 2*np.std(delta5)) and (delta5[i] > np.mean(delta5) - 2*np.std(delta5)):
		tab_dod_d5.append(delta5[i])

tab_dod_d1 = []
for i in range(len(delta1)):
	if (delta1[i] < np.mean(delta1) + 2*np.std(delta1)) and (delta1[i] > np.mean(delta1) - 2*np.std(delta1)):
		tab_dod_d1.append(delta1[i])

tab_dod_d3 = []
for i in range(len(delta3)):
	if (delta3[i] < np.mean(delta3) + 2*np.std(delta3)) and (delta3[i] > np.mean(delta3) - 2*np.std(delta3)):
		tab_dod_d3.append(delta3[i])

tab_dod_d4 = []
for i in range(len(delta4)):
	if (delta4[i] < np.mean(delta4) + 2*np.std(delta4)) and (delta4[i] > np.mean(delta4) - 2*np.std(delta4)):
		tab_dod_d4.append(delta4[i])

print 'New mean dalta1: ', np.mean(tab_dod_d5), ' +/- ', np.std(tab_dod_d5)
print 'New mean dalta2: ', np.mean(tab_dod_d1), ' +/- ', np.std(tab_dod_d1)
print 'New mean dalta3: ', np.mean(tab_dod_d3), ' +/- ', np.std(tab_dod_d3)
print 'New mean dalta4: ', np.mean(tab_dod_d4), ' +/- ', np.std(tab_dod_d4)
