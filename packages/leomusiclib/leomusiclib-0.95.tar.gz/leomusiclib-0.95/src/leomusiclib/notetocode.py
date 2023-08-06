# -*- coding: cp1251 -*-
def note_to_pitch(note=str):
    if note == 'dobb' or note == '��bb' or note == 'Ceses':
        return(5)
    if note == 'dob' or note == '��b' or note == 'Ces':
        return(5.5)
    if note == 'do' or note == '��' or note == 'C':
        return(0)
    if note == 'do#' or note == '��#' or note == 'Cis':
        return(0.5)
    if note == 'do##' or note == '��##' or note == 'Cisis':
        return(1)
    if note == 'rebb' or note == '��bb' or note == 'Deses':
        return(0)
    if note == 'reb' or note == '��b' or note == 'Des':
        return(0.5)
    if note == 're' or note == '��' or note == 'D':
        return(1)
    if note == 're#' or note == '��#' or note == 'Dis':
        return(1.5)
    if note == 're##' or note == '��##' or note == 'Disis':
        return(2)
    if note == 'mibb' or note == '��bb' or note == 'Eses':
        return(1)
    if note == 'mib' or note == '��b' or note == 'Es':
        return(1.5)
    if note == 'mi' or note == '��' or note == 'E':
        return(2)
    if note == 'mi#' or note == '��#' or note == 'Eis':
        return(2.5)
    if note == 'mi##' or note == '��##' or note == 'Eisis':
        return(0.5)
    if note == 'fabb' or note == '��bb' or note == 'Feses':
        return(1.5)
    if note == 'fab' or note == '��b' or note == 'Fes':
        return(2)
    if note == 'fa' or note == '��' or note == 'F':
        return(2.5)
    if note == 'fa#' or note == '��#' or note == 'Fis':
        return(3)
    if note == 'fa##' or note == '��##' or note == 'Fisis':
        return(3.5)
    if note == 'solbb' or note == '����bb' or note == 'Geses':
        return(2.5)
    if note == 'solb' or note == '����b' or note == 'Ges':
        return(3)
    if note == 'sol' or note == 'c���' or note == 'G':
        return(3.5)
    if note == 'sol#' or note == '����#' or note == 'Gis':
        return(4)
    if note == 'sol##' or note == '����##' or note == 'Gisis':
        return(4.5)
    if note == 'labb' or note == '��bb' or note == 'Ases':
        return(3.5)
    if note == 'lab' or note == '��b' or note == 'As':
        return(4)
    if note == 'la' or note == '��' or note == 'A':
        return(4.5)
    if note == 'la#' or note == '��#' or note == 'Ais':
        return(5)
    if note == 'la##' or note == '��##' or note == 'Aisis':
        return(5.5)
    if note == 'sibb' or note == '��bb' or note == 'Heses':
        return(4.5)
    if note == 'sib' or note == '��b' or note == 'B' or note == 'Hes':
        return(5)
    if note == 'si' or note == 'c�' or note == 'H':
        return(5.5)
    if note == 'si#' or note == 'c�#' or note == 'His':
        return(6)
    if note == 'si##' or note == '��##' or note == 'Hisis':
        return(6.5)
    else:
        return('������')
