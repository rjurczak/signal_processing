import numpy as np
import pylab as py
import scipy.signal as ss

print 'Mounting'

ud = np.fromfile('./data/up_down/up_down.raw', dtype='float32') # up-down
du = np.fromfile('./data/down_up/down_up.raw', dtype='float32') # down_up
lr = np.fromfile('./data/left_right/left_right.raw', dtype='float32') # left_right
rl = np.fromfile('./data/right_left/right_left.raw', dtype='float32') # right_left
rm = np.fromfile('./data/random_movements/random_movements.raw', dtype='float32') # random movements


Fs = 128.0

RM_RVER = [] # random movements, right, vertical
RM_RHOR = [] # random movements, right, horizontal
RM_LVER = [] # random movements, left, vertical
RM_LHOR = [] # random movements, left, horizontal

UD_RVER = [] # up-down, right, vertical
UD_RHOR = []
UD_LVER = []
UD_LHOR = []

DU_RVER = [] # down-up, right, vertical
DU_RHOR = []
DU_LVER = []
DU_LHOR = []

LR_RVER = [] # left-right, right, vertical
LR_RHOR = []
LR_LVER = []
LR_LHOR = []

RL_RVER = [] # right-left, right, vertical
RL_RHOR = []
RL_LVER = []
RL_LHOR = []

i=0
while i < len(ud):
	RM_RVER.append(rm[i])
	RM_RHOR.append(rm[i+1])
	RM_LVER.append(rm[i+2])
	RM_LHOR.append(rm[i+3])
	i+=4

i=0
while i < len(ud):
	UD_RVER.append(ud[i])
	UD_RHOR.append(ud[i+1])
	UD_LVER.append(ud[i+2])
	UD_LHOR.append(ud[i+3])
	i+=4

i=0
while i < len(du):
	DU_RVER.append(du[i])
	DU_RHOR.append(du[i+1])
	DU_LVER.append(du[i+2])
	DU_LHOR.append(du[i+3])
	i+=4

i=0
while i < len(lr):
	LR_RVER.append(lr[i])
	LR_RHOR.append(lr[i+1])
	LR_LVER.append(lr[i+2])
	LR_LHOR.append(lr[i+3])
	i+=4

i=0
while i < len(rl):
	RL_RVER.append(rl[i])
	RL_RHOR.append(rl[i+1])
	RL_LVER.append(rl[i+2])
	RL_LHOR.append(rl[i+3])
	i+=4

print 'Mounting done'

print "Filtering..."

b, a = ss.butter(3, [0.1/(Fs/2.0), 10.0/(Fs/2.0)], 'bandpass')

#b, a = ss.butter(3, 20./(Fs/2.0), 'lowpass')
RM_RVER = ss.filtfilt(b, a, RM_RVER)
RM_RHOR = ss.filtfilt(b, a, RM_RHOR)
RM_LVER = ss.filtfilt(b, a, RM_LVER)
RM_LHOR = ss.filtfilt(b, a, RM_LHOR)

UD_RVER = ss.filtfilt(b, a, UD_RVER)
UD_RHOR = ss.filtfilt(b, a, UD_RHOR)
UD_LVER = ss.filtfilt(b, a, UD_LVER)
UD_LHOR = ss.filtfilt(b, a, UD_LHOR)

DU_RVER = ss.filtfilt(b, a, DU_RVER)
DU_RHOR = ss.filtfilt(b, a, DU_RHOR)
DU_LVER = ss.filtfilt(b, a, DU_LVER)
DU_LHOR = ss.filtfilt(b, a, DU_LHOR)

LR_RVER = ss.filtfilt(b, a, LR_RVER)
LR_RHOR = ss.filtfilt(b, a, LR_RHOR)
LR_LVER = ss.filtfilt(b, a, LR_LVER)
LR_LHOR = ss.filtfilt(b, a, LR_LHOR)

RL_RVER = ss.filtfilt(b, a, RL_RVER)
RL_RHOR = ss.filtfilt(b, a, RL_RHOR)
RL_LVER = ss.filtfilt(b, a, RL_LVER)
RL_LHOR = ss.filtfilt(b, a, RL_LHOR)

print 'Filtering done'


