# -*- coding: cp1251 -*-
import leomusiclib.chords as ch
import leomusiclib.intervals as i
import leomusiclib.notetocode as ntc

def note_to_pitch(note=str):
    if note == 'dobb' or note == 'доbb' or note == 'Ceses':
        return(5)
    if note == 'dob' or note == 'доb' or note == 'Ces':
        return(5.5)
    if note == 'do' or note == 'до' or note == 'C':
        return(0)
    if note == 'do#' or note == 'до#' or note == 'Cis':
        return(0.5)
    if note == 'do##' or note == 'до##' or note == 'Cisis':
        return(1)
    if note == 'rebb' or note == 'реbb' or note == 'Deses':
        return(0)
    if note == 'reb' or note == 'реb' or note == 'Des':
        return(0.5)
    if note == 're' or note == 'ре' or note == 'D':
        return(1)
    if note == 're#' or note == 'ре#' or note == 'Dis':
        return(1.5)
    if note == 're##' or note == 'ре##' or note == 'Disis':
        return(2)
    if note == 'mibb' or note == 'миbb' or note == 'Eses':
        return(1)
    if note == 'mib' or note == 'миb' or note == 'Es':
        return(1.5)
    if note == 'mi' or note == 'ми' or note == 'E':
        return(2)
    if note == 'mi#' or note == 'ми#' or note == 'Eis':
        return(2.5)
    if note == 'mi##' or note == 'ми##' or note == 'Eisis':
        return(0.5)
    if note == 'fabb' or note == 'фаbb' or note == 'Feses':
        return(1.5)
    if note == 'fab' or note == 'фаb' or note == 'Fes':
        return(2)
    if note == 'fa' or note == 'фа' or note == 'F':
        return(2.5)
    if note == 'fa#' or note == 'фа#' or note == 'Fis':
        return(3)
    if note == 'fa##' or note == 'фа##' or note == 'Fisis':
        return(3.5)
    if note == 'solbb' or note == 'сольbb' or note == 'Geses':
        return(2.5)
    if note == 'solb' or note == 'сольb' or note == 'Ges':
        return(3)
    if note == 'sol' or note == 'cоль' or note == 'G':
        return(3.5)
    if note == 'sol#' or note == 'соль#' or note == 'Gis':
        return(4)
    if note == 'sol##' or note == 'соль##' or note == 'Gisis':
        return(4.5)
    if note == 'labb' or note == 'ляbb' or note == 'Ases':
        return(3.5)
    if note == 'lab' or note == 'ляb' or note == 'As':
        return(4)
    if note == 'la' or note == 'ля' or note == 'A':
        return(4.5)
    if note == 'la#' or note == 'ля#' or note == 'Ais':
        return(5)
    if note == 'la##' or note == 'ля##' or note == 'Aisis':
        return(5.5)
    if note == 'sibb' or note == 'сиbb' or note == 'Heses':
        return(4.5)
    if note == 'sib' or note == 'сиb' or note == 'B' or note == 'Hes':
        return(5)
    if note == 'si' or note == 'cи' or note == 'H':
        return(5.5)
    if note == 'si#' or note == 'cи#' or note == 'His':
        return(6)
    if note == 'si##' or note == 'си##' or note == 'Hisis':
        return(6.5)
    else:
        return('Ошибка')
def note_to_step(note=str):
    if note == 'dobb' or note == 'доbb' or note == 'Ceses':
        return(1)
    if note == 'dob' or note == 'доb' or note == 'Ces':
        return(1)
    if note == 'do' or note == 'до' or note == 'C':
        return(1)
    if note == 'do#' or note == 'до#' or note == 'Cis':
        return(1)
    if note == 'do##' or note == 'до##' or note == 'Cisis':
        return(1)
    if note == 'rebb' or note == 'реbb' or note == 'Deses':
        return(2)
    if note == 'reb' or note == 'реb' or note == 'Des':
        return(2)
    if note == 're' or note == 'ре' or note == 'D':
        return(2)
    if note == 're#' or note == 'ре#' or note == 'Dis':
        return(2)
    if note == 're##' or note == 'ре##' or note == 'Disis':
        return(2)
    if note == 'mibb' or note == 'миbb' or note == 'Eses':
        return(3)
    if note == 'mib' or note == 'миb' or note == 'Es':
        return(3)
    if note == 'mi' or note == 'ми' or note == 'E':
        return(3)
    if note == 'mi#' or note == 'ми#' or note == 'Eis':
        return(3)
    if note == 'mi##' or note == 'ми##' or note == 'Eisis':
        return(3)
    if note == 'fabb' or note == 'фаbb' or note == 'Feses':
        return(4)
    if note == 'fab' or note == 'фаb' or note == 'Fes':
        return(4)
    if note == 'fa' or note == 'фа' or note == 'F':
        return(4)
    if note == 'fa#' or note == 'фа#' or note == 'Fis':
        return(4)
    if note == 'fa##' or note == 'фа##' or note == 'Fisis':
        return(4)
    if note == 'solbb' or note == 'сольbb' or note == 'Geses':
        return(5)
    if note == 'solb' or note == 'сольb' or note == 'Ges':
        return(5)
    if note == 'sol' or note == 'cоль' or note == 'G':
        return(5)
    if note == 'sol#' or note == 'соль#' or note == 'Gis':
        return(5)
    if note == 'sol##' or note == 'соль##' or note == 'Gisis':
        return(5)
    if note == 'labb' or note == 'ляbb' or note == 'Ases':
        return(6)
    if note == 'lab' or note == 'ляb' or note == 'As':
        return(6)
    if note == 'la' or note == 'ля' or note == 'A':
        return(6)
    if note == 'la#' or note == 'ля#' or note == 'Ais':
        return(6)
    if note == 'la##' or note == 'ля##' or note == 'Aisis':
        return(6)
    if note == 'sibb' or note == 'сиbb' or note == 'Heses':
        return(7)
    if note == 'sib' or note == 'сиb' or note == 'B':
        return(7)
    if note == 'si' or note == 'cи' or note == 'H':
        return(7)
    if note == 'si#' or note == 'cи#' or note == 'H#':
        return(7)
    if note == 'si##' or note == 'си##' or note == 'Hisis':
        return(7)
    else:
        return('Ошибка')