def note_to_step(note=str):
    if note == 'dobb' or note == '��bb' or note == 'Ceses':
        return(1)
    if note == 'dob' or note == '��b' or note == 'Ces':
        return(1)
    if note == 'do' or note == '��' or note == 'C':
        return(1)
    if note == 'do#' or note == '��#' or note == 'Cis':
        return(1)
    if note == 'do##' or note == '��##' or note == 'Cisis':
        return(1)
    if note == 'rebb' or note == '��bb' or note == 'Deses':
        return(2)
    if note == 'reb' or note == '��b' or note == 'Des':
        return(2)
    if note == 're' or note == '��' or note == 'D':
        return(2)
    if note == 're#' or note == '��#' or note == 'Dis':
        return(2)
    if note == 're##' or note == '��##' or note == 'Disis':
        return(2)
    if note == 'mibb' or note == '��bb' or note == 'Eses':
        return(3)
    if note == 'mib' or note == '��b' or note == 'Es':
        return(3)
    if note == 'mi' or note == '��' or note == 'E':
        return(3)
    if note == 'mi#' or note == '��#' or note == 'Eis':
        return(3)
    if note == 'mi##' or note == '��##' or note == 'Eisis':
        return(3)
    if note == 'fabb' or note == '��bb' or note == 'Feses':
        return(4)
    if note == 'fab' or note == '��b' or note == 'Fes':
        return(4)
    if note == 'fa' or note == '��' or note == 'F':
        return(4)
    if note == 'fa#' or note == '��#' or note == 'Fis':
        return(4)
    if note == 'fa##' or note == '��##' or note == 'Fisis':
        return(4)
    if note == 'solbb' or note == '����bb' or note == 'Geses':
        return(5)
    if note == 'solb' or note == '����b' or note == 'Ges':
        return(5)
    if note == 'sol' or note == 'c���' or note == 'G':
        return(5)
    if note == 'sol#' or note == '����#' or note == 'Gis':
        return(5)
    if note == 'sol##' or note == '����##' or note == 'Gisis':
        return(5)
    if note == 'labb' or note == '��bb' or note == 'Ases':
        return(6)
    if note == 'lab' or note == '��b' or note == 'As':
        return(6)
    if note == 'la' or note == '��' or note == 'A':
        return(6)
    if note == 'la#' or note == '��#' or note == 'Ais':
        return(6)
    if note == 'la##' or note == '��##' or note == 'Aisis':
        return(6)
    if note == 'sibb' or note == '��bb' or note == 'Heses':
        return(7)
    if note == 'sib' or note == '��b' or note == 'B':
        return(7)
    if note == 'si' or note == 'c�' or note == 'H':
        return(7)
    if note == 'si#' or note == 'c�#' or note == 'H#':
        return(7)
    if note == 'si##' or note == '��##' or note == 'Hisis':
        return(7)
    else:
        return('������')