axes = py.figure()
axes.text(.52, .02, u"$Trial$", horizontalalignment='center', fontsize=12)
axes.text(.01, .52, u"$Tension \\ [\mu V]$", verticalalignment='center', fontsize=12, rotation=90)
py.suptitle('     EOG graph, random movements', fontsize=13)
py.subplot(4, 1, 1)
py.title('Left eye, vertical', fontsize=11)
py.xlim([0,len(RM_RVER)])
py.plot(RM_RVER)
py.subplot(4, 1, 2)
py.title('Right eye, horizontal', fontsize=11)
py.xlim([0,len(RM_RHOR)])
py.plot(RM_RHOR)
py.subplot(4, 1, 3)
py.title('Left eye, vertical', fontsize=11)
py.xlim([0,len(RM_LVER)])
py.plot(RM_LVER)
py.subplot(4, 1, 4)
py.title('Left eye, horizontal', fontsize=11)
py.xlim([0,len(RM_LHOR)])
py.plot(RM_LHOR)
py.tight_layout(pad=1.6, w_pad=0.1, h_pad=0.1)
py.show()

axes = py.figure()
axes.text(.52, .02, u"$Trial$", horizontalalignment='center', fontsize=12)
axes.text(.01, .52, u"$Tension \\ [\mu V]$", verticalalignment='center', fontsize=12, rotation=90)
py.suptitle('        EOG graph, up-down', fontsize=13)
py.subplot(4, 1, 1)
py.title('Right eye, vertical', fontsize=11)
py.xlim([0,len(UD_RVER)])
py.plot(UD_RVER)
py.subplot(4, 1, 2)
py.title('Right eye, horizontal', fontsize=11)
py.xlim([0,len(UD_RHOR)])
py.plot(UD_RHOR)
py.subplot(4, 1, 3)
py.title('Left eye, vertical', fontsize=11)
py.xlim([0,len(UD_LVER)])
py.plot(UD_LVER)
py.subplot(4, 1, 4)
py.title('Left eye, horizontal', fontsize=11)
py.xlim([0,len(UD_LHOR)])
py.plot(UD_LHOR)
py.tight_layout(pad=1.6, w_pad=0.1, h_pad=0.1)
py.show()

axes = py.figure()
axes.text(.52, .02, u"$Trial$", horizontalalignment='center', fontsize=12)
axes.text(.01, .52, u"$Tension [\mu V]$", verticalalignment='center', fontsize=12, rotation=90)
py.suptitle('        EOG graph, down-up', fontsize=13)
py.subplot(4, 1, 1)
py.title('Right eye, vertical', fontsize=11)
py.xlim([0,len(DU_RVER)])
py.plot(DU_RVER)
py.subplot(4, 1, 2)
py.title('Right eye, horizontal', fontsize=11)
py.xlim([0,len(DU_RHOR)])
py.plot(DU_RHOR)
py.subplot(4, 1, 3)
py.title('Left eye, vertical', fontsize=11)
py.xlim([0,len(DU_LVER)])
py.plot(DU_LVER)
py.subplot(4, 1, 4)
py.title('Left eye, horizontal', fontsize=11)
py.xlim([0,len(DU_LHOR)])
py.plot(DU_LHOR)
py.tight_layout(pad=1.6, w_pad=0.1, h_pad=0.1)
py.show()

axes = py.figure()
axes.text(.52, .02, u"$Trial$", horizontalalignment='center', fontsize=12)
axes.text(.01, .52, u"$Tension [\mu V]$", verticalalignment='center', fontsize=12, rotation=90)
py.suptitle('        EOG graph, left-right', fontsize=13)
py.subplot(4, 1, 1)
py.title('Right eye, vertical', fontsize=11)
py.xlim([0,len(LR_RVER)])
py.plot(LR_RVER)
py.subplot(4, 1, 2)
py.title('Right eye, horizontal', fontsize=11)
py.xlim([0,len(LR_RHOR)])
py.plot(LR_RHOR)
py.subplot(4, 1, 3)
py.title('Left eye, vertical', fontsize=11)
py.xlim([0,len(LR_LVER)])
py.plot(LR_LVER)
py.subplot(4, 1, 4)
py.title('Left eye, horizontal', fontsize=11)
py.xlim([0,len(LR_LHOR)])
py.plot(LR_LHOR)
py.tight_layout(pad=1.6, w_pad=0.1, h_pad=0.1)
py.show()

