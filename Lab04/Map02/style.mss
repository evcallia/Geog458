Map {
  background-color: #dafdee;
}

#cb2014usstate500k {
  line-color: #a11717;
  line-join: round;
  line-comp-op: color-dodge;
  [zoom < 4]{
    line-width: 2;
  }
  [zoom >= 4]{
    line-width: 3;
	}
  polygon-fill: #b66106;
}

#countries {
  ::outline {
    line-color: #0a490;
    line-width: 2;
    line-join: round;
  }
  polygon-fill: #fff;
}


#statemcdonaldscounts [zoom < 4] {
  point-file:url(Data/McD.svg);
  point-allow-overlap:true;
  /*marker-width:6;
  marker-fill:#f45;
  marker-line-color:#eeb92b;
  marker-allow-overlap:true;
  marker-ignore-placement:true;*/
  [zoom = 0]{
    marker-width: .5px;
    point-transform: "scale(.01)";
  }[zoom = 1]{
    marker-width: 2px;
    point-transform: "scale(.03)";
  }[zoom = 2]{
    marker-width: 3px;
    point-transform: "scale(.05)";
  }[zoom = 3]{
    marker-width: 7px;
    point-transform: "scale(0)";
    text-name: [McDonalds Count];
    text-face-name: "Arial Bold";
    text-fill: #ecb521;
    text-size: 10;
    text-allow-overlap:true;
  }
}

#mcdonalds [zoom >= 4]{
  marker-width:6;
  marker-fill:#eeb92b;
  marker-line-color:#eeb92b;
  marker-allow-overlap:true;
  marker-ignore-placement:true;
  [zoom = 4]{
    marker-width: .5px;
  }[zoom = 5]{
    marker-width: 2px;
  }[zoom = 6]{
    marker-width: 3px;
  }[zoom = 7]{
    marker-width: 7px;
  }
}