def renamer(word,example):
    if example == 'do' or example == 1 or example == 'en':
      if word == 'dobb' or word == '��bb' or word == 'Ceses':
          return('dobb')
      if word == 'dob' or word == '��b' or word == 'Ces':
          return('dob')
      if word == 'do' or word == '��' or word == 'C':
          return('do')
      if word == 'do#' or word == '��#' or word == 'Cis':
          return('do#')
      if word == 'do##' or word == '��##' or word == 'Cisis':
          return('do##')
      if word == 'rebb' or word == '��bb' or word == 'Deses':
          return('rebb')
      if word == 'reb' or word == '��b' or word == 'Des':
          return('reb')
      if word == 're' or word == '��' or word == 'D':
          return('re')
      if word == 're#' or word == '��#' or word == 'Dis':
          return('re#')
      if word == 're##' or word == '��##' or word == 'Disis':
          return('re##')
      if word == 'mibb' or word == '��bb' or word == 'Eses':
          return('mibb')
      if word == 'mib' or word == '��b' or word == 'Es':
          return('mib')
      if word == 'mi' or word == '��' or word == 'E':
          return('mi')
      if word == 'mi#' or word == '��#' or word == 'Eis':
          return('mi#')
      if word == 'mi##' or word == '��##' or word == 'Eisis':
          return('mi##')
      if word == 'fabb' or word == '��bb' or word == 'Feses':
          return('fabb')
      if word == 'fab' or word == '��b' or word == 'Fes':
          return('fab')
      if word == 'fa' or word == '��' or word == 'F':
          return('fa')
      if word == 'fa#' or word == '��#' or word == 'Fis':
          return('fa#')
      if word == 'fa##' or word == '��##' or word == 'Fisis':
          return('fa##')
      if word == 'solbb' or word == '����bb' or word == 'Geses':
          return('solbb')
      if word == 'solb' or word == '����b' or word == 'Ges':
          return('solb')
      if word == 'sol' or word == '����' or word == 'G':
          return('sol')
      if word == 'sol#' or word == '����#' or word == 'Gis':
          return('sol#')
      if word == 'sol##' or word == '����##' or word == 'Gisis':
          return('sol##')
      if word == 'labb' or word == '��bb' or word == 'Ases':
          return('labb')
      if word == 'lab' or word == '��b' or word == 'As':
          return('lab')
      if word == 'la' or word == '��' or word == 'A': 
          return('la')
      if word == 'la#' or word == '��#' or word == 'Ais':
          return('la#')
      if word == 'la##' or word == '��##' or word == 'Aisis':
          return('la##')
      if word == 'sibb' or word == '��bb' or word == 'Heses':
          return('sibb')
      if word == 'sib' or word == '��b' or word == 'B' or word == 'Hes':
          return('sib')
      if word == 'si' or word == '��' or word == 'H':
          return('si')
      if word == 'si#' or word == '��#' or word == 'His':
          return('si#')
      if word == 'si##' or word == '��##' or word == 'Hisis':
          return('si##')
      else: return('������')
    if example == '��' or example == 2 or example == 'ru':
      if word == 'dobb' or word == '��bb' or word == 'Ceses':
          return('��bb')
      if word == 'dob' or word == '��b' or word == 'Ces':
          return('��b')
      if word == 'do' or word == '��' or word == 'C':
          return('��')
      if word == 'do#' or word == '��#' or word == 'Cis':
          return('��#')
      if word == 'do##' or word == '��##' or word == 'Cisis':
          return('��##')
      if word == 'rebb' or word == '��bb' or word == 'Deses':
          return('��bb')
      if word == 'reb' or word == '��b' or word == 'Des':
          return('��b')
      if word == 're' or word == '��' or word == 'D':
          return('��')
      if word == 're#' or word == '��#' or word == 'Dis':
          return('��#')
      if word == 're##' or word == '��##' or word == 'Disis':
          return('��##')
      if word == 'mibb' or word == '��bb' or word == 'Eses':
          return('��bb')
      if word == 'mib' or word == '��b' or word == 'Es':
          return('��b')
      if word == 'mi' or word == '��' or word == 'E':
          return('��')
      if word == 'mi#' or word == '��#' or word == 'Eis':
          return('��#')
      if word == 'mi##' or word == '��##' or word == 'Eisis':
          return('��##')
      if word == 'fab' or word == '��b' or word == 'Fes':
          return('��b')
      if word == 'fabb' or word == '��bb' or word == 'Feses':
          return('��bb')
      if word == 'fa' or word == '��' or word == 'F':
          return('��')
      if word == 'fa#' or word == '��#' or word == 'Fis':
          return('��#')
      if word == 'fa##' or word == '��##' or word == 'Fisis':
          return('��##')
      if word == 'solbb' or word == '����bb' or word == 'Geses':
          return('����bb')
      if word == 'solb' or word == '����b' or word == 'Ges':
          return('����b')
      if word == 'sol' or word == '����' or word == 'G':
          return('����')
      if word == 'sol#' or word == '����#' or word == 'Gis':
          return('����#')
      if word == 'sol##' or word == '����##' or word == 'Gisis':
          return('����##')
      if word == 'labb' or word == '��bb' or word == 'Ases':
          return('��bb')
      if word == 'lab' or word == '��b' or word == 'As':
          return('��b')
      if word == 'la' or word == '��' or word == 'A': 
          return('��')
      if word == 'la#' or word == '��#' or word == 'Ais':
          return('��#')
      if word == 'la##' or word == '��##' or word == 'Aisis':
          return('��##')
      if word == 'sibb' or word == '��bb' or word == 'Heses':
          return('��bb')
      if word == 'sib' or word == '��b' or word == 'B':
          return('��b')
      if word == 'si' or word == '��' or word == 'H':
          return('��')
      if word == 'si#' or word == '��#' or word == 'His':
          return('��#')
      if word == 'si##' or word == '��##' or word == 'Hisis':
          return('��##')
      else: return('������')
    if example == 'C' or example == 3 or example == 'de' or example == 'eng':
      if word == 'dobb' or word == '��bb' or word == 'Ceses':
          return('Ceses')
      if word == 'dob' or word == '��b' or word == 'Ces':
          return('Ceses')
      if word == 'do' or word == '��' or word == 'C':
          return('C')
      if word == 'do#' or word == '��#' or word == 'Cis':
          return('Cis')
      if word == 'do##' or word == '��##' or word == 'Cisis':
          return('Cisis')
      if word == 'rebb' or word == '��bb' or word == 'Deses':
          return('Deses')
      if word == 'reb' or word == '��b' or word == 'Des':
          return('Des')
      if word == 're' or word == '��' or word == 'D':
          return('D')
      if word == 're#' or word == '��#' or word == 'Dis':
          return('Dis')
      if word == 're##' or word == '��##' or word == 'Disis':
          return('Disis')
      if word == 'mibb' or word == '��bb' or word == 'Eses':
          return('Eses')
      if word == 'mib' or word == '��b' or word == 'Es':
          return('Es')
      if word == 'mi' or word == '��' or word == 'E':
          return('E')
      if word == 'mi#' or word == '��#' or word == 'Eis':
          return('Eis')
      if word == 'mi##' or word == '��##' or word == 'Eisis':
          return('Eisis')
      if word == 'fabb' or word == '��bb' or word == 'Feses':
          return('Feses')
      if word == 'fab' or word == '��b' or word == 'Fes':
          return('Fes')
      if word == 'fa' or word == '��' or word == 'F':
          return('F')
      if word == 'fa#' or word == '��#' or word == 'Fis':
          return('Fis')
      if word == 'fa##' or word == '��##' or word == 'Fisis':
          return('Fisis')
      if word == 'solbb' or word == '����bb' or word == 'Geses':
          return('Geses')
      if word == 'solb' or word == '����b' or word == 'Ges':
          return('Ges')
      if word == 'sol' or word == '����' or word == 'G':
          return('G')
      if word == 'sol#' or word == '����#' or word == 'Gis':
          return('Gis')
      if word == 'sol##' or word == '����##' or word == 'Gisis':
          return('Gisis')
      if word == 'labb' or word == '��bb' or word == 'Ases':
          return('Ases')
      if word == 'lab' or word == '��b' or word == 'As':
          return('As')
      if word == 'la' or word == '��' or word == 'A': 
          return('A')
      if word == 'la#' or word == '��#' or word == 'Ais':
          return('Ais')
      if word == 'la##' or word == '��##' or word == 'Aisis':
          return('Aisis')
      if word == 'sibb' or word == '��bb' or word == 'Heses':
          return('Heses')
      if word == 'sib' or word == '��b' or word == 'B':
          return('B')
      if word == 'si' or word == '��' or word == 'H':
          return('H')
      if word == 'si#' or word == '��#' or word == 'His':
          return('His')
      if word == 'si##' or word == '��##' or word == 'Hisis':
          return('Hisis')
      else: return('������')
    else: return('������')
