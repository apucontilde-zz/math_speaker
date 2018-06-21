
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIF FRAC FUNCION INFINITY INT LIMIT LLAVD LLAVI MON NUM OPERBI RAIZ REDD REDI SUB SUM SUP TOalll : allall : limitall : integralall : fractionall : rootall : monomiall yall : NUMall : MONall : FUNCIONall : REDI all xx : OPERBI all xx : REDD yy : expy : exp : SUP LLAVI all LLAVDmonomiall : monomial monomiallmonomiall : monomialmonomial : MON NUMmonomial : NUM MONfraction : FRAC LLAVI all LLAVD LLAVI all LLAVDroot : RAIZ LLAVI all LLAVDintegral : INT all DIF MONintegral : INT SUB LLAVI all LLAVD SUP LLAVI all LLAVD all DIF MONintegral : SUM SUB LLAVI all LLAVD SUP LLAVI all LLAVD alllimit : LIMIT SUB LLAVI MON TO INFINITY LLAVD alllimit : LIMIT SUB LLAVI MON TO MON LLAVD alllimit : LIMIT SUB LLAVI MON TO NUM LLAVD all'
    
_lr_action_items = {'NUM':([0,9,11,13,17,21,22,28,29,31,33,35,39,40,54,57,64,65,66,67,68,75,76,],[8,22,8,8,32,-19,-18,8,8,22,8,8,8,8,60,8,8,8,8,8,8,8,8,]),'MON':([0,8,11,13,17,21,22,28,29,32,33,35,37,38,39,40,54,57,64,65,66,67,68,75,76,79,],[9,21,9,9,31,-19,-18,9,9,21,9,9,46,47,9,9,58,9,9,9,9,9,9,9,9,80,]),'FUNCION':([0,11,13,28,29,33,35,39,40,57,64,65,66,67,68,75,76,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'REDI':([0,11,13,28,29,33,35,39,40,57,64,65,66,67,68,75,76,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'LIMIT':([0,11,13,28,29,33,35,39,40,57,64,65,66,67,68,75,76,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'INT':([0,11,13,28,29,33,35,39,40,57,64,65,66,67,68,75,76,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'SUM':([0,11,13,28,29,33,35,39,40,57,64,65,66,67,68,75,76,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'FRAC':([0,11,13,28,29,33,35,39,40,57,64,65,66,67,68,75,76,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'RAIZ':([0,11,13,28,29,33,35,39,40,57,64,65,66,67,68,75,76,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'$end':([1,2,3,4,5,6,7,8,9,10,17,18,19,21,22,30,34,36,45,47,51,52,53,69,70,71,72,78,80,],[0,-1,-2,-3,-4,-5,-14,-7,-8,-9,-17,-6,-13,-19,-18,-16,-10,-14,-12,-22,-21,-15,-11,-20,-26,-25,-27,-24,-23,]),'OPERBI':([3,4,5,6,7,8,9,10,17,18,19,21,22,23,30,34,36,44,45,47,51,52,53,69,70,71,72,78,80,],[-2,-3,-4,-5,-14,-7,-8,-9,-17,-6,-13,-19,-18,35,-16,-10,-14,35,-12,-22,-21,-15,-11,-20,-26,-25,-27,-24,-23,]),'REDD':([3,4,5,6,7,8,9,10,17,18,19,21,22,23,30,34,36,44,45,47,51,52,53,69,70,71,72,78,80,],[-2,-3,-4,-5,-14,-7,-8,-9,-17,-6,-13,-19,-18,36,-16,-10,-14,36,-12,-22,-21,-15,-11,-20,-26,-25,-27,-24,-23,]),'DIF':([3,4,5,6,7,8,9,10,17,18,19,21,22,25,30,34,36,45,47,51,52,53,69,70,71,72,77,78,80,],[-2,-3,-4,-5,-14,-7,-8,-9,-17,-6,-13,-19,-18,38,-16,-10,-14,-12,-22,-21,-15,-11,-20,-26,-25,-27,79,-24,-23,]),'LLAVD':([3,4,5,6,7,8,9,10,17,18,19,21,22,30,34,36,41,42,43,45,47,48,49,51,52,53,58,59,60,63,69,70,71,72,73,74,78,80,],[-2,-3,-4,-5,-14,-7,-8,-9,-17,-6,-13,-19,-18,-16,-10,-14,50,51,52,-12,-22,55,56,-21,-15,-11,64,65,66,69,-20,-26,-25,-27,75,76,-24,-23,]),'SUP':([7,17,21,22,30,36,55,56,],[20,-17,-19,-18,-16,20,61,62,]),'SUB':([12,13,14,],[24,26,27,]),'LLAVI':([15,16,20,24,26,27,50,61,62,],[28,29,33,37,39,40,57,67,68,]),'TO':([46,],[54,]),'INFINITY':([54,],[59,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'alll':([0,],[1,]),'all':([0,11,13,28,29,33,35,39,40,57,64,65,66,67,68,75,76,],[2,23,25,41,42,43,44,48,49,63,70,71,72,73,74,77,78,]),'limit':([0,11,13,28,29,33,35,39,40,57,64,65,66,67,68,75,76,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'integral':([0,11,13,28,29,33,35,39,40,57,64,65,66,67,68,75,76,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'fraction':([0,11,13,28,29,33,35,39,40,57,64,65,66,67,68,75,76,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'root':([0,11,13,28,29,33,35,39,40,57,64,65,66,67,68,75,76,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'monomiall':([0,11,13,17,28,29,33,35,39,40,57,64,65,66,67,68,75,76,],[7,7,7,30,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'monomial':([0,11,13,17,28,29,33,35,39,40,57,64,65,66,67,68,75,76,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'y':([7,36,],[18,45,]),'exp':([7,36,],[19,19,]),'x':([23,44,],[34,53,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> alll","S'",1,None,None,None),
  ('alll -> all','alll',1,'p_alll','math_speaker.py',284),
  ('all -> limit','all',1,'p_all1','math_speaker.py',305),
  ('all -> integral','all',1,'p_all2','math_speaker.py',309),
  ('all -> fraction','all',1,'p_all3','math_speaker.py',313),
  ('all -> root','all',1,'p_all4','math_speaker.py',317),
  ('all -> monomiall y','all',2,'p_all5','math_speaker.py',321),
  ('all -> NUM','all',1,'p_all51','math_speaker.py',328),
  ('all -> MON','all',1,'p_all52','math_speaker.py',331),
  ('all -> FUNCION','all',1,'p_all6','math_speaker.py',335),
  ('all -> REDI all x','all',3,'p_all7','math_speaker.py',339),
  ('x -> OPERBI all x','x',3,'p_x','math_speaker.py',342),
  ('x -> REDD y','x',2,'p_x2','math_speaker.py',345),
  ('y -> exp','y',1,'p_y','math_speaker.py',351),
  ('y -> <empty>','y',0,'p_y2','math_speaker.py',354),
  ('exp -> SUP LLAVI all LLAVD','exp',4,'p_exp','math_speaker.py',357),
  ('monomiall -> monomial monomiall','monomiall',2,'p_monomiall','math_speaker.py',361),
  ('monomiall -> monomial','monomiall',1,'p_monomiall1','math_speaker.py',365),
  ('monomial -> MON NUM','monomial',2,'p_monomial','math_speaker.py',369),
  ('monomial -> NUM MON','monomial',2,'p_monomial1','math_speaker.py',373),
  ('fraction -> FRAC LLAVI all LLAVD LLAVI all LLAVD','fraction',7,'p_fraction','math_speaker.py',377),
  ('root -> RAIZ LLAVI all LLAVD','root',4,'p_root','math_speaker.py',381),
  ('integral -> INT all DIF MON','integral',4,'p_integral','math_speaker.py',385),
  ('integral -> INT SUB LLAVI all LLAVD SUP LLAVI all LLAVD all DIF MON','integral',12,'p_integral2','math_speaker.py',389),
  ('integral -> SUM SUB LLAVI all LLAVD SUP LLAVI all LLAVD all','integral',10,'p_sum','math_speaker.py',393),
  ('limit -> LIMIT SUB LLAVI MON TO INFINITY LLAVD all','limit',8,'p_limit','math_speaker.py',397),
  ('limit -> LIMIT SUB LLAVI MON TO MON LLAVD all','limit',8,'p_limit1','math_speaker.py',401),
  ('limit -> LIMIT SUB LLAVI MON TO NUM LLAVD all','limit',8,'p_limit2','math_speaker.py',405),
]