axes = py.figure()
axes.text(.52, .02, u"$Trial$", horizontalalignment='center', fontsize=12)
axes.text(.01, .52, u"$Tension [\mu V]$", verticalalignment='center', fontsize=12, rotation=90)
py.suptitle('        EOG graph, right-left', fontsize=13)
py.subplot(4, 1, 1)
py.title('Right eye, vertical', fontsize=11)
py.xlim([0,len(RL_RVER)])
py.plot(RL_RVER)
py.subplot(4, 1, 2)
py.title('Right eye, horizontal', fontsize=11)
py.xlim([0,len(RL_RHOR)])
py.plot(RL_RHOR)
py.subplot(4, 1, 3)
py.title('Left eye, vertical', fontsize=11)
py.xlim([0,len(RL_LVER)])
py.plot(RL_LVER)
py.subplot(4, 1, 4)
py.title('Left eye, horizontal', fontsize=11)
py.xlim([0,len(RL_LHOR)])
py.plot(RL_LHOR)
py.tight_layout(pad=1.6, w_pad=0.1, h_pad=0.1)
py.show()

print 'Calculating correlation and means'

UD_1 = UD_RVER[128:256]
UD_2 = UD_RHOR[128:256]
UD_3 = UD_LVER[128:256]
UD_4 = UD_LHOR[128:256]

DU_1 = DU_RVER[128:256]
DU_2 = DU_RHOR[128:256]
DU_3 = DU_LVER[128:256]
DU_4 = DU_LHOR[128:256]

LR_1 = LR_RVER[128:256]
LR_2 = LR_RHOR[128:256]
LR_3 = LR_LVER[128:256]
LR_4 = LR_LHOR[128:256]