def pitch_and_step_to_note(pitch,step):
    step = step%7
    pitch = pitch%6
    if step == 1:
        if pitch == 5.0 or pitch == -1.0:
         return('dobb')
        if pitch == 5.5 or pitch == -0.5:
         return('dob')
        if pitch == 6 or pitch == 0:
         return('do')
        if pitch == 0.5:
         return('do#') 
        if pitch == 1:
         return('do##')
    if step == 2:
        if pitch == 0:
         return('rebb')
        if pitch == 0.5:
         return('reb')
        if pitch == 1:
         return('re')
        if pitch == 1.5:
         return('re#') 
        if pitch == 2:
         return('re##')
    if step == 3:
        if pitch == 1:
         return('mibb')
        if pitch == 1.5:
         return('mib')
        if pitch == 2:
         return('mi')
        if pitch == 2.5:
         return('mi#') 
        if pitch == 3.0:
         return('mi##')
    if step == 4:
        if pitch == 1.5:
         return('fabb')
        if pitch == 2:
         return('fab')
        if pitch == 2.5:
         return('fa')
        if pitch == 3:
         return('fa#') 
        if pitch == 3.5:
         return('fa##') 
    if step == 5:
        if pitch == 2.5:
         return('solbb')
        if pitch == 3:
         return('solb')
        if pitch == 3.5:
         return('sol')
        if pitch == 4:
         return('sol#') 
        if pitch == 4.5:
         return('sol##')
    if step == 6:
        if pitch == 3.5:
         return('labb')
        if pitch == 4:
         return('lab')
        if pitch == 4.5:
         return('la')
        if pitch == 5:
         return('la#') 
        if pitch == 5.5:
         return('la##')
    if step == 7 or step == 0:
        if pitch == 4.5:
         return('sibb')
        if pitch == 5:
         return('sib')
        if pitch == 5.5:
         return('si')
        if pitch == 6.0 or pitch == 0:
         return('si#') 
        if pitch == 6.5 or pitch == 0.5:
         return('si##')
    else:
         return('������')
