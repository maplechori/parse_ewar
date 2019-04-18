#/usr/bin/python3

from pyparsing import *
import re

tilde = Suppress(Literal("~"))
areadata = "#AREADATA"
end = "End"
ending = "#$"
space=White(' ',exact=1)
newline=White('\n',exact=1)

area_start = Suppress(Literal(areadata))
area_name = Suppress(Literal("Name")) + Regex("[^~]*") + tilde
area_repop = Suppress(Literal("Repop")) + Regex("[^~]*", flags=re.MULTILINE) + tilde
area_repop_rate = Suppress(Literal("SRepop")) + Word(nums)
area_clan_zone = Suppress(Literal("SCZone")) + Word(nums)
area_builders = Suppress(Literal("Builders")) + delimitedList(Word(alphas), delim=space) + tilde
area_revisions = Suppress(Literal("Revisions")) + delimitedList(Word(alphas), delim=space)  + tilde
area_vnums = Suppress(Literal("VNUMs")) + delimitedList(Word(nums),delim=space)
area_canquit = Suppress(Literal("NQuit")) + Word(nums)
area_open = Suppress(Literal("Open")) + Word(nums)
area_home = Suppress(Literal("Homeland")) + Word(nums)
area_quest_exempt = Suppress(Literal("QuestExempt")) + Word(nums)
area_approval = Suppress(Literal('Approval')) + Word(nums)
area_event_exempt = Suppress(Literal('EventExempt')) + Word(nums)
end = Suppress(Literal(end))

mob_data = "#MOBDATA"
mob_start = Suppress(Literal(mob_data)) 

multi_line_txt = Regex("[^~]*", flags=re.MULTILINE)
short_txt = Regex("[^~]*")

mob_vnum = Suppress(Literal("#")) + Word(nums)
mob_name = Suppress(Literal("Name")) + short_txt  + tilde
mob_short = Suppress(Literal("Short")) + short_txt + tilde
mob_long = Suppress(Literal("Long")) + multi_line_txt  + tilde
mob_description = Suppress(Literal("Descr")) + multi_line_txt + tilde

mob_attackname = Suppress(Literal("Attackmsg")) + multi_line_txt + tilde
mob_clanguard_two = Suppress(Literal("AClan2")) + Word(nums) 
mob_clanguard_one = Suppress(Literal("AClan")) + Word(nums) 
mob_actbits = Suppress(Literal("ActBits")) + Word(nums) 
mob_actbits3 = Suppress(Literal("ActBits3")) + Word(nums) 
mob_actbits5 = Suppress(Literal("ActBits5")) + Word(nums)
mob_yeller = Suppress(Literal("AYeller")) + Word(nums) 
mob_amax = Suppress(Literal("AMax")) + Word(nums) 
mob_willhelp = Suppress(Literal("AWillHelp")) + Word(nums) 
mob_actbits4 = Suppress(Literal("ActBits4")) + Word(nums)  
mob_affectby = Suppress(Literal("Affect_By")) + Word(nums) 
mob_affect2 = Suppress(Literal("AffectTWO")) + Word(nums)
mob_alignment = Suppress(Literal("Alignment")) + Word(nums)

mob_hp = Suppress(Literal("Hp")) + Word(nums)
mob_xp = Suppress(Literal("Xp")) + Word(nums)
mob_guard = Suppress(Literal("Guard")) + Word(nums)
mob_type = Suppress(Literal("MobType")) + Word(nums)
mob_sex = Suppress(Literal("Sex")) + Word(nums)
mob_level = Suppress(Literal("Level")) + Word(nums)
mob_nheight = Suppress(Literal("NHeight")) + Word(nums)
mob_money = Suppress(Literal("Money")) + Word(nums)
mob_spec = Suppress(Literal("Spec")) + Regex("[^\s]*")
mob_warrior = Suppress(Literal("BWarrior_P")) + Word(nums)
mob_bcast = Suppress(Literal("BCast_P")) + Word(nums)
mob_bcasts = Suppress(Literal("BCasts")) + Regex("[^~]*") + tilde
mob_shop2 = Suppress(Literal("Shopd2")) + Word(nums)
mob_shop3 = Suppress(Literal("Shopd3")) + Word(nums)
mob_shop = Suppress(Literal("Shop")) + Group(OneOrMore(Word(nums))) 
mob_shopU1 = Suppress(Literal("ShopU1")) + Word(nums)
mob_askltaught = Suppress(Literal("ASklTaught")) + Group(OneOrMore(Word(nums)))
mob_options =   Optional(mob_description) &\
                Optional(mob_amax) & \
                Optional(mob_money) &\
                Optional(mob_spec) &\
                Optional(mob_warrior) &\
                Optional(mob_attackname) & \
                Optional(mob_clanguard_two) &\
                Optional(mob_clanguard_one) & \
                Optional(mob_actbits) &  \
                Optional(mob_actbits3) &  \
                Optional(mob_actbits5) & \
                Optional(mob_yeller) & \
                Optional(mob_amax) &  \
                Optional(mob_willhelp) &\
                Optional(mob_actbits4) &\
                Optional(mob_affectby) &\
                Optional(mob_affect2) &\
                Optional(mob_nheight) & \
                Optional(mob_hp) & \
                Optional(mob_xp) & \
                Optional(mob_askltaught) &\
                Optional(mob_guard) & \
                Optional(mob_type) & \
                Optional(mob_sex) & \
                Optional(mob_alignment) &\
                Optional(ZeroOrMore(mob_bcasts)) &\
                Optional(mob_bcast) &\
                Optional(mob_shop2) &\
                Optional(mob_shop3) &\
                Optional(mob_shop) &\
                Optional(mob_shopU1) &\
                Optional(mob_level) 

