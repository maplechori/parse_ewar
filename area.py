#/usr/bin/python3

from pyparsing import *
import pprint
import argparse
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
area_revisions = Suppress(Literal("Revisions")) + Optional(delimitedList(Word(alphas), delim=space))  + tilde
area_vnums = Suppress(Literal("VNUMs")) + delimitedList(Word(nums),delim=space)
area_canquit = Suppress(Literal("NQuit")) + Word(nums)
area_open = Suppress(Literal("Open")) + Word(nums)
area_home = Suppress(Literal("Homeland")) + Word(nums)
area_sczone = Suppress(Literal("SCZone")) + Word(nums)
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


mob_avngr = Suppress(Literal("Avngr")) + Word(nums)
mob_attackname = Suppress(Literal("Attackmsg")) + multi_line_txt + tilde
mob_clanguard_two = Suppress(Literal("AClan2")) + Word(nums) 
mob_clanguard_one = Suppress(Literal("AClan")) + Word(nums) 
mob_actbits = Suppress(Literal("ActBits")) +  Regex("[\-0-9]*")
mob_actbits3 = Suppress(Literal("ActBits3")) +  Regex("[\-0-9]*")
mob_actbits4 = Suppress(Literal("ActBits4")) + Regex("[\-0-9]*") 
mob_actbits5 = Suppress(Literal("ActBits5")) +  Regex("[\-0-9]*")
mob_racehate = Suppress(Literal("RaceHate")) + Regex("[\-0-9]*")
mob_yeller = Suppress(Literal("AYeller")) + Word(nums) 
mob_amax = Suppress(Literal("AMax")) + Word(nums) 
mob_willhelp = Suppress(Literal("AWillhelp")) + Word(nums) 
mob_affectby = Suppress(Literal("Affect_By")) + Regex("[\-0-9]*")
mob_affect2 = Suppress(Literal("AffectTWO")) + Word(nums)
mob_alignment = Suppress(Literal("Alignment")) + Word(nums)
mob_armorclass = Suppress(Literal("ArmorClass")) +  Regex("[\-0-9]*")
mob_hp = Suppress(Literal("Hp")) + Word(nums)
mob_xp = Suppress(Literal("Xp")) + Word(nums)
mob_guard = Suppress(Literal("Guard")) + Word(nums)
mob_type = Suppress(Literal("MobType")) + Word(nums)
mob_altv = Suppress(Literal("Alt_vnum")) + Word(nums)
mob_sex = Suppress(Literal("Sex")) + Word(nums)
mob_level = Suppress(Literal("Level")) + Word(nums)
mob_nheight = Suppress(Literal("NHeight")) + Word(nums)
mob_money = Suppress(Literal("Money")) + Word(nums)
mob_spec = Suppress(Literal("Spec")) + Regex(".*")
mob_warrior = Suppress(Literal("BWarrior_P")) + Word(nums)
mob_bcast = Suppress(Literal("BCast_P")) + Word(nums)
mob_bcasts = Suppress(Literal("BCasts")) + Regex("[^~]*") + tilde
mob_shop2 = Suppress(Literal("Shopd2")) + Word(nums)
mob_shop3 = Suppress(Literal("Shopd3")) + Word(nums)
mob_shop = Suppress(Literal("Shop")) + Group(OneOrMore(Word(nums))) 
mob_shopU1 = Suppress(Literal("ShopU1")) + Word(nums)
mob_shopU2 = Suppress(Literal("ShopU2")) + Word(nums)
mob_shopU3 = Suppress(Literal("ShopU3")) + Word(nums)
mob_shopU4 = Suppress(Literal("ShopU4")) + Word(nums)
mob_shopU5 = Suppress(Literal("ShopU5")) + Word(nums)
mob_shopU6 = Suppress(Literal("ShopU6")) + Word(nums)
mob_shopU7 = Suppress(Literal("ShopU7")) + Word(nums)
mob_shopU8 = Suppress(Literal("ShopU8")) + Word(nums)
mob_shopU9 = Suppress(Literal("ShopU9")) + Word(nums)
mob_shopU10 = Suppress(Literal("ShopU10")) + Word(nums)
mob_shopCS = Suppress(Literal("ShopCS")) + short_txt + tilde
mob_shopcr = Suppress(Literal("ShopCr")) + Word(nums)
mob_shcrh = Suppress(Literal("ShCrh")) + Word(nums)
mob_timer = Suppress(Literal("Timer")) + Word(nums)
mob_smns = Suppress(Literal("Smns")) + Word(nums)
mob_askltaught = Suppress(Literal("ASklTaught")) + Group(OneOrMore(Word(nums)))
mob_ghit = Suppress(Literal("GHitR")) + Word(nums)
mob_gdamr = Suppress(Literal("GDamR")) + Word("-" + nums)
mob_gdod = Suppress(Literal("GDod")) + Word(nums)
mob_gpar = Suppress(Literal("GPar")) + Word(nums)