def note_to_rounding(note=str):
    if note == 'dobb' or note == '��bb' or note == 'Ceses':
        return('do')
    if note == 'dob' or note == '��b' or note == 'Ces':
        return('do')
    if note == 'do' or note == '��' or note == 'C':
        return('do')
    if note == 'do#' or note == '��#' or note == 'Cis':
        return('do')
    if note == 'do##' or note == '��##' or note == 'Cisis':
        return('do')
    if note == 'rebb' or note == '��bb' or note == 'Deses':
        return('re')
    if note == 'reb' or note == '��b' or note == 'Des':
        return('re')
    if note == 're' or note == '��' or note == 'D':
        return('re')
    if note == 're#' or note == '��#' or note == 'Dis':
        return('re')
    if note == 're##' or note == '��##' or note == 'Disis':
        return('re')
    if note == 'mibb' or note == '��bb' or note == 'Eses':
        return('mi')
    if note == 'mib' or note == '��b' or note == 'Es':
        return('mi')
    if note == 'mi' or note == '��' or note == 'E':
        return('mi')
    if note == 'mi#' or note == '��#' or note == 'Eis':
        return('mi')
    if note == 'mi##' or note == '��##' or note == 'Eisis':
        return('mi')
    if note == 'fabb' or note == '��bb' or note == 'Feses':
        return('fa')
    if note == 'fab' or note == '��b' or note == 'Fes':
        return('fa')
    if note == 'fa' or note == '��' or note == 'F':
        return('fa')
    if note == 'fa#' or note == '��#' or note == 'Fis':
        return('fa')
    if note == 'fa##' or note == '��##' or note == 'Fisis':
        return('fa')
    if note == 'solbb' or note == '����bb' or note == 'Geses':
        return('sol')
    if note == 'solb' or note == '����b' or note == 'Ges':
        return('sol')
    if note == 'sol' or note == 'c���' or note == 'G':
        return('sol')
    if note == 'sol#' or note == '����#' or note == 'Gis':
        return('sol')
    if note == 'sol##' or note == '����##' or note == 'Gisis':
        return('sol')
    if note == 'labb' or note == '��bb' or note == 'Ases':
        return('la')
    if note == 'lab' or note == '��b' or note == 'As':
        return('la')
    if note == 'la' or note == '��' or note == 'A':
        return('la')
    if note == 'la#' or note == '��#' or note == 'Ais':
        return('la')
    if note == 'la##' or note == '��##' or note == 'Aisis':
        return('la')
    if note == 'sibb' or note == '��bb' or note == 'Heses':
        return('si')
    if note == 'sib' or note == '��b' or note == 'B' or note == 'hes':
        return('si')
    if note == 'si' or note == 'c�' or note == 'H':
        return('si')
    if note == 'si#' or note == 'c�#' or note == 'His':
        return('si')
    if note == 'si##' or note == 'c�##' or note == 'Hisis':
        return('si')
    else:
        return('������')
