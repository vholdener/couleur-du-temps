
var selectedStation = "Uetliberg";
var datum = "";
var zeitperiode = "";

d3.csv("/data/Prognose_all.csv", d3.autoType).then(function (csv) {
    data = csv;
    const d3datum = data.map((d) => d.datum);
    datum = d3datum.slice(0,1);
    const d3zeit = data.map((d) => d.zeitperiode);
    zeitperiode = d3zeit.slice(0,1);
    label();
  });

function label(){
    document.getElementById("zeitperiode").textContent = '\u00AB' + zeitperiode + '\u00BB';
    document.getElementById("datumslabel").textContent = datum;
    document.getElementById("stationslabel").textContent = selectedStation + ",  ";
  }