def renamer(word,example):
    if example == 'do' or example == 1 or example == 'en':
      if word == 'dobb' or word == 'доbb' or word == 'Ceses':
          return('dobb')
      if word == 'dob' or word == 'доb' or word == 'Ces':
          return('dob')
      if word == 'do' or word == 'до' or word == 'C':
          return('do')
      if word == 'do#' or word == 'до#' or word == 'Cis':
          return('do#')
      if word == 'do##' or word == 'до##' or word == 'Cisis':
          return('do##')
      if word == 'rebb' or word == 'реbb' or word == 'Deses':
          return('rebb')
      if word == 'reb' or word == 'реb' or word == 'Des':
          return('reb')
      if word == 're' or word == 'ре' or word == 'D':
          return('re')
      if word == 're#' or word == 'ре#' or word == 'Dis':
          return('re#')
      if word == 're##' or word == 'ре##' or word == 'Disis':
          return('re##')
      if word == 'mibb' or word == 'миbb' or word == 'Eses':
          return('mibb')
      if word == 'mib' or word == 'миb' or word == 'Es':
          return('mib')
      if word == 'mi' or word == 'ми' or word == 'E':
          return('mi')
      if word == 'mi#' or word == 'ми#' or word == 'Eis':
          return('mi#')
      if word == 'mi##' or word == 'ми##' or word == 'Eisis':
          return('mi##')
      if word == 'fabb' or word == 'фаbb' or word == 'Feses':
          return('fabb')
      if word == 'fab' or word == 'фаb' or word == 'Fes':
          return('fab')
      if word == 'fa' or word == 'фа' or word == 'F':
          return('fa')
      if word == 'fa#' or word == 'фа#' or word == 'Fis':
          return('fa#')
      if word == 'fa##' or word == 'фа##' or word == 'Fisis':
          return('fa##')
      if word == 'solbb' or word == 'сольbb' or word == 'Geses':
          return('solbb')
      if word == 'solb' or word == 'сольb' or word == 'Ges':
          return('solb')
      if word == 'sol' or word == 'соль' or word == 'G':
          return('sol')
      if word == 'sol#' or word == 'соль#' or word == 'Gis':
          return('sol#')
      if word == 'sol##' or word == 'соль##' or word == 'Gisis':
          return('sol##')
      if word == 'labb' or word == 'ляbb' or word == 'Ases':
          return('labb')
      if word == 'lab' or word == 'ляb' or word == 'As':
          return('lab')
      if word == 'la' or word == 'ля' or word == 'A': 
          return('la')
      if word == 'la#' or word == 'ля#' or word == 'Ais':
          return('la#')
      if word == 'la##' or word == 'ля##' or word == 'Aisis':
          return('la##')
      if word == 'sibb' or word == 'сиbb' or word == 'Heses':
          return('sibb')
      if word == 'sib' or word == 'сиb' or word == 'B' or word == 'Hes':
          return('sib')
      if word == 'si' or word == 'си' or word == 'H':
          return('si')
      if word == 'si#' or word == 'си#' or word == 'His':
          return('si#')
      if word == 'si##' or word == 'си##' or word == 'Hisis':
          return('si##')
      else: return('Ошибка')
    if example == 'до' or example == 2 or example == 'ru':
      if word == 'dobb' or word == 'доbb' or word == 'Ceses':
          return('доbb')
      if word == 'dob' or word == 'доb' or word == 'Ces':
          return('доb')
      if word == 'do' or word == 'до' or word == 'C':
          return('до')
      if word == 'do#' or word == 'до#' or word == 'Cis':
          return('до#')
      if word == 'do##' or word == 'до##' or word == 'Cisis':
          return('до##')
      if word == 'rebb' or word == 'реbb' or word == 'Deses':
          return('реbb')
      if word == 'reb' or word == 'реb' or word == 'Des':
          return('реb')
      if word == 're' or word == 'ре' or word == 'D':
          return('ре')
      if word == 're#' or word == 'ре#' or word == 'Dis':
          return('ре#')
      if word == 're##' or word == 'ре##' or word == 'Disis':
          return('ре##')
      if word == 'mibb' or word == 'миbb' or word == 'Eses':
          return('миbb')
      if word == 'mib' or word == 'миb' or word == 'Es':
          return('миb')
      if word == 'mi' or word == 'ми' or word == 'E':
          return('ми')
      if word == 'mi#' or word == 'ми#' or word == 'Eis':
          return('ми#')
      if word == 'mi##' or word == 'ми##' or word == 'Eisis':
          return('ми##')
      if word == 'fab' or word == 'фаb' or word == 'Fes':
          return('фаb')
      if word == 'fabb' or word == 'фаbb' or word == 'Feses':
          return('фаbb')
      if word == 'fa' or word == 'фа' or word == 'F':
          return('фа')
      if word == 'fa#' or word == 'фа#' or word == 'Fis':
          return('фа#')
      if word == 'fa##' or word == 'фа##' or word == 'Fisis':
          return('фа##')
      if word == 'solbb' or word == 'сольbb' or word == 'Geses':
          return('сольbb')
      if word == 'solb' or word == 'сольb' or word == 'Ges':
          return('сольb')
      if word == 'sol' or word == 'соль' or word == 'G':
          return('соль')
      if word == 'sol#' or word == 'соль#' or word == 'Gis':
          return('соль#')
      if word == 'sol##' or word == 'соль##' or word == 'Gisis':
          return('соль##')
      if word == 'labb' or word == 'ляbb' or word == 'Ases':
          return('ляbb')
      if word == 'lab' or word == 'ляb' or word == 'As':
          return('ляb')
      if word == 'la' or word == 'ля' or word == 'A': 
          return('ля')
      if word == 'la#' or word == 'ля#' or word == 'Ais':
          return('ля#')
      if word == 'la##' or word == 'ля##' or word == 'Aisis':
          return('ля##')
      if word == 'sibb' or word == 'сиbb' or word == 'Heses':
          return('сиbb')
      if word == 'sib' or word == 'сиb' or word == 'B':
          return('сиb')
      if word == 'si' or word == 'си' or word == 'H':
          return('си')
      if word == 'si#' or word == 'си#' or word == 'His':
          return('си#')
      if word == 'si##' or word == 'си##' or word == 'Hisis':
          return('си##')
      else: return('Ошибка')
    if example == 'C' or example == 3 or example == 'de' or example == 'eng':
      if word == 'dobb' or word == 'доbb' or word == 'Ceses':
          return('Ceses')
      if word == 'dob' or word == 'доb' or word == 'Ces':
          return('Ceses')
      if word == 'do' or word == 'до' or word == 'C':
          return('C')
      if word == 'do#' or word == 'до#' or word == 'Cis':
          return('Cis')
      if word == 'do##' or word == 'до##' or word == 'Cisis':
          return('Cisis')
      if word == 'rebb' or word == 'реbb' or word == 'Deses':
          return('Deses')
      if word == 'reb' or word == 'реb' or word == 'Des':
          return('Des')
      if word == 're' or word == 'ре' or word == 'D':
          return('D')
      if word == 're#' or word == 'ре#' or word == 'Dis':
          return('Dis')
      if word == 're##' or word == 'ре##' or word == 'Disis':
          return('Disis')
      if word == 'mibb' or word == 'миbb' or word == 'Eses':
          return('Eses')
      if word == 'mib' or word == 'миb' or word == 'Es':
          return('Es')
      if word == 'mi' or word == 'ми' or word == 'E':
          return('E')
      if word == 'mi#' or word == 'ми#' or word == 'Eis':
          return('Eis')
      if word == 'mi##' or word == 'ми##' or word == 'Eisis':
          return('Eisis')
      if word == 'fabb' or word == 'фаbb' or word == 'Feses':
          return('Feses')
      if word == 'fab' or word == 'фаb' or word == 'Fes':
          return('Fes')
      if word == 'fa' or word == 'фа' or word == 'F':
          return('F')
      if word == 'fa#' or word == 'фа#' or word == 'Fis':
          return('Fis')
      if word == 'fa##' or word == 'фа##' or word == 'Fisis':
          return('Fisis')
      if word == 'solbb' or word == 'сольbb' or word == 'Geses':
          return('Geses')
      if word == 'solb' or word == 'сольb' or word == 'Ges':
          return('Ges')
      if word == 'sol' or word == 'соль' or word == 'G':
          return('G')
      if word == 'sol#' or word == 'соль#' or word == 'Gis':
          return('Gis')
      if word == 'sol##' or word == 'соль##' or word == 'Gisis':
          return('Gisis')
      if word == 'labb' or word == 'ляbb' or word == 'Ases':
          return('Ases')
      if word == 'lab' or word == 'ляb' or word == 'As':
          return('As')
      if word == 'la' or word == 'ля' or word == 'A': 
          return('A')
      if word == 'la#' or word == 'ля#' or word == 'Ais':
          return('Ais')
      if word == 'la##' or word == 'ля##' or word == 'Aisis':
          return('Aisis')
      if word == 'sibb' or word == 'сиbb' or word == 'Heses':
          return('Heses')
      if word == 'sib' or word == 'сиb' or word == 'B':
          return('B')
      if word == 'si' or word == 'си' or word == 'H':
          return('H')
      if word == 'si#' or word == 'си#' or word == 'His':
          return('His')
      if word == 'si##' or word == 'си##' or word == 'Hisis':
          return('Hisis')
      else: return('Ошибка')
    else: return('Ошибка')
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
         return('Ошибка')