RL_1 = RL_RVER[128:256]
RL_2 = RL_RHOR[128:256]
RL_3 = RL_LVER[128:256]
RL_4 = RL_LHOR[128:256]
'''
UD_CORR_1 = []
UD_CORR_2 = []
UD_CORR_3 = []
UD_CORR_4 = []

DU_CORR_1 = []
DU_CORR_2 = []
DU_CORR_3 = []
DU_CORR_4 = []

LR_CORR_1 = []
LR_CORR_2 = []
LR_CORR_3 = []
LR_CORR_4 = []

RL_CORR_1 = []
RL_CORR_2 = []
RL_CORR_3 = []
RL_CORR_4 = []

for i in range((len(ud)/4)-len(UD_1)):
	UD_CORR_1.append(np.correlate(UD_1, UD_RVER[i:i+len(UD_1)]))
	UD_CORR_2.append(np.correlate(UD_2, UD_RHOR[i:i+len(UD_2)]))
	UD_CORR_3.append(np.correlate(UD_3, UD_LVER[i:i+len(UD_3)]))
	UD_CORR_4.append(np.correlate(UD_4, UD_LHOR[i:i+len(UD_4)]))

for i in range((len(du)/4)-len(DU_1)):
	DU_CORR_1.append(np.correlate(DU_1, DU_RVER[i:i+len(DU_1)]))
	DU_CORR_2.append(np.correlate(DU_2, DU_RHOR[i:i+len(DU_2)]))
	DU_CORR_3.append(np.correlate(DU_3, DU_LVER[i:i+len(DU_3)]))
	DU_CORR_4.append(np.correlate(DU_4, DU_LHOR[i:i+len(DU_4)]))

for i in range((len(lr)/4)-len(LR_1)):
	LR_CORR_1.append(np.correlate(LR_1, LR_RVER[i:i+len(LR_1)]))
	LR_CORR_2.append(np.correlate(LR_2, LR_RHOR[i:i+len(LR_2)]))
	LR_CORR_3.append(np.correlate(LR_3, LR_LVER[i:i+len(LR_3)]))
	LR_CORR_4.append(np.correlate(LR_4, LR_LHOR[i:i+len(LR_4)]))

for i in range((len(rl)/4)-len(RL_1)):
	RL_CORR_1.append(np.correlate(RL_1, RL_RVER[i:i+len(RL_1)]))
	RL_CORR_2.append(np.correlate(RL_2, RL_RHOR[i:i+len(RL_2)]))
	RL_CORR_3.append(np.correlate(RL_3, RL_LVER[i:i+len(RL_3)]))
	RL_CORR_4.append(np.correlate(RL_4, RL_LHOR[i:i+len(RL_4)]))

for i in range(60, len(DU_CORR_1)-60):
	DU_CORR_1[i] = np.mean(DU_CORR_1[i-60:i+60])
	DU_CORR_2[i] = np.mean(DU_CORR_2[i-60:i+60])
	DU_CORR_3[i] = np.mean(DU_CORR_3[i-60:i+60])
	DU_CORR_4[i] = np.mean(DU_CORR_4[i-60:i+60])

for i in range(60, len(UD_CORR_1)-60):
	UD_CORR_1[i] = np.mean(UD_CORR_1[i-60:i+60])
	UD_CORR_2[i] = np.mean(UD_CORR_2[i-60:i+60])
	UD_CORR_3[i] = np.mean(UD_CORR_3[i-60:i+60])
	UD_CORR_4[i] = np.mean(UD_CORR_4[i-60:i+60])

for i in range(60, len(LR_CORR_1)-60):
	LR_CORR_1[i] = np.mean(LR_CORR_1[i-60:i+60])
	LR_CORR_2[i] = np.mean(LR_CORR_2[i-60:i+60])
	LR_CORR_3[i] = np.mean(LR_CORR_3[i-60:i+60])
	LR_CORR_4[i] = np.mean(LR_CORR_4[i-60:i+60])

for i in range(60, len(RL_CORR_1)-60):
	RL_CORR_1[i] = np.mean(RL_CORR_1[i-60:i+60])
	RL_CORR_2[i] = np.mean(RL_CORR_2[i-60:i+60])
	RL_CORR_3[i] = np.mean(RL_CORR_3[i-60:i+60])
	RL_CORR_4[i] = np.mean(RL_CORR_4[i-60:i+60])

UD_CORR_1 /= max([max(UD_CORR_1), max(UD_CORR_2), max(UD_CORR_3), max(UD_CORR_4)])
UD_CORR_2 /= max([max(UD_CORR_1), max(UD_CORR_2), max(UD_CORR_3), max(UD_CORR_4)])
UD_CORR_3 /= max([max(UD_CORR_1), max(UD_CORR_2), max(UD_CORR_3), max(UD_CORR_4)])
UD_CORR_4 /= max([max(UD_CORR_1), max(UD_CORR_2), max(UD_CORR_3), max(UD_CORR_4)])

DU_CORR_1 /= max([max(DU_CORR_1), max(DU_CORR_2), max(DU_CORR_3), max(DU_CORR_4)])
DU_CORR_2 /= max([max(DU_CORR_1), max(DU_CORR_2), max(DU_CORR_3), max(DU_CORR_4)])
DU_CORR_3 /= max([max(DU_CORR_1), max(DU_CORR_2), max(DU_CORR_3), max(DU_CORR_4)])
DU_CORR_4 /= max([max(DU_CORR_1), max(DU_CORR_2), max(DU_CORR_3), max(DU_CORR_4)])

LR_CORR_1 /= max([max(LR_CORR_1), max(LR_CORR_2), max(LR_CORR_3), max(LR_CORR_4)])
LR_CORR_2 /= max([max(LR_CORR_1), max(LR_CORR_2), max(LR_CORR_3), max(LR_CORR_4)])
LR_CORR_3 /= max([max(LR_CORR_1), max(LR_CORR_2), max(LR_CORR_3), max(LR_CORR_4)])
LR_CORR_4 /= max([max(LR_CORR_1), max(LR_CORR_2), max(LR_CORR_3), max(LR_CORR_4)])

RL_CORR_1 /= max([max(RL_CORR_1), max(RL_CORR_2), max(RL_CORR_3), max(RL_CORR_4)])
RL_CORR_2 /= max([max(RL_CORR_1), max(RL_CORR_2), max(RL_CORR_3), max(RL_CORR_4)])
RL_CORR_3 /= max([max(RL_CORR_1), max(RL_CORR_2), max(RL_CORR_3), max(RL_CORR_4)])
RL_CORR_4 /= max([max(RL_CORR_1), max(RL_CORR_2), max(RL_CORR_3), max(RL_CORR_4)])
'''
'''
print 'Up-down:'
print 'Right y: ', np.mean(UD_CORR_1), '+/-', np.std(UD_CORR_1)
print 'Right x: ', np.mean(UD_CORR_2), '+/-', np.std(UD_CORR_2)
print 'Left  y: ', np.mean(UD_CORR_3), '+/-', np.std(UD_CORR_3)
print 'Left  x: ', np.mean(UD_CORR_4), '+/-', np.std(UD_CORR_4)

print 'Down-up:'
print 'Right y: ', np.mean(DU_CORR_1), '+/-', np.std(DU_CORR_1)
print 'Right x: ', np.mean(DU_CORR_2), '+/-', np.std(DU_CORR_2)
print 'Left  y: ', np.mean(DU_CORR_3), '+/-', np.std(DU_CORR_3)
print 'Left  x: ', np.mean(DU_CORR_4), '+/-', np.std(DU_CORR_4)

print 'Left-right:'
print 'Right y: ', np.mean(LR_CORR_1), '+/-', np.std(LR_CORR_1)
print 'Right x: ', np.mean(LR_CORR_2), '+/-', np.std(LR_CORR_2)
print 'Left  y: ', np.mean(LR_CORR_3), '+/-', np.std(LR_CORR_3)
print 'Left  x: ', np.mean(LR_CORR_4), '+/-', np.std(LR_CORR_4)

print 'Right-left:'
print 'Right y: ', np.mean(RL_CORR_1), '+/-', np.std(RL_CORR_1)
print 'Right x: ', np.mean(RL_CORR_2), '+/-', np.std(RL_CORR_2)
print 'Left  y: ', np.mean(RL_CORR_3), '+/-', np.std(RL_CORR_3)
print 'Left  x: ', np.mean(RL_CORR_4), '+/-', np.std(RL_CORR_4)
'''
'''

print 'Calculating correlation and means done'

print 'Correlation graphs'

axes = py.figure()
axes.text(.52, .02, u"$Trial$", horizontalalignment='center', fontsize=12)
axes.text(.01, .52, u"$Correlation$", verticalalignment='center', fontsize=12, rotation=90)
py.suptitle('Normalized correlation up-down', fontsize=13)
py.subplot(4, 1, 1)
py.title('Right eye, vertical', fontsize=11)
py.xlim([0,len(UD_CORR_1)])
l1, = py.plot(UD_CORR_1)
py.subplot(4, 1, 2)
py.title('Right eye, horizontal', fontsize=11)
py.xlim([0,len(UD_CORR_2)])
l2, = py.plot(UD_CORR_2)
py.subplot(4, 1, 3)
py.title('Left eye, vertical', fontsize=11)
py.xlim([0,len(UD_CORR_3)])
l3, = py.plot(UD_CORR_3)
py.subplot(4, 1, 4)
py.title('Left eye, vertical', fontsize=11)
py.xlim([0,len(UD_CORR_4)])
l4, = py.plot(UD_CORR_4)
py.tight_layout(pad=1.6, w_pad=0.1, h_pad=0.1)
py.show()

axes = py.figure()
axes.text(.52, .02, u"$Trial$", horizontalalignment='center', fontsize=12)
axes.text(.01, .52, u"$Normalized correlation$", verticalalignment='center', fontsize=12, rotation=90)
py.suptitle('Normalized correlation down-up', fontsize=13)
py.subplot(4, 1, 1)
py.title('Right eye, vertical', fontsize=11)
py.xlim([0,len(DU_CORR_1)])
l1, = py.plot(DU_CORR_1)
py.subplot(4, 1, 2)
py.title('Right eye, horizontal', fontsize=11)
py.xlim([0,len(DU_CORR_2)])
l2, = py.plot(DU_CORR_2)
py.subplot(4, 1, 3)
py.title('Left eye, vertical', fontsize=11)
py.xlim([0,len(DU_CORR_3)])
l3, = py.plot(DU_CORR_3)
py.subplot(4, 1, 4)
py.title('Left eye, vertical', fontsize=11)
py.xlim([0,len(DU_CORR_4)])
l4, = py.plot(DU_CORR_4)
py.tight_layout(pad=1.6, w_pad=0.1, h_pad=0.1)
py.show()

axes = py.figure()
axes.text(.52, .02, u"$Trial$", horizontalalignment='center', fontsize=12)
axes.text(.01, .52, u"$Correlation$", verticalalignment='center', fontsize=12, rotation=90)
py.suptitle('Normalized correlation left-right', fontsize=13)
py.subplot(4, 1, 1)
py.title('Right eye, vertical', fontsize=11)
py.xlim([0,len(LR_CORR_1)])
l1, = py.plot(LR_CORR_1)
py.subplot(4, 1, 2)
py.title('Right eye, horizontal', fontsize=11)
py.xlim([0,len(LR_CORR_2)])
l2, = py.plot(LR_CORR_2)
py.subplot(4, 1, 3)
py.title('Left eye, vertical', fontsize=11)
py.xlim([0,len(LR_CORR_3)])
l3, = py.plot(LR_CORR_3)
py.subplot(4, 1, 4)
py.title('Left eye, vertical', fontsize=11)
py.xlim([0,len(LR_CORR_4)])
l4, = py.plot(LR_CORR_4)
py.tight_layout(pad=1.6, w_pad=0.1, h_pad=0.1)
py.show()

axes = py.figure()
axes.text(.52, .02, u"$Trial$", horizontalalignment='center', fontsize=12)
axes.text(.01, .52, u"$Correlation$", verticalalignment='center', fontsize=12, rotation=90)
py.suptitle('Normalized correlation right-left', fontsize=13)
py.subplot(4, 1, 1)
py.title('Right eye, vertical', fontsize=11)
py.xlim([0,len(RL_CORR_1)])
l1, = py.plot(RL_CORR_1)
py.subplot(4, 1, 2)
py.title('Right eye, horizontal', fontsize=11)
py.xlim([0,len(RL_CORR_2)])
l2, = py.plot(RL_CORR_2)
py.subplot(4, 1, 3)
py.title('Left eye, vertical', fontsize=11)
py.xlim([0,len(RL_CORR_3)])
l3, = py.plot(RL_CORR_3)
py.subplot(4, 1, 4)
py.title('Left eye, vertical', fontsize=11)
py.xlim([0,len(RL_CORR_4)])
l4, = py.plot(RL_CORR_4)
py.tight_layout(pad=1.6, w_pad=0.1, h_pad=0.1)
py.show()

axes = py.figure()
axes.text(.52, .02, u"$Trial$", horizontalalignment='center', fontsize=12)
axes.text(.01, .52, u"$Correlation$", verticalalignment='center', fontsize=12, rotation=90)
py.title('Normalized correlation up-down', fontsize=13)
l1, = py.plot(UD_CORR_1)
l2, = py.plot(UD_CORR_2)
l3, = py.plot(UD_CORR_3)
l4, = py.plot(UD_CORR_4)
py.xlim([0,len(UD_CORR_1)])
py.legend([l1, l2, l3, l4], ['Up', 'Right', 'Down', 'Left'], loc=4)
py.show()

axes = py.figure()
axes.text(.52, .02, u"$Trial$", horizontalalignment='center', fontsize=12)
axes.text(.01, .52, u"$Correlation$", verticalalignment='center', fontsize=12, rotation=90)
py.title('Normalized correlation down-up', fontsize=13)
l1, = py.plot(DU_CORR_1)
l2, = py.plot(DU_CORR_2)
l3, = py.plot(DU_CORR_3)
l4, = py.plot(DU_CORR_4)
py.xlim([0,len(DU_CORR_1)])
py.legend([l1, l2, l3, l4], ['Up', 'Right', 'Down', 'Left'], loc=4)
py.show()

axes = py.figure()
axes.text(.52, .02, u"$Trial$", horizontalalignment='center', fontsize=12)
axes.text(.01, .52, u"$Correlation$", verticalalignment='center', fontsize=12, rotation=90)
py.title('Normalized correlation left-right', fontsize=13)
l1, = py.plot(LR_CORR_1)
l2, = py.plot(LR_CORR_2)
l3, = py.plot(LR_CORR_3)
l4, = py.plot(LR_CORR_4)
py.xlim([0,len(LR_CORR_1)])
py.legend([l1, l2, l3, l4], ['Up', 'Right', 'Down', 'Left'], loc=4)
py.show()

axes = py.figure()
axes.text(.52, .02, u"$Trial$", horizontalalignment='center', fontsize=12)
axes.text(.01, .52, u"$Correlation$", verticalalignment='center', fontsize=12, rotation=90)
py.title('Normalized correlation right-left', fontsize=13)
l1, = py.plot(RL_CORR_1)
l2, = py.plot(RL_CORR_2)
l3, = py.plot(RL_CORR_3)
l4, = py.plot(RL_CORR_4)
py.xlim([0,len(RL_CORR_1)])
py.legend([l1, l2, l3, l4], ['Up', 'Right', 'Down', 'Left'], loc=4)
py.show()

'''
print 'Calculating correlationa and means of random eye movement'

