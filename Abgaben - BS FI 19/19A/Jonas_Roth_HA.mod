<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<project source="2.7.1" version="1.0">
This file is intended to be loaded by Logisim (http://www.cburch.com/logisim/).
<lib desc="#Wiring" name="0"/>
  <lib desc="#Gates" name="1"/>
  <lib desc="#Plexers" name="2"/>
  <lib desc="#Arithmetic" name="3"/>
  <lib desc="#Memory" name="4"/>
  <lib desc="#I/O" name="5"/>
  <lib desc="#Base" name="6">
    <tool name="Text Tool">
      <a name="text" val=""/>
      <a name="font" val="SansSerif plain 12"/>
      <a name="halign" val="center"/>
      <a name="valign" val="base"/>
    </tool>
  </lib>
  <main name="main"/>
  <options>
    <a name="gateUndefined" val="ignore"/>
    <a name="simlimit" val="1000"/>
    <a name="simrand" val="0"/>
  </options>
  <mappings>
    <tool lib="6" map="Button2" name="Menu Tool"/>
    <tool lib="6" map="Button3" name="Menu Tool"/>
    <tool lib="6" map="Ctrl Button1" name="Menu Tool"/>
  </mappings>
  <toolbar>
    <tool lib="6" name="Poke Tool"/>
    <tool lib="6" name="Edit Tool"/>
    <tool lib="6" name="Text Tool">
      <a name="text" val=""/>
      <a name="font" val="SansSerif plain 12"/>
      <a name="halign" val="center"/>
      <a name="valign" val="base"/>
    </tool>
    <sep/>
    <tool lib="0" name="Pin">
      <a name="tristate" val="false"/>
    </tool>
    <tool lib="0" name="Pin">
      <a name="facing" val="west"/>
      <a name="output" val="true"/>
      <a name="labelloc" val="east"/>
    </tool>
    <tool lib="1" name="NOT Gate"/>
    <tool lib="1" name="AND Gate"/>
    <tool lib="1" name="OR Gate"/>
  </toolbar>
  <circuit name="main">
    <a name="circuit" val="main"/>
    <a name="clabel" val=""/>
    <a name="clabelup" val="east"/>
    <a name="clabelfont" val="SansSerif plain 12"/>
  </circuit>
  <circuit name="Halbaddierer">
    <a name="circuit" val="Halbaddierer"/>
    <a name="clabel" val=""/>
    <a name="clabelup" val="east"/>
    <a name="clabelfont" val="SansSerif plain 12"/>
    <wire from="(390,190)" to="(420,190)"/>
    <wire from="(280,120)" to="(300,120)"/>
    <wire from="(390,170)" to="(410,170)"/>
    <wire from="(410,140)" to="(430,140)"/>
    <wire from="(300,90)" to="(300,100)"/>
    <wire from="(300,100)" to="(300,120)"/>
    <wire from="(390,170)" to="(390,190)"/>
    <wire from="(220,90)" to="(300,90)"/>
    <wire from="(280,170)" to="(390,170)"/>
    <wire from="(410,140)" to="(410,170)"/>
    <wire from="(480,120)" to="(610,120)"/>
    <wire from="(480,210)" to="(610,210)"/>
    <wire from="(300,100)" to="(430,100)"/>
    <wire from="(220,90)" to="(220,210)"/>
    <wire from="(220,210)" to="(420,210)"/>
    <comp lib="5" loc="(610,210)" name="LED"/>
    <comp lib="0" loc="(280,120)" name="Pin">
      <a name="tristate" val="false"/>
    </comp>
    <comp lib="1" loc="(480,120)" name="AND Gate"/>
    <comp lib="0" loc="(280,170)" name="Pin">
      <a name="tristate" val="false"/>
    </comp>
    <comp lib="1" loc="(480,210)" name="XOR Gate"/>
    <comp lib="5" loc="(610,120)" name="LED"/>
  </circuit>
</project>