import leomusiclib.chords as ch
import leomusiclib.intervals as i
def dir_body_to_ch_int(a,body=str,direction='up'):
    if direction == 'up':
        if body == 'ch1':
            return i.ch1_up(a)
        if body == 'uv1':
            return i.uv1_up(a)
        if body == 'um2':
            return i.um2_up(a)
        if body == 'm2':
            return i.m2_up(a)
        if body == 'b2':
            return i.b2_up(a)
        if body == 'uv2':
            return i.uv2_up(a)
        if body == 'um3':
            return i.um3_up(a)
        if body == 'm3':
            return i.m3_up(a)
        if body == 'b3':
            return i.b3_up(a)
        if body == 'um4':
            return i.um4_up(a)
        if body == 'ch4':
            return i.ch4_up(a)
        if body == 'uv4':
            return i.uv4_up(a)
        if body == 'um5':
            return i.um5_up(a)
        if body == 'ch5':
            return i.ch5_up(a)
        if body == 'uv5':
            return i.uv5_up(a)
        if body == 'um6':
            return i.um6_up(a)
        if body == 'm6':
            return i.m6_up(a)
        if body == 'b6':
            return i.b6_up(a)
        if body == 'uv6':
            return i.uv6_up(a)
        if body == 'um7':
            return i.um7_up(a)
        if body == 'm7':
            return i.m7_up(a)
        if body == 'b7':
            return i.b7_up(a)
        if body == 'uv7':
            return i.uv7_up(a)

        if body == 'T3':
            return ch.T3_up(a)
        if body == 'T53':
            return ch.T53_up(a)
        if body == 't53':
            return ch.t53_up(a)
        if body == 'T6':
            return ch.T6_up(a)
        if body == 't6':
            return ch.t6_up(a)
        if body == 'T64':
            return ch.T64_up(a)
        if body == 't64':
            return ch.t64_up(a)
        if body == 'D7' or 'd7':
            return ch.d7_up(a)
        if body == 'D65' or 'd65':
            return ch.d65_up(a)
        if body == 'D43' or 'd43':
            return ch.d43_up(a)
        if body == 'D2' or 'd2':
            return ch.d2_up(a)
        if body == 'T53r1':
            return ch.T53r1_up
        if body == 'T53r2' or 'T53razv':
            return ch.T53r1_up
        if body == 't53r1':
            return ch.t53r1_up
        if body == 't53r2' or 't53razv':
            return ch.t53r1_up
        
    if direction == 'down':
        if body == 'ch1':
            return i.ch1_down(a)
        if body == 'uv1':
            return i.uv1_down(a)
        if body == 'um2':
            return i.um2_down(a)
        if body == 'm2':
            return i.m2_down(a)
        if body == 'b2':
            return i.b2_down(a)
        if body == 'uv2':
            return i.uv2_down(a)
        if body == 'um3':
            return i.um3_down(a)
        if body == 'm3':
            return i.m3_down(a)
        if body == 'b3':
            return i.b3_down(a)
        if body == 'um4':
            return i.um4_down(a)
        if body == 'ch4':
            return i.ch4_down(a)
        if body == 'uv4':
            return i.uv4_down(a)
        if body == 'um5':
            return i.um5_down(a)
        if body == 'ch5':
            return i.ch5_down(a)
        if body == 'uv5':
            return i.uv5_down(a)
        if body == 'um6':
            return i.um6_down(a)
        if body == 'm6':
            return i.m6_down(a)
        if body == 'b6':
            return i.b6_down(a)
        if body == 'uv6':
            return i.uv6_down(a)
        if body == 'um7':
            return i.um7_down(a)
        if body == 'm7':
            return i.m7_down(a)
        if body == 'b7':
            return i.b7_down(a)
        if body == 'uv7':
            return i.uv7_down(a)

        if body == 'T53':
            return ch.T53_down(a)
        if body == 't53':
            return ch.t53_down(a)
        if body == 'T6':
            return ch.T6_down(a)
        if body == 't6':
            return ch.t6_down(a)
        if body == 'T64':
            return ch.T64_down(a)
        if body == 't64':
            return ch.t64_down(a)
        if body == 'D7' or 'd7':
            return ch.d7_down(a)
        if body == 'D65' or 'd65':
            return ch.d65_down(a)
        if body == 'D43' or 'd43':
            return ch.d43_down(a)
        if body == 'D2' or 'd2':
            return ch.d2_down(a)
        