RM_CORR_1_UD = []
RM_CORR_2_UD = []
RM_CORR_3_UD = []
RM_CORR_4_UD = []

RM_CORR_1_DU = []
RM_CORR_2_DU = []
RM_CORR_3_DU = []
RM_CORR_4_DU = []

RM_CORR_1_LR = []
RM_CORR_2_LR = []
RM_CORR_3_LR = []
RM_CORR_4_LR = []

RM_CORR_1_RL = []
RM_CORR_2_RL = []
RM_CORR_3_RL = []
RM_CORR_4_RL = []

for i in range((len(RM_RVER)/4)-len(UD_1)-100):
	RM_CORR_1_UD.append(np.correlate(UD_1, RM_RVER[i:i+len(UD_1)]))
	RM_CORR_2_UD.append(np.correlate(UD_2, RM_RHOR[i:i+len(UD_2)]))
	RM_CORR_3_UD.append(np.correlate(UD_3, RM_LVER[i:i+len(UD_3)]))
	RM_CORR_4_UD.append(np.correlate(UD_4, RM_LHOR[i:i+len(UD_4)]))

for i in range((len(RM_RVER)/4)-len(DU_1)):
	RM_CORR_1_DU.append(np.correlate(DU_1, RM_RVER[i:i+len(DU_1)]))
	RM_CORR_2_DU.append(np.correlate(DU_2, RM_RHOR[i:i+len(DU_2)]))
	RM_CORR_3_DU.append(np.correlate(DU_3, RM_LVER[i:i+len(DU_3)]))
	RM_CORR_4_DU.append(np.correlate(DU_4, RM_LHOR[i:i+len(DU_4)]))

