import leomusiclib.notetocode as n
#up
def ch1_up(a=str):
   return(a)
def uv1_up(a=str):
   a_step = n.note_to_step(a)
   b_step = a_step

   return((a+0.5)%6)
def um2_up(a=str):
   a_step = n.note_to_step(a)
   b_step = (a_step + 1)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch + 0)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def m2_up(a):
   a_step = n.note_to_step(a)
   b_step = (a_step + 1)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch + 0.5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def b2_up(a):
   a_step = n.note_to_step(a)
   b_step = (a_step + 1)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch + 1)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def uv2_up(a):
   a_step = n.note_to_step(a)
   b_step = (a_step + 1)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch + 1.5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def um3_up(a):
   a_step = n.note_to_step(a)
   b_step = (a_step + 2)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch + 1)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def m3_up(a):
   a_step = n.note_to_step(a)
   b_step = (a_step + 2)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch + 1.5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def b3_up(a):
   a_step = n.note_to_step(a)
   b_step = (a_step + 2)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch + 2)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def uv3_up(a):
   a_step = n.note_to_step(a)
   b_step = (a_step + 2)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch + 2.5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def um4_up(a):
   a_step = n.note_to_step(a)
   b_step = (a_step + 3)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch + 2)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def ch4_up(a):
   a_step = n.note_to_step(a)
   b_step = (a_step + 3)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch + 2.5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def uv4_up(a):
   a_step = n.note_to_step(a)
   b_step = (a_step + 3)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch + 3)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def um5_up(a):
   a_step = n.note_to_step(a)
   b_step = (a_step + 4)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch + 3)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def ch5_up(a):
   a_step = n.note_to_step(a)
   b_step = (a_step + 4)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch + 3.5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def uv5_up(a):
   a_step = n.note_to_step(a)
   b_step = (a_step + 4)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch + 4)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def um6_up(a):
   a_step = n.note_to_step(a)
   b_step = (a_step + 5)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch + 3.5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def m6_up(a):
   a_step = n.note_to_step(a)
   b_step = (a_step + 5)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch + 4)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def b6_up(a):
   a_step = n.note_to_step(a)
   b_step = (a_step + 5)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch + 4.5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def uv6_up(a):
   a_step = n.note_to_step(a)
   b_step = (a_step + 5)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch + 5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def um7_up(a):
   a_step = n.note_to_step(a)
   b_step = (a_step + 6)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch + 4.5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def m7_up(a):
   a_step = n.note_to_step(a)
   b_step = (a_step + 6)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch + 5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def b7_up(a):
   a_step = n.note_to_step(a)
   b_step = (a_step + 6)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch + 5.5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def uv7_up(a):
   a_step = n.note_to_step(a)
   b_step = (a_step + 6)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch + 6)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def um8_up(a):
   a_step = n.note_to_step(a)
   b_step = (a_step + 7)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch + 5.5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def ch8_up(a):
   a_step = n.note_to_step(a)
   b_step = (a_step + 7)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch + 6)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def uv8_up(a):
   a_step = n.note_to_step(a)
   b_step = (a_step + 7)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch + 6.5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)


#down
def ch1_down(a=str):
   return(a)
def uv1_down(a=str):
   a_step = n.note_to_step(a)
   b_step = a_step

   return((a-0.5)%6)
def um2_down(a=str):
   a_step = n.note_to_step(a)
   b_step = (a_step - 1)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch - 0)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def m2_down(a):
   a_step = n.note_to_step(a)
   b_step = (a_step - 1)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch - 0.5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def b2_down(a):
   a_step = n.note_to_step(a)
   b_step = (a_step - 1)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch - 1)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def uv2_down(a):
   a_step = n.note_to_step(a)
   b_step = (a_step - 1)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch - 1.5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def um3_down(a):
   a_step = n.note_to_step(a)
   b_step = (a_step - 2)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch - 1)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def m3_down(a):
   a_step = n.note_to_step(a)
   b_step = (a_step - 2)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch - 1.5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def b3_down(a):
   a_step = n.note_to_step(a)
   b_step = (a_step - 2)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch - 2)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def uv3_down(a):
   a_step = n.note_to_step(a)
   b_step = (a_step - 2)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch - 2.5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def um4_down(a):
   a_step = n.note_to_step(a)
   b_step = (a_step - 3)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch - 2)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def ch4_down(a):
   a_step = n.note_to_step(a)
   b_step = (a_step - 3)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch - 2.5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def uv4_down(a):
   a_step = n.note_to_step(a)
   b_step = (a_step - 3)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch - 3)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def um5_down(a):
   a_step = n.note_to_step(a)
   b_step = (a_step - 4)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch - 3)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def ch5_down(a):
   a_step = n.note_to_step(a)
   b_step = (a_step - 4)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch - 3.5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def uv5_down(a):
   a_step = n.note_to_step(a)
   b_step = (a_step - 4)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch - 4)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def um6_down(a):
   a_step = n.note_to_step(a)
   b_step = (a_step - 5)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch - 3.5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def m6_down(a):
   a_step = n.note_to_step(a)
   b_step = (a_step - 5)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch - 4)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def b6_down(a):
   a_step = n.note_to_step(a)
   b_step = (a_step - 5)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch - 4.5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def uv6_down(a):
   a_step = n.note_to_step(a)
   b_step = (a_step - 5)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch - 5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def um7_down(a):
   a_step = n.note_to_step(a)
   b_step = (a_step - 6)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch - 4.5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def m7_down(a):
   a_step = n.note_to_step(a)
   b_step = (a_step - 6)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch - 5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def b7_down(a):
   a_step = n.note_to_step(a)
   b_step = (a_step - 6)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch - 5.5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def uv7_down(a):
   a_step = n.note_to_step(a)
   b_step = (a_step - 6)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch - 6)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def um8_down(a):
   a_step = n.note_to_step(a)
   b_step = (a_step - 7)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch - 5.5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def ch8_down(a):
   a_step = n.note_to_step(a)
   b_step = (a_step - 7)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch - 6)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)
def uv8_down(a):
   a_step = n.note_to_step(a)
   b_step = (a_step - 7)%7
   a_pitch = n.note_to_pitch(a)
   b_pitch = (a_pitch - 6.5)%6
   b = n.pitch_and_step_to_note(b_pitch,b_step)
   return(b)