def note_to_rounding(note=str):
    if note == 'dobb' or note == 'доbb' or note == 'Ceses':
        return('do')
    if note == 'dob' or note == 'доb' or note == 'Ces':
        return('do')
    if note == 'do' or note == 'до' or note == 'C':
        return('do')
    if note == 'do#' or note == 'до#' or note == 'Cis':
        return('do')
    if note == 'do##' or note == 'до##' or note == 'Cisis':
        return('do')
    if note == 'rebb' or note == 'реbb' or note == 'Deses':
        return('re')
    if note == 'reb' or note == 'реb' or note == 'Des':
        return('re')
    if note == 're' or note == 'ре' or note == 'D':
        return('re')
    if note == 're#' or note == 'ре#' or note == 'Dis':
        return('re')
    if note == 're##' or note == 'ре##' or note == 'Disis':
        return('re')
    if note == 'mibb' or note == 'миbb' or note == 'Eses':
        return('mi')
    if note == 'mib' or note == 'миb' or note == 'Es':
        return('mi')
    if note == 'mi' or note == 'ми' or note == 'E':
        return('mi')
    if note == 'mi#' or note == 'ми#' or note == 'Eis':
        return('mi')
    if note == 'mi##' or note == 'ми##' or note == 'Eisis':
        return('mi')
    if note == 'fabb' or note == 'фаbb' or note == 'Feses':
        return('fa')
    if note == 'fab' or note == 'фаb' or note == 'Fes':
        return('fa')
    if note == 'fa' or note == 'фа' or note == 'F':
        return('fa')
    if note == 'fa#' or note == 'фа#' or note == 'Fis':
        return('fa')
    if note == 'fa##' or note == 'фа##' or note == 'Fisis':
        return('fa')
    if note == 'solbb' or note == 'сольbb' or note == 'Geses':
        return('sol')
    if note == 'solb' or note == 'сольb' or note == 'Ges':
        return('sol')
    if note == 'sol' or note == 'cоль' or note == 'G':
        return('sol')
    if note == 'sol#' or note == 'соль#' or note == 'Gis':
        return('sol')
    if note == 'sol##' or note == 'соль##' or note == 'Gisis':
        return('sol')
    if note == 'labb' or note == 'ляbb' or note == 'Ases':
        return('la')
    if note == 'lab' or note == 'ляb' or note == 'As':
        return('la')
    if note == 'la' or note == 'ля' or note == 'A':
        return('la')
    if note == 'la#' or note == 'ля#' or note == 'Ais':
        return('la')
    if note == 'la##' or note == 'ля##' or note == 'Aisis':
        return('la')
    if note == 'sibb' or note == 'сиbb' or note == 'Heses':
        return('si')
    if note == 'sib' or note == 'сиb' or note == 'B' or note == 'hes':
        return('si')
    if note == 'si' or note == 'cи' or note == 'H':
        return('si')
    if note == 'si#' or note == 'cи#' or note == 'His':
        return('si')
    if note == 'si##' or note == 'cи##' or note == 'Hisis':
        return('si')
    else:
        return('Ошибка')
