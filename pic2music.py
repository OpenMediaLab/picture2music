from pyknon.genmidi import Midi
from pyknon.music import NoteSeq
from pyknon.music import Note,Rest
import pic
import random
import sys
import os
import hashlib

imgfile = sys.argv[1]
sizes=50
here =pic.getImgAttr(imgfile) 
random.seed(hashlib.new("md5",here).hexdigest())
sett1=[[11,4,6,7,2],[0,2,4,7,9],[1,3,6,8,10],[2,4,6,7,9],[2,4,7,9,11]]

j=0

notes1=NoteSeq("")
diao=int((pic.getImgLight(imgfile)*5))
for i in here:
	if (j+1)%sizes<sizes:
		if abs(here[j%sizes]-here[(j+1)%sizes])>3:
			if((j%12)%2==0):
				notes1=notes1+Note(value=sett1[diao][random.randint(0,4)], octave=random.randint(diao+2,diao+3),dur=0.08*random.randint(0,4), volume=127)

	#	else :
	#		notes1=notes1+Note(value=1, octave=1,dur=0.01, volume=0)
		
	j+=1

midi = Midi(1, tempo=90,instrument=0)
midi.seq_notes(notes1, track=0)
midi.write(imgfile+".mid")