mob_default = mob_vnum + Group(mob_name + mob_short + mob_long & Group(mob_options)) + end 

mob_parser = Literal("#MOBDATA") + ZeroOrMore(mob_default) + Literal("#0")

obj_vnum = Suppress(Literal("#")) + Word(nums)
obj_name = Suppress(Literal("Name")) + Regex("[^~]*") + tilde
obj_short = Suppress(Literal("Short")) + Regex("[^~]*", flags=re.MULTILINE) + tilde
obj_description = Suppress(Literal("Descr")) + Regex("[^~]*", flags=re.MULTILINE) + tilde
obj_type = Suppress(Literal("Type")) + Word(nums)

obj_extra = Suppress(Literal("Extra")) + Word(nums)
obj_wear = Suppress(Literal("Wear")) + Word(nums)
obj_weight = Suppress(Literal("Weight")) + Word(nums)
obj_cost = Suppress(Literal("Cost")) + Word(nums)
obj_shardcost = Suppress(Literal("Shardcost")) + Word(nums)
obj_usespell = Suppress(Literal("Usespell")) + Word(nums)
obj_extradescr = Suppress(Literal("ExtraDescr")) + Regex("[^~]*",flags=re.MULTILINE) + tilde + Regex("[^~]*", flags=re.MULTILINE) + tilde

obj_affect = Suppress(Literal("Affect")) + OneOrMore(Word(nums))
obj_values = Suppress(Literal("Values")) + OneOrMore(Word(nums))

obj_options = Optional(obj_type) &\
              Optional(obj_extra) &\
              Optional(obj_wear) &\
              Optional(obj_weight) &\
              Optional(obj_cost) &\
              Optional(obj_shardcost) &\
              Optional(ZeroOrMore(obj_affect)) &\
              Optional(obj_values) &\
              Optional(obj_usespell) &\
              Optional(obj_extradescr)

obj_default = obj_vnum + Group(obj_name + obj_short + obj_description & Group(obj_options)) + end

obj_parser = Literal("#OBJDATA") + OneOrMore(Group(obj_default)) + Literal("#0")


room_vnum = Suppress(Literal("#")) + Word(nums)
room_name = Suppress(Literal("Name")) + Regex("[^~]*") + tilde
room_description = Suppress(Literal("Descr")) + Regex("[^~]*") + tilde
room_flags = Suppress(Literal("Flags")) + Word(nums)
room_flags2 = Suppress(Literal("Flags2")) + Word(nums)
room_sector = Suppress(Literal("Sector")) + Word(nums)
desc_door = Group(Optional(Regex("[^~]*"))) + tilde + Group(Optional(Regex("[^~]*"))) +  tilde
room_door = Suppress(Literal("Door")) + Word(nums) + Word(nums) + Word(nums) + Word(nums) + Word(nums) + Word(nums) + Suppress(newline) + desc_door

numeric = Optional(Literal("-")) + Word(nums)

room_reset = Suppress(Literal("Reset")) + Word(alphas) + numeric + numeric + numeric

room_options = Optional(room_name) &\
               Optional(room_flags2) &\
               Optional(room_flags) &\
               Optional(room_sector) &\
               Optional(room_description) &\
               ZeroOrMore(room_reset) &\
               ZeroOrMore(Group(room_door).setResultsName("doors")) 


room_default = room_vnum + Group(room_options) + end

room_parser = Literal("#ROOMDATA") + OneOrMore(room_default) + Literal("#0")

area_parser = area_start + area_name  + area_repop + area_repop_rate + area_clan_zone + area_builders + area_revisions + area_vnums\
            + area_canquit + area_open + area_home + area_quest_exempt + area_approval + area_event_exempt + end 

area_parser = Group(area_parser) + Group(mob_parser) + Group(obj_parser) + Group(room_parser) + ending

with open("raven.are") as f:
  input_string = f.read()
 
  try:
    result =  area_parser.parseString(input_string, parseAll=True)
    #print("== area ==")
    #for i,k  in result.area.items():
    #  print(i,k)

    #print("== mobs ==")
    #for i,k in result.mob_list.items():
    #  print(i,k)
    
    print(result.dump())
  except ParseException as pe:
      print(pe.markInputline())
      print(pe) 