def dir_body_to_ch_int(a,body,direction):
    if direction == 'up':

        if body == 'ch1':
            return (a,i.ch1_up(a))
        if body == 'uv1':
            return (a,i.uv1_up(a))
        if body == 'um2':
            return (a,i.um2_up(a))
        if body == 'm2':
            return (a,i.m2_up(a))
        if body == 'b2':
            return (a,i.b2_up(a))
        if body == 'uv2':
            return (a,i.uv2_up(a))
        if body == 'um3':
            return (a,i.um3_up(a))
        if body == 'm3':
            return (a,i.m3_up(a))
        if body == 'b3':
            return (a,i.b3_up(a))
        if body == 'um4':
            return (a,i.um4_up(a))
        if body == 'ch4':
            return (a,i.ch4_up(a))
        if body == 'uv4':
            return (a,i.uv4_up(a))
        if body == 'um5':
            return (a,i.um5_up(a))
        if body == 'ch5':
            return (a,i.ch5_up(a))
        if body == 'uv5':
            return (a,i.uv5_up(a))
        if body == 'um6':
            return (a,i.um6_up(a))
        if body == 'm6':
            return (a,i.m6_up(a))
        if body == 'b6':
            return (a,i.b6_up(a))
        if body == 'uv6':
            return (a,i.uv6_up(a))
        if body == 'um7':
            return (a,i.um7_up(a))
        if body == 'm7':
            return (a,i.m7_up(a))
        if body == 'b7':
            return (a,i.b7_up(a))
        if body == 'uv7':
            return (a,i.uv7_up(a))
        if body == 'um8':
            return (a,i.um8_up(a))
        if body == 'ch8':
            return (a,i.ch8_up(a))
        if body == 'uv8':
            return (a,i.uv8_up(a))

        if body == 'T3':
            return ch.T3_up(a)
        if body == 'T53' or body == 'S53':
            return ch.T53_up(a)
        if body == 't53' or body == 's53':
            return ch.t53_up(a)
        if body == 'T6'  or body == 'S6':
            return ch.T6_up(a)
        if body == 't6'  or body == 's6':
            return ch.t6_up(a)
        if body == 'T64' or body == 'S64':
            return ch.T64_up(a)
        if body == 't64' or body == 's64':
            return ch.t64_up(a)
        if body == 'D7' or body == 'd7':
            return ch.d7_up
        if body == 'D65' or body == 'd65':
            return ch.d65_up(a)
        if body == 'D43' or body == 'd43':
            return ch.d43_up(a)
        if body == 'D2' or body == 'd2':
            return ch.d2_up(a)
        if body == 'T53r1':
            return ch.T53r1_up(a)
        if body == 'T53r2' or body == 'T53razv':
            return ch.T53r1_up(a)
        if body == 't53r1':
            return ch.t53r1_up(a)
        if body == 't53r2' or body == 't53razv':
            return ch.t53r1_up  

    if direction == 'down':

        if body == 'ch1':
            return (a,i.ch1_down(a))
        if body == 'uv1':
            return (a,i.uv1_down(a))
        if body == 'um2':
            return (a,i.um2_down(a))
        if body == 'm2':
            return (a,i.m2_down(a))
        if body == 'b2':
            return (a,i.b2_down(a))
        if body == 'uv2':
            return (a,i.uv2_down(a))
        if body == 'um3':
            return (a,i.um3_down(a))
        if body == 'm3':
            return (a,i.m3_down(a))
        if body == 'b3':
            return (a,i.b3_down(a))
        if body == 'um4':
            return (a,i.um4_down(a))
        if body == 'ch4':
            return (a,i.ch4_down(a))
        if body == 'uv4':
            return (a,i.uv4_down(a))
        if body == 'um5':
            return (a,i.um5_down(a))
        if body == 'ch5':
            return (a,i.ch5_down(a))
        if body == 'uv5':
            return (a,i.uv5_down(a))
        if body == 'um6':
            return (a,i.um6_down(a))
        if body == 'm6':
            return (a,i.m6_down(a))
        if body == 'b6':
            return (a,i.b6_down(a))
        if body == 'uv6':
            return (a,i.uv6_down(a))
        if body == 'um7':
            return (a,i.um7_down(a))
        if body == 'm7':
            return (a,i.m7_down(a))
        if body == 'b7':
            return (a,i.b7_down(a))
        if body == 'uv7':
            return (a,i.uv7_down(a))
        if body == 'um8':
            return (a,i.um8_down(a))
        if body == 'ch8':
            return (a,i.ch8_down(a))
        if body == 'uv8':
            return (a,i.uv8_down(a))

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
        if body == 'D7' or body == 'd7':
            return ch.d7_down(a)
        if body == 'D65' or body == 'd65':
            return ch.d65_down(a)
        if body == 'D43' or body == 'd43':
            return ch.d43_down(a)
        if body == 'D2' or body == 'd2':
            return ch.d2_down(a)
