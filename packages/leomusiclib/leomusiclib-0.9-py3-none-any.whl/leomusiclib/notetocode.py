# -*- coding: cp1251 -*-
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
         return('Ошибка')
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
         return('Ошибка')
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
         return('Ошибка')
    if c == 5.5:
         return('dob')
    else: return('Ошибка')
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
         return('Ошибка')
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
         return('Ошибка')
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
         return('Ошибка')