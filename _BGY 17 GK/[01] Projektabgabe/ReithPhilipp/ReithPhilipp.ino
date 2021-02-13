/*
Der Arduino erkennt den Wechsel von Null auf Eins sofort, beim Wechsel von Eins auf Null ist eine circa fünfsekündige Verzögerung vorhanden.
Wenn ich den Knopf nichte, dann bekomme ich durchs Drücken eine Null und durchs Loslassen eine Eins.
Der Timer soll also durch eine Null (Knopf gedrückt) resettet werden, und die Eins (Knopf loslassen), die am Arduino sofort erkannt wird, dient zum Starten.
Gestoppt wird durch das Drücken des zweiten Knopfes.
Das ganze hat sich nun geändert, da ich mit Herr Kothe die Schaltung optimiert habe. Nun wird sowohl das Drücken, als auch das Loslassen sofort erkannt.
Um nun den Unterschied zwischen Knopf Drücken und Knopf Loslassen festzustellen, registriere ich einen ehemaligen Zustand (estar und estop), der am Ende
jeden loops den Knopfzustand übernimmt. So kann ich beim nächsten Durchlauf überprüfen, ob der Knop gedrückt (Wechsel von 0 auf 1) oder
losgelassen (Wechsel von 1 auf 0) wird.Damit ermögliche ich das Starten der Stoppuhr mit dem Loslassen des Startknopfes und das Stoppen mit dem
Drüccken des Stoppknopfes.

Als Quelle wurde nur https://playground.arduino.cc/Code/Stopwatch/ verwendet. Der Rest kam aus meinem Hirn.


*/
int startpin=3;
int stopppin=6;

void setup() {
  Serial.begin(9600);       //Serieller Monitor zur Ausgabe
  pinMode(startpin,INPUT);  
  pinMode(stopppin,INPUT);
}

int start=0;//Knopfzustand
int stopp=0;
int estop=0;//letzter Knopfzustand
int estar=1;

int startsekunde=0;//Variablen für die Zeitnahme
int stoppsekunde=0;
int zeit=0;
int wdhs=0;

void loop() {
  
  start=digitalRead(startpin);
  stopp=digitalRead(stopppin);
  
  if (start==0 && estar==1){//speichern der Startzeit
    startsekunde = millis();
  }
  if (stopp==1 && estop==0){//speichern der Stoppzeit
    stoppsekunde = millis();
  }
  
  zeit=(stoppsekunde-startsekunde);//Setzen der Zeit
  
  if (stopp==1 && start==1 or start==1){//reset
    zeit=0;
    }
  
  estop=stopp;
  estar=start;
  
  //Ausgabe:
  
/*  Serial.print(start);
  Serial.print("  ");
  Serial.print(stopp);
  Serial.print("  ");
  Serial.print(startsekunde);
  Serial.print("  ");
  Serial.println(stoppsekunde);
*/  Serial.print(" Zeit zwischen Loslassen Startknopf und  Drücken Stoppknopf: ");
  Serial.print(zeit);
  Serial.println("");

}