def body_tonal_to_ch_int(body,tonal='C-dur'):
        t = ntc.tonal_step_to_note(tonal,1)
        if body == 'ch1':
            return i.ch1_up(t)
        if body == 'uv1':
            return i.uv1_up(t)
        if body == 'um2':
            return i.um2_up(t)
        if body == 'm2':
            return i.m2_up(t)
        if body == 'b2':
            return i.b2_up(t)
        if body == 'uv2':
            return i.uv2_up(t)
        if body == 'um3':
            return i.um3_up(t)
        if body == 'm3':
            return i.m3_up(t)
        if body == 'b3':
            return i.b3_up(t)
        if body == 'um4':
            return i.um4_up(t)
        if body == 'ch4':
            return i.ch4_up(t)
        if body == 'uv4':
            return i.uv4_up(t)
        if body == 'um5':
            return i.um5_up(t)
        if body == 'ch5':
            return i.ch5_up(t)
        if body == 'uv5':
            return i.uv5_up(t)
        if body == 'um6':
            return i.um6_up(t)
        if body == 'm6':
            return i.m6_up(t)
        if body == 'b6':
            return i.b6_up(t)
        if body == 'uv6':
            return i.uv6_up(t)
        if body == 'um7':
            return i.um7_up(t)
        if body == 'm7':
            return i.m7_up(t)
        if body == 'b7':
            return i.b7_up(t)
        if body == 'uv7':
            return i.uv7_up(t)

        if body == 'T3':
            return ch.T3_ton(t)
        if body == 't3':
            return ch.t3_ton(t)
        if body == 'T53':
            return ch.T53_ton(t)
        if body == 't53':
            return ch.t53_ton(t)
        if body == 'T6':
            return ch.T6_ton(t)
        if body == 't6':
            return ch.t6_ton(t)
        if body == 'T64':
            return ch.T64_ton(t)
        if body == 't64':
            return ch.t64_ton(t)

        s = ntc.tonal_step_to_note(tonal,4)
        if body == 'S53':
            return ch.S53_ton(s)
        if body == 's53':
            return ch.s53_ton(s)
        if body == 'S6':
            return ch.S6_ton(s)
        if body == 's6':
            return ch.S6_ton(s)
        if body == 'S64':
            return ch.S64_ton(s)
        if body == 's64':
            return ch.S64_ton(s)
        d = ntc.tonal_step_to_note(tonal,5)
        if body == 'D7' or body == 'd7':
            return ch.d7_ton(d)
        if body == 'D65' or body == 'd65':
            return ch.d65_ton(d)
        if body == 'D43' or body == 'd43':
            return ch.d43_ton(d)
        if body == 'D2' or body == 'd2':
            return ch.d2_ton(d)

        if body == 'T53r1':
            return ch.T53r1_ton(t)
        if body == 'T53r2' or body == 'T53rtzv':
            return ch.T53r1_ton(t)
        if body == 't53r1':
            return ch.t53r1_ton(t)
        if body == 't53r2' or body == 't53rtzv':
            return ch.t53r1_ton(t)   

