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

def pitch_to_note1(pitch,step):
    c = (pitch-step)%6
    if c == 0:
        if pitch == 0:
         return('do')
        if pitch == 1:
         return('re')
        if pitch == 2:
         return('mi')
        if pitch == 2.5:
         return('fa')
        if pitch == 3.5:
         return('sol')
        if pitch == 4.5:
         return('la')
        if pitch == 5.5:
         return('si')
        else:
         return('������')
    if c == 0.5:
        if pitch == 0.5:
         return('do#')
        if pitch == 1.5:
         return('re#')
        if pitch == 2.5:
         return('mi#')
        if pitch == 3:
         return('fa#')
        if pitch == 4:
         return('sol#')
        if pitch == 5:
         return('la#')
        if pitch == 6:
         return('si#')
        else:
         return('������')
    if c < 0:
        if pitch == 0.5:
         return('reb')
        if pitch == 1.5:
         return('mib')
        if pitch == 2:
         return('fab')
        if pitch == 3:
         return('solb')
        if pitch == 4:
         return('lab')
        if pitch == 5:
         return('sib')
        else:
         return('������')
    if c == 5.5:
         return('dob')
    else: return('������')
def pitch_to_note2(pitch,lift):
    if pitch == 0:
         return('do')
    if pitch == 1:
         return('re')
    if pitch == 3.5:
         return('sol')
    if pitch == 4.5:
         return('la')
    if lift == 0 or lift == 'stay':
        if pitch == 0:
         return('do')
        if pitch == 1:
         return('re')
        if pitch == 2:
         return('mi')
        if pitch == 2.5:
         return('fa')
        if pitch == 3.5:
         return('sol')
        if pitch == 4.5:
         return('la')
        if pitch == 5.5:
         return('si')
        else:
         return('������')
    if lift == 'up' or lift == 0.5:
        if pitch == 0.5:
         return('do#')
        if pitch == 1.5:
         return('re#')
        if pitch == 2.5:
         return('mi#')
        if pitch == 3:
         return('fa#')
        if pitch == 4:
         return('sol#')
        if pitch == 5:
         return('la#')
        if pitch == 6:
         return('si#')
        if pitch == 2:
         return('mi')
        if pitch == 5.5:
         return('si')
        else:
         return('������')
    if lift == 'down' or lift == -0.5:
        if pitch == 0.5:
         return('reb')
        if pitch == 1.5:
         return('mib')
        if pitch == 2:
         return('fab')
        if pitch == 3:
         return('solb')
        if pitch == 4:
         return('lab')
        if pitch == 5:
         return('sib')
        if pitch == 5.5:
         return('dob')
        if pitch == 2.5:
         return('fa')
        if pitch == 6.0:
         return('si#')
    else:
         return('������')