mob_options =   Group(
                Optional(mob_description.setResultsName("description")) &\
                Optional(mob_avngr) &\
                Optional(mob_amax) & \
                Optional(mob_altv) &\
                Optional(mob_nheight) & \
                Optional(mob_actbits3) &  \
                Optional(mob_actbits4) &\
                Optional(mob_actbits5) & \
                Optional(mob_actbits) &  \
                Optional(mob_armorclass) &\
                Optional(mob_racehate) &\
                Optional(mob_shopcr) &\
                Optional(mob_affectby) &\
                Optional(mob_affect2) &\
                Optional(mob_shcrh) &\
                Optional(mob_ghit) &\
                Optional(mob_gdamr) &\
                Optional(mob_gdod) &\
                Optional(mob_gpar) &\
                Optional(mob_money) &\
                Optional(mob_timer) &\
                Optional(mob_spec) &\
                Optional(mob_warrior) &\
                Optional(mob_attackname) & \
                Optional(mob_clanguard_two) &\
                Optional(mob_clanguard_one) & \
                Optional(mob_yeller) & \
                Optional(mob_level) &\
                Optional(mob_smns) &\
                Optional(mob_amax) &  \
                Optional(mob_willhelp) &\
                Optional(mob_hp) & \
                Optional(mob_xp) & \
                ZeroOrMore(mob_askltaught) &\
                Optional(mob_guard) & \
                Optional(mob_type) & \
                Optional(mob_sex) & \
                Optional(mob_alignment) &\
                ZeroOrMore(mob_bcasts) &\
                Optional(mob_bcast) &\
                Optional(mob_shop2) &\
                Optional(mob_shop3) &\
                Optional(mob_shop) &\
                Optional(mob_shopU1) &\
                Optional(mob_shopU2) &\
                Optional(mob_shopU3) &\
                Optional(mob_shopU4) &\
                Optional(mob_shopU5) &\
                Optional(mob_shopU6) &\
                Optional(mob_shopU7) &\
                Optional(mob_shopU8) &\
                Optional(mob_shopU9) &\
                Optional(mob_shopU10) &\
                Optional(mob_shopCS))

mob_default = mob_vnum.setParseAction(tokenMap(int)) + Group(mob_name.setResultsName('name') + mob_short + mob_long & Group(mob_options)) + end 

mob_parser = Suppress(Literal("#MOBDATA")) + ZeroOrMore(mob_default) + Suppress(Literal("#0"))

obj_vnum = Suppress(Literal("#")) + Word(nums)
obj_name = Suppress(Literal("Name")) + Regex("[^~]*") + tilde
obj_short = Suppress(Literal("Short")) + Regex("[^~]*", flags=re.MULTILINE) + tilde
obj_description = Suppress(Literal("Descr")) + Regex("[^~]*", flags=re.MULTILINE) + tilde
obj_type = Suppress(Literal("Type")) + Word(nums)

obj_extra = Suppress(Literal("Extra")) + Word("-" + nums)
obj_extra2 = Suppress(Literal("Extra2")) + Word(nums)
obj_oracenum = Suppress(Literal("Oracenum")) + Word(nums)
obj_wear = Suppress(Literal("Wear")) + Word("-" + nums)
obj_weight = Suppress(Literal("Weight")) + Word(nums)
obj_cost = Suppress(Literal("Cost")) + Word(nums)
obj_shardcost = Suppress(Literal("Shardcost")) + Word(nums)
obj_usespell = Suppress(Literal("Usespell")) + Word(nums)
obj_extradescr = Suppress(Literal("ExtraDescr")) + Regex("[^~]*",flags=re.MULTILINE) + tilde + Regex("[^~]*", flags=re.MULTILINE) + tilde
obj_timer = Suppress(Literal("Timer")) + Word(nums)
obj_usespell = Suppress(Literal("Usespell")) + Word(nums)
obj_recharge = Suppress(Literal("Recharge")) + Word(nums)
obj_orace = Suppress(Literal("Orace")) + Word("-" + nums)
obj_maxinroom = Suppress(Literal("Maxinroom")) + Word(nums)
obj_maxinworld = Suppress(Literal("Maxinworld")) + Word(nums)
obj_affect = Suppress(Literal("Affect")) + OneOrMore(Word("-"+nums))
obj_values = Suppress(Literal("Values")) + OneOrMore(Word("-"+nums))

obj_options = Optional(obj_type) &\
              Optional(obj_extra2) &\
              Optional(obj_extra) &\
              Optional(obj_oracenum) &\
              Optional(obj_orace) &\
              Optional(obj_wear) &\
              Optional(obj_weight) &\
              Optional(obj_usespell) &\
              Optional(obj_recharge) &\
              Optional(obj_cost) &\
              Optional(obj_timer) &\
              Optional(obj_maxinworld) &\
              Optional(obj_maxinroom) &\
              Optional(obj_shardcost) &\
              ZeroOrMore(obj_affect) &\
              Optional(obj_values) &\
              Optional(obj_usespell) &\
              ZeroOrMore(obj_extradescr)