def tonal_step_to_note(tonal='C',step='1'):
        step = step%7
        #dur
        if tonal == 'Cb' or tonal == 'dob-dur' or tonal == 'Ces-dur' or tonal == 'Ces':
            if step == 1:
                return 'dob'
            if step == 2:
                return 'reb'
            if step == 3:
                return 'mib'
            if step == 4:
                return 'fab'
            if step == 5:
                return 'solb'
            if step == 6:
                return 'lab'
            if step == 7 or step == 0:
                return 'sib'
        if tonal == 'C' or tonal == 'do-dur' or tonal == 'C-dur':
            if step == 1:
                return 'do'
            if step == 2:
                return 're'
            if step == 3:
                return 'mi'
            if step == 4:
                return 'fa'
            if step == 5:
                return 'sol'
            if step == 6:
                return 'la'
            if step == 7 or step == 0:
                return 'si'
        if tonal == 'C#' or tonal == 'do#-dur' or tonal == 'Cis-dur' or tonal == 'Cis':
            if step == 1:
                return 'do#'
            if step == 2:
                return 're#'
            if step == 3:
                return 'mi#'
            if step == 4:
                return 'fa#'
            if step == 5:
                return 'sol#'
            if step == 6:
                return 'la#'
            if step == 7 or step == 0:
                return 'si#'
        if tonal == 'Db' or tonal == 'reb-dur' or tonal == 'Des-dur' or tonal == 'Des':
            if step == 1:
                return 'reb'
            if step == 2:
                return 'mib'
            if step == 3:
                return 'fa'
            if step == 4:
                return 'solb'
            if step == 5:
                return 'lab'
            if step == 6:
                return 'sib'
            if step == 7 or step == 0:
                return 'do'
        if tonal == 'D' or tonal == 're-dur' or tonal == 'D-dur':
            if step == 1:
                return 're'
            if step == 2:
                return 'mi'
            if step == 3:
                return 'fa#'
            if step == 4:
                return 'sol'
            if step == 5:
                return 'la'
            if step == 6:
                return 'si'
            if step == 7 or step == 0:
                return 'do#'
        if tonal == 'D#' or tonal == 're#-dur' or tonal == 'Dis-dur' or tonal == 'Dis':
            if step == 1:
                return 're#'
            if step == 2:
                return 'mi#'
            if step == 3:
                return 'fa##'
            if step == 4:
                return 'sol#'
            if step == 5:
                return 'la#'
            if step == 6:
                return 'si#'
            if step == 7 or step == 0:
                return 'do##'
        if tonal == 'Eb' or tonal == 'mib-dur' or tonal == 'Es-dur' or tonal == 'Es':
            if step == 1:
                return 'mib'
            if step == 2:
                return 'fa'
            if step == 3:
                return 'sol'
            if step == 4:
                return 'lab'
            if step == 5:
                return 'sib'
            if step == 6:
                return 'do'
            if step == 7 or step == 0:
                return 're'
        if tonal == 'E' or tonal == 'mi-dur' or tonal == 'E-dur':
            if step == 1:
                return 'mi'
            if step == 2:
                return 'fa#'
            if step == 3:
                return 'sol#'
            if step == 4:
                return 'la'
            if step == 5:
                return 'si'
            if step == 6:
                return 'do#'
            if step == 7 or step == 0:
                return 're#'
        if tonal == 'E#' or tonal == 'mi#-dur' or tonal == 'Eis-dur' or tonal == 'Eis':
            if step == 1:
                return 'mi#'
            if step == 2:
                return 'fa##'
            if step == 3:
                return 'sol##'
            if step == 4:
                return 'la#'
            if step == 5:
                return 'si#'
            if step == 6:
                return 'do##'
            if step == 7 or step == 0:
                return 're##'
        if tonal == 'Fb' or tonal == 'fab-dur' or tonal == 'Fes-dur' or tonal == 'Fes':
            if step == 1:
                return 'fab'
            if step == 2:
                return 'solb'
            if step == 3:
                return 'lab'
            if step == 4:
                return 'sibb'
            if step == 5:
                return 'dob'
            if step == 6:
                return 'reb'
            if step == 7 or step == 0:
                return 'mib'
        if tonal == 'F' or tonal == 'fa-dur' or tonal == 'F-dur':
            if step == 1:
                return 'fa'
            if step == 2:
                return 'sol'
            if step == 3:
                return 'la'
            if step == 4:
                return 'sib'
            if step == 5:
                return 'do'
            if step == 6:
                return 're'
            if step == 7 or step == 0:
                return 'mi'
        if tonal == 'F#' or tonal == 'fa#-dur' or tonal == 'Fis-dur' or tonal == 'Fis':
            if step == 1:
                return 'fa#'
            if step == 2:
                return 'sol#'
            if step == 3:
                return 'la#'
            if step == 4:
                return 'si'
            if step == 5:
                return 'do#'
            if step == 6:
                return 're#'
            if step == 7 or step == 0:
                return 'mi#'
        if tonal == 'Gb' or tonal == 'solb-dur' or tonal == 'Ges-dur' or tonal == 'Ges':
            if step == 1:
                return 'solb'
            if step == 2:
                return 'lab'
            if step == 3:
                return 'sib'
            if step == 4:
                return 'dob'
            if step == 5:
                return 'reb'
            if step == 6:
                return 'mib'
            if step == 7 or step == 0:
                return 'fa'
        if tonal == 'G' or tonal == 'sol-dur' or tonal == 'G-dur':
            if step == 1:
                return 'sol'
            if step == 2:
                return 'la'
            if step == 3:
                return 'si'
            if step == 4:
                return 'do'
            if step == 5:
                return 're'
            if step == 6:
                return 'mi'
            if step == 7 or step == 0:
                return 'fa#'
        if tonal == 'G#' or tonal == 'sol#-dur' or tonal == 'Gis-dur' or tonal == 'Gis':
            if step == 1:
                return 'sol#'
            if step == 2:
                return 'la#'
            if step == 3:
                return 'si#'
            if step == 4:
                return 'do#'
            if step == 5:
                return 're#'
            if step == 6:
                return 'mi#'
            if step == 7 or step == 0:
                return 'fa##'
        if tonal == 'Ab' or tonal == 'lab-dur' or tonal == 'As-dur' or tonal == 'As':
            if step == 1:
                return 'lab'
            if step == 2:
                return 'sib'
            if step == 3:
                return 'do'
            if step == 4:
                return 'reb'
            if step == 5:
                return 'mib'
            if step == 6:
                return 'fa'
            if step == 7 or step == 0:
                return 'sol'
        if tonal == 'A' or tonal == 'la-dur' or tonal == 'A-dur':
            if step == 1:
                return 'la'
            if step == 2:
                return 'si'
            if step == 3:
                return 'do#'
            if step == 4:
                return 're'
            if step == 5:
                return 'mi'
            if step == 6:
                return 'fa#'
            if step == 7 or step == 0:
                return 'sol#'
        if tonal == 'A#' or tonal == 'la#-dur' or tonal == 'Ais-dur' or tonal == 'Ais':
            if step == 1:
                return 'la#'
            if step == 2:
                return 'si#'
            if step == 3:
                return 'do##'
            if step == 4:
                return 're#'
            if step == 5:
                return 'mi#'
            if step == 6:
                return 'fa##'
            if step == 7 or step == 0:
                return 'sol##'
        if tonal == 'B' or tonal == 'sib-dur' or tonal == 'B-dur' or tonal == 'Hes':
            if step == 1:
                return 'sib'
            if step == 2:
                return 'do'
            if step == 3:
                return 're'
            if step == 4:
                return 'mib'
            if step == 5:
                return 'fa'
            if step == 6:
                return 'sol'
            if step == 7 or step == 0:
                return 'la'
        if tonal == 'H' or tonal == 'si-dur' or tonal == 'H-dur':
            if step == 1:
                return 'si'
            if step == 2:
                return 'do#'
            if step == 3:
                return 're#'
            if step == 4:
                return 'mi'
            if step == 5:
                return 'fa#'
            if step == 6:
                return 'sol#'
            if step == 7 or step == 0:
                return 'la#'
        if tonal == 'H#' or tonal == 'si#-dur' or tonal == 'His-dur' or tonal == 'His':
            if step == 1:
                return 'si#'
            if step == 2:
                return 'do##'
            if step == 3:
                return 're##'
            if step == 4:
                return 'mi#'
            if step == 5:
                return 'fa##'
            if step == 6:
                return 'sol##'
            if step == 7 or step == 0:
                return 'la##'
        #moll
        if tonal == 'cb' or tonal == 'dob-moll' or tonal == 'ces-moll' or tonal == 'ces':
            if step == 1:
                return 'dob'
            if step == 2:
                return 'reb'
            if step == 3:
                return 'mibb'
            if step == 4:
                return 'fab'
            if step == 5:
                return 'solb'
            if step == 6:
                return 'labb'
            if step == 7 or step == 0:
                return 'sibb'
        if tonal == 'c' or tonal == 'do-moll' or tonal == 'c-moll':
            if step == 1:
                return 'do'
            if step == 2:
                return 're'
            if step == 3:
                return 'mib'
            if step == 4:
                return 'fa'
            if step == 5:
                return 'sol'
            if step == 6:
                return 'lab'
            if step == 7 or step == 0:
                return 'sib'
        if tonal == 'c#' or tonal == 'do#-moll' or tonal == 'cis-moll' or tonal == 'cis':
            if step == 1:
                return 'do#'
            if step == 2:
                return 're#'
            if step == 3:
                return 'mi'
            if step == 4:
                return 'fa#'
            if step == 5:
                return 'sol#'
            if step == 6:
                return 'la'
            if step == 7 or step == 0:
                return 'si'
        if tonal == 'db' or tonal == 'reb-moll' or tonal == 'des-moll' or tonal == 'des':
            if step == 1:
                return 'reb'
            if step == 2:
                return 'mib'
            if step == 3:
                return 'fab'
            if step == 4:
                return 'solb'
            if step == 5:
                return 'lab'
            if step == 6:
                return 'sibb'
            if step == 7 or step == 0:
                return 'dob'
        if tonal == 'd' or tonal == 're-moll' or tonal == 'd-moll':
            if step == 1:
                return 're'
            if step == 2:
                return 'mi'
            if step == 3:
                return 'fa'
            if step == 4:
                return 'sol'
            if step == 5:
                return 'la'
            if step == 6:
                return 'sib'
            if step == 7 or step == 0:
                return 'do'
        if tonal == 'd#' or tonal == 're#-moll' or tonal == 'dis-moll' or tonal == 'dis':
            if step == 1:
                return 're#'
            if step == 2:
                return 'mi#'
            if step == 3:
                return 'fa#'
            if step == 4:
                return 'sol#'
            if step == 5:
                return 'la#'
            if step == 6:
                return 'si'
            if step == 7 or step == 0:
                return 'do#'
        if tonal == 'eb' or tonal == 'mib-moll' or tonal == 'es-moll' or tonal == 'es':
            if step == 1:
                return 'mib'
            if step == 2:
                return 'fa'
            if step == 3:
                return 'solb'
            if step == 4:
                return 'lab'
            if step == 5:
                return 'sib'
            if step == 6:
                return 'dob'
            if step == 7 or step == 0:
                return 'reb'
        if tonal == 'e' or tonal == 'mi-moll' or tonal == 'e-moll':
            if step == 1:
                return 'mi'
            if step == 2:
                return 'fa#'
            if step == 3:
                return 'sol'
            if step == 4:
                return 'la'
            if step == 5:
                return 'si'
            if step == 6:
                return 'do'
            if step == 7 or step == 0:
                return 're'
        if tonal == 'e#' or tonal == 'mi#-moll' or tonal == 'eis-moll' or tonal == 'eis':
            if step == 1:
                return 'mi#'
            if step == 2:
                return 'fa##'
            if step == 3:
                return 'sol#'
            if step == 4:
                return 'la#'
            if step == 5:
                return 'si#'
            if step == 6:
                return 'do#'
            if step == 7 or step == 0:
                return 're#'
        if tonal == 'fb' or tonal == 'fab-moll' or tonal == 'fes-moll' or tonal == 'fes':
            if step == 1:
                return 'fab'
            if step == 2:
                return 'solb'
            if step == 3:
                return 'labb'
            if step == 4:
                return 'sibb'
            if step == 5:
                return 'dob'
            if step == 6:
                return 'rebb'
            if step == 7 or step == 0:
                return 'mibb'
        if tonal == 'f' or tonal == 'fa-moll' or tonal == 'f-moll':
            if step == 1:
                return 'fa'
            if step == 2:
                return 'sol'
            if step == 3:
                return 'lab'
            if step == 4:
                return 'sib'
            if step == 5:
                return 'do'
            if step == 6:
                return 'reb'
            if step == 7 or step == 0:
                return 'mib'
        if tonal == 'f#' or tonal == 'fa#-moll' or tonal == 'fis-moll' or tonal == 'fis':
            if step == 1:
                return 'fa#'
            if step == 2:
                return 'sol#'
            if step == 3:
                return 'la'
            if step == 4:
                return 'si'
            if step == 5:
                return 'do#'
            if step == 6:
                return 're'
            if step == 7 or step == 0:
                return 'mi'
        if tonal == 'gb' or tonal == 'solb-moll' or tonal == 'ges-moll' or tonal == 'ges':
            if step == 1:
                return 'solb'
            if step == 2:
                return 'lab'
            if step == 3:
                return 'sibb'
            if step == 4:
                return 'dob'
            if step == 5:
                return 'reb'
            if step == 6:
                return 'mibb'
            if step == 7 or step == 0:
                return 'fab'
        if tonal == 'g' or tonal == 'sol-moll' or tonal == 'g-moll':
            if step == 1:
                return 'sol'
            if step == 2:
                return 'la'
            if step == 3:
                return 'sib'
            if step == 4:
                return 'do'
            if step == 5:
                return 're'
            if step == 6:
                return 'mib'
            if step == 7 or step == 0:
                return 'fa'
        if tonal == 'g#' or tonal == 'sol#-moll' or tonal == 'gis-moll' or tonal == 'gis':
            if step == 1:
                return 'sol#'
            if step == 2:
                return 'la#'
            if step == 3:
                return 'si'
            if step == 4:
                return 'do#'
            if step == 5:
                return 're#'
            if step == 6:
                return 'mi'
            if step == 7 or step == 0:
                return 'fa#'
        if tonal == 'ab' or tonal == 'lab-moll' or tonal == 'as-moll' or tonal == 'as':
            if step == 1:
                return 'lab'
            if step == 2:
                return 'sib'
            if step == 3:
                return 'dob'
            if step == 4:
                return 'reb'
            if step == 5:
                return 'mib'
            if step == 6:
                return 'fab'
            if step == 7 or step == 0:
                return 'solb'
        if tonal == 'a' or tonal == 'la-moll' or tonal == 'a-moll':
            if step == 1:
                return 'la'
            if step == 2:
                return 'si'
            if step == 3:
                return 'do'
            if step == 4:
                return 're'
            if step == 5:
                return 'mi'
            if step == 6:
                return 'fa'
            if step == 7 or step == 0:
                return 'sol'
        if tonal == 'a#' or tonal == 'la#-moll' or tonal == 'ais-moll' or tonal == 'ais':
            if step == 1:
                return 'la#'
            if step == 2:
                return 'si#'
            if step == 3:
                return 'do#'
            if step == 4:
                return 're#'
            if step == 5:
                return 'mi#'
            if step == 6:
                return 'fa#'
            if step == 7 or step == 0:
                return 'sol#'
        if tonal == 'b' or tonal == 'sib-moll' or tonal == 'b-moll' or tonal == 'hes':
            if step == 1:
                return 'sib'
            if step == 2:
                return 'do'
            if step == 3:
                return 'reb'
            if step == 4:
                return 'mib'
            if step == 5:
                return 'fa'
            if step == 6:
                return 'solb'
            if step == 7 or step == 0:
                return 'lab'
        if tonal == 'h' or tonal == 'si-moll' or tonal == 'h-moll':
            if step == 1:
                return 'si'
            if step == 2:
                return 'do#'
            if step == 3:
                return 're'
            if step == 4:
                return 'mi'
            if step == 5:
                return 'fa#'
            if step == 6:
                return 'sol'
            if step == 7 or step == 0:
                return 'la'
        if tonal == 'h#' or tonal == 'si#-moll' or tonal == 'his-moll' or tonal == 'his':
            if step == 1:
                return 'si#'
            if step == 2:
                return 'do##'
            if step == 3:
                return 're#'
            if step == 4:
                return 'mi#'
            if step == 5:
                return 'fa##'
            if step == 6:
                return 'sol#'
            if step == 7 or step == 0:
                return 'la#'