for i in range((len(RM_RVER)/4)-len(LR_1)):
	RM_CORR_1_LR.append(np.correlate(LR_1, RM_RVER[i:i+len(LR_1)]))
	RM_CORR_2_LR.append(np.correlate(LR_2, RM_RHOR[i:i+len(LR_2)]))
	RM_CORR_3_LR.append(np.correlate(LR_3, RM_LVER[i:i+len(LR_3)]))
	RM_CORR_4_LR.append(np.correlate(LR_4, RM_LHOR[i:i+len(LR_4)]))

for i in range((len(RM_RVER)/4)-len(RL_1)):
	RM_CORR_1_RL.append(np.correlate(RL_1, RM_RVER[i:i+len(RL_1)]))
	RM_CORR_2_RL.append(np.correlate(RL_2, RM_RHOR[i:i+len(RL_2)]))
	RM_CORR_3_RL.append(np.correlate(RL_3, RM_LVER[i:i+len(RL_3)]))
	RM_CORR_4_RL.append(np.correlate(RL_4, RM_LHOR[i:i+len(RL_4)]))

for i in range(60, 2688):
	RM_CORR_1_UD[i] = np.mean(RM_CORR_1_UD[i-60:i+60])
	RM_CORR_2_UD[i] = np.mean(RM_CORR_2_UD[i-60:i+60])
	RM_CORR_3_UD[i] = np.mean(RM_CORR_3_UD[i-60:i+60])
	RM_CORR_4_UD[i] = np.mean(RM_CORR_4_UD[i-60:i+60])

