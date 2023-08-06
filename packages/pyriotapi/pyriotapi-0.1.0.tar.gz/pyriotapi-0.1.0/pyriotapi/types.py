from enum import Enum


class Region(Enum):
    #Platforms
    BR = 'br1'
    EUN = 'eun1'
    EUW = 'euw1'
    JP = 'jp1'
    KR = 'kr'
    LAS = 'la1'
    LAN = 'la2'
    NA = 'na1'
    OC = 'oc1'
    TR = 'tr1'
    RU = 'ru'
    
    #Regions
    AMERICAS = 'americas'
    ASIA = 'asia'
    EUROPE = 'europe'
    SEA = 'sea'


class Tier(Enum):
    IRON = 'IRON'
    BRONZE = 'BRONZE'
    SILVER = 'SILVER'
    GOLD = 'GOLD'
    PLATINUM = 'PLATINUM'
    DIAMOND = 'DIAMOND'
    MASTER = 'MASTER'
    GRANDMASTER = 'GRANDMASTER'
    CHALLENGER = 'CHALLENGER'


class Division(Enum):
    I = 'I'
    II = 'II'
    III = 'III'
    IV = 'IV'


class Queue(Enum):
    SOLO = 'RANKED_SOLO_5x5'
    FLEX = 'RANKED_FLEX_SR'