obj_default = obj_vnum.setParseAction(tokenMap(int)) + Group(obj_name + obj_short + obj_description & Group(obj_options)) + end

obj_parser = Suppress(Literal("#OBJDATA")) + ZeroOrMore(Group(obj_default)) + Suppress(Literal("#0"))


room_vnum = Suppress(Literal("#")) + Word(nums).setParseAction(tokenMap(int))
room_name = Suppress(Literal("Name")) + Regex("[^~]*") + tilde
room_description = Suppress(Literal("Descr")) + Regex("[^~]*") + tilde
room_movedir = Suppress(Literal("Move_dir")) + Word(nums)
room_extradescription =  Suppress(Literal("ExtraDescr")) + Regex("[^~]*",flags=re.MULTILINE) + tilde + Regex("[^~]*", flags=re.MULTILINE) + tilde
room_movemess = Suppress(Literal("Movemess")) + multi_line_txt + tilde
room_flags = Suppress(Literal("Flags")) + Word("-"+nums)
room_flags2 = Suppress(Literal("Flags2")) + Word("-"+nums)
room_sector = Suppress(Literal("Sector")) + Word(nums).setParseAction(tokenMap(int))
desc_door = Optional(Regex("[^~]*")) + tilde + Optional(Regex("[^~]*")) +  tilde
room_door = Suppress(Literal("Door")) + Word(nums).setParseAction(tokenMap(int))\
        + Word(nums).setParseAction(tokenMap(int)) + Word(nums).setParseAction(tokenMap(int))\
        + Word(nums).setParseAction(tokenMap(int)) + Word(nums).setParseAction(tokenMap(int))\
        + Word(nums).setParseAction(tokenMap(int))  + Suppress(newline) + Group(desc_door)
room_ascii = Suppress(Literal("Ascii")) + Regex(".*")
room_color = Suppress(Literal("Color")) + Word(nums)

#numeric = Optional(Literal("-")) +
numeric = Word("-" + nums)

room_reset = Suppress(Literal("Reset")) + Word(alphas) + numeric.setParseAction(tokenMap(int)) + numeric.setParseAction(tokenMap(int))\
        + numeric.setParseAction(tokenMap(int))

room_options = Optional(room_name.setResultsName('name')) &\
               Optional(room_flags2.setResultsName('flags2*')) &\
               Optional(room_flags.setResultsName('flags*')) &\
               Optional(room_sector.setResultsName('sector')) &\
               Optional(room_description.setResultsName('description')) &\
               ZeroOrMore(room_reset.setResultsName('reset*')) &\
               Optional(room_movedir.setResultsName('movedir')) &\
               Optional(room_ascii.setResultsName('ascii')) &\
               Optional(room_color.setResultsName('color')) &\
               Optional(room_movemess.setResultsName('movemessage')) &\
               ZeroOrMore(room_extradescription.setResultsName('extradescription*')) &\
               ZeroOrMore(room_door.setResultsName("doors*"))


room_default = Group(room_vnum.setResultsName("vnum*") + room_options) + end

room_parser = Suppress(Literal("#ROOMDATA")) + ZeroOrMore(room_default) + Suppress(Literal("#0"))

area_parser = area_start + area_name  + area_repop + Optional(area_repop_rate) + Optional(area_sczone) + Optional(area_clan_zone) + area_builders + area_revisions + area_vnums\
            + area_canquit + area_open + area_home + Optional(area_quest_exempt) + Optional(area_approval) + Optional(area_event_exempt) + end 

area_parser = Group(area_parser).setResultsName("area") + Group(mob_parser).setResultsName("mobs") +\
        Group(obj_parser).setResultsName("objects") + Group(room_parser).setResultsName("rooms") + Suppress(ending)


rooms_dict = {}


def main():
    parser = argparse.ArgumentParser(description='process everwar area file')
    parser.add_argument('area', type=str)

    args = parser.parse_args()


    with open(args.area) as f:
       input_string = f.read()
 
    try:
       result =  area_parser.parseString(input_string, parseAll=True)

       rr = result.asDict()
       for i in rr['rooms']:
           vnum = i['vnum'][0][0]

           if 'sector' in i:
               rooms_dict[vnum] = {'sector' : i['sector'][0] }
           else:
               rooms_dict[vnum] = {'sector' : 0 }

           if 'doors' in i:
               print(i['doors'])

       rp = pprint.PrettyPrinter(indent=4)
       rp.pprint(rr)

    except ParseException as pe:
       print(pe.markInputline())
       print(pe)

if __name__ == "__main__":
    main()