for i in range(60, 2688):
	RM_CORR_1_DU[i] = np.mean(RM_CORR_1_DU[i-60:i+60])
	RM_CORR_2_DU[i] = np.mean(RM_CORR_2_DU[i-60:i+60])
	RM_CORR_3_DU[i] = np.mean(RM_CORR_3_DU[i-60:i+60])
	RM_CORR_4_DU[i] = np.mean(RM_CORR_4_DU[i-60:i+60])

for i in range(60, 2688):
	RM_CORR_1_LR[i] = np.mean(RM_CORR_1_LR[i-60:i+60])
	RM_CORR_2_LR[i] = np.mean(RM_CORR_2_LR[i-60:i+60])
	RM_CORR_3_LR[i] = np.mean(RM_CORR_3_LR[i-60:i+60])
	RM_CORR_4_LR[i] = np.mean(RM_CORR_4_LR[i-60:i+60])

for i in range(60, 2688):
	RM_CORR_1_RL[i] = np.mean(RM_CORR_1_RL[i-60:i+60])
	RM_CORR_2_RL[i] = np.mean(RM_CORR_2_RL[i-60:i+60])
	RM_CORR_3_RL[i] = np.mean(RM_CORR_3_RL[i-60:i+60])
	RM_CORR_4_RL[i] = np.mean(RM_CORR_4_RL[i-60:i+60])

#print len(RM_CORR_1_UD), len(RM_CORR_1_UD[0])
#print RM_CORR_1_UD[0]
#print max([max(RM_CORR_1_UD), max(RM_CORR_2_UD), max(RM_CORR_3_UD), max(RM_CORR_4_UD)])
RM_CORR_1_UD /= max([max(RM_CORR_1_UD), max(RM_CORR_2_UD), max(RM_CORR_3_UD), max(RM_CORR_4_UD)])
RM_CORR_2_UD /= max([max(RM_CORR_1_UD), max(RM_CORR_2_UD), max(RM_CORR_3_UD), max(RM_CORR_4_UD)])
RM_CORR_3_UD /= max([max(RM_CORR_1_UD), max(RM_CORR_2_UD), max(RM_CORR_3_UD), max(RM_CORR_4_UD)])
RM_CORR_4_UD /= max([max(RM_CORR_1_UD), max(RM_CORR_2_UD), max(RM_CORR_3_UD), max(RM_CORR_4_UD)])

RM_CORR_1_DU /= max([max(RM_CORR_1_DU), max(RM_CORR_2_DU), max(RM_CORR_3_DU), max(RM_CORR_4_DU)])
RM_CORR_2_DU /= max([max(RM_CORR_1_DU), max(RM_CORR_2_DU), max(RM_CORR_3_DU), max(RM_CORR_4_DU)])
RM_CORR_3_DU /= max([max(RM_CORR_1_DU), max(RM_CORR_2_DU), max(RM_CORR_3_DU), max(RM_CORR_4_DU)])
RM_CORR_4_DU /= max([max(RM_CORR_1_DU), max(RM_CORR_2_DU), max(RM_CORR_3_DU), max(RM_CORR_4_DU)])

RM_CORR_1_LR /= max([max(RM_CORR_1_LR), max(RM_CORR_2_LR), max(RM_CORR_3_LR), max(RM_CORR_4_LR)])
RM_CORR_2_LR /= max([max(RM_CORR_1_LR), max(RM_CORR_2_LR), max(RM_CORR_3_LR), max(RM_CORR_4_LR)])
RM_CORR_3_LR /= max([max(RM_CORR_1_LR), max(RM_CORR_2_LR), max(RM_CORR_3_LR), max(RM_CORR_4_LR)])
RM_CORR_4_LR /= max([max(RM_CORR_1_LR), max(RM_CORR_2_LR), max(RM_CORR_3_LR), max(RM_CORR_4_LR)])

RM_CORR_1_RL /= max([max(RM_CORR_1_RL), max(RM_CORR_2_RL), max(RM_CORR_3_RL), max(RM_CORR_4_RL)])
RM_CORR_2_RL /= max([max(RM_CORR_1_RL), max(RM_CORR_2_RL), max(RM_CORR_3_RL), max(RM_CORR_4_RL)])
RM_CORR_3_RL /= max([max(RM_CORR_1_RL), max(RM_CORR_2_RL), max(RM_CORR_3_RL), max(RM_CORR_4_RL)])
RM_CORR_4_RL /= max([max(RM_CORR_1_RL), max(RM_CORR_2_RL), max(RM_CORR_3_RL), max(RM_CORR_4_RL)])

print 'Calculating correlationa and means of random eye movement done'

axes = py.figure()
axes.text(.52, .02, u"$Trial$", horizontalalignment='center', fontsize=12)
axes.text(.01, .52, u"$Correlation$", verticalalignment='center', fontsize=12, rotation=90)
py.suptitle('Normalized correlation graph of random movements', fontsize=13)

py.subplot(4, 1, 1)
py.title('Right eye, vertical', fontsize=11)
l1, = py.plot(RM_CORR_1_UD)
l2, = py.plot(RM_CORR_1_DU)
#l3, = py.plot(RM_CORR_1_LR)
#l4, = py.plot(RM_CORR_1_RL)
py.xlim([0,len(RM_CORR_1_UD)])
py.legend([l1, l2], ['Down', 'Up'], loc=4)

py.subplot(4, 1, 2)
py.title('Right eye, horizontal', fontsize=11)
#l1, = py.plot(RM_CORR_2_UD)
#l2, = py.plot(RM_CORR_2_DU)
l3, = py.plot(RM_CORR_2_LR)
l4, = py.plot(RM_CORR_2_RL)
py.xlim([0,len(RM_CORR_2_UD)])
py.legend([l3, l4], ['Right', 'Left'], loc=4)

py.subplot(4, 1, 3)
py.title('Left eye, vertical', fontsize=11)
l1, = py.plot(RM_CORR_3_UD)
l2, = py.plot(RM_CORR_3_DU)
#l3, = py.plot(RM_CORR_3_LR)
#l4, = py.plot(RM_CORR_3_RL)
py.xlim([0,len(RM_CORR_3_UD)])
py.legend([l1, l2], ['Up', 'Down'], loc=4)

py.subplot(4, 1, 4)
py.title('Left eye, horizontal', fontsize=11)
#l1, = py.plot(RM_CORR_4_UD)
#l2, = py.plot(RM_CORR_4_DU)
l3, = py.plot(RM_CORR_4_LR)
l4, = py.plot(RM_CORR_4_RL)
py.xlim([0,len(RM_CORR_4_UD)])
py.legend([l3, l4], ['Right', 'Left'], loc=4)

py.tight_layout(pad=1.6, w_pad=0.1, h_pad=0.1)
py.show()

print 'All done'
