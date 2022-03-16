var data = [];
var selectedStation = "Uetliberg";

d3.csv("/data/Prognose_all.csv", d3.autoType).then(function (csv) {
  data = csv;
  console.log(data);
  render(data);
});

function render(data) {
  console.log("selectedStation", selectedStation);
  const stations = data.map((d) => d.namestn);
  
  const selectedData = data.filter((d) => {
    return d.namestn == selectedStation;
  });
    
  d3.select("#menu")
    .selectAll("a")
    .data(stations)
    .enter()
    .append("a")
    .attr("href", "#")
    .text((d) => d)
    .on("click", function (evt, elt) {
      console.log("click", evt, elt);
      selectedStation = elt;
      render(data);
      label();
    });

  const yScaleNS = d3
    .scalePow() // bis max. 120mm Niederschlag
    .exponent(0.23) // mit Exponent spielen https://observablehq.com/@d3/continuous-scales
    .domain([0, 120])
    .range([0, 32]);

  const yScaleSUN = d3
    .scaleLinear()
    .domain([0, 21000]) // bis 21'000sec Sonnenscheindauer
    .range([0, 23]);

  const container = d3
    .select("svg")
    .attr("viewBox", "0 0 100 100")
    .attr("width", 0.5 * window.innerWidth)
    .attr("height", 0.4 * window.innerWidth)
    .classed("leinwand", true);

  // hier entferne ich alle bilder die vorher gezeichnet werden,
  // damit die elemente weiter unten neu gesetzt werden mit den neuen daten
  container.selectAll("*").remove();

  console.log("selectedData", selectedData);

    // Hintergrund
  const Hintergrund = container
    .selectAll(".zeit")
    .data(selectedData)
    .enter()
    .append("image")
    .classed("zeit", true)
    .attr("width", 100)
    .attr("height", 100)
    .attr("x", 0)
    .attr("y", 0)
    .attr("href", (d) => {
      const date = new Date(d.time);
      const hours = date.getHours();
      if (hours >= 0 && hours < 6) {
        return "imgs/lanuit.png";
      }
      else if (hours >= 6 && hours < 12) {
        return "imgs/lamattinee.png";
      }
      else if (hours >= 12 && hours < 18) {
        return "imgs/lapresmidi.png";
      }
      else return "imgs/lasoiree.png";
    });

  // Sonne
  const barsSUN = container
    .selectAll(".barSUN")
    .data(selectedData)
    .enter()
    .append("image")
    .classed("barSUN", true)
    .attr("width", 96)
    .attr("height", (d) => {
      console.log("d", d)
      return yScaleSUN(d.sonne);
    })
    .attr("x", 2)
    .attr("y", 34)
    .attr("preserveAspectRatio", "none")
    .attr("href", "imgs/Sonne.png");

  // Niederschlag am unteren Rand des Bildes positionieren
  const barsNS = container
    .selectAll(".barNS")
    .data(selectedData)
    .enter()
    .append("image")
    .classed("barNS", true)
    .attr("width", 96)
    .attr("height", (d) => {
      return yScaleNS(d.niederschlag);
    })
    .attr("x", 2)
    .attr("y", (d) => {
      return 95  - yScaleNS(d.niederschlag);
    })
    .attr("preserveAspectRatio", "none")
    .attr("href", "imgs/Regen.png");

  // tempdiff
  // hier aendert nur die Bildquelle aufgrund des 'tempdiff'-Wertes.
  // Groesse des Bildes bleibt fix
  const barstempdiff = container
    .selectAll(".barTEMP")
    .data(selectedData)
    .enter()
    .append("image")
    .classed("barTEMP", true)
    .attr("width", 96)
    .attr("height", 23)
    .attr("x", 2)
    .attr("y", 5)
    .attr("preserveAspectRatio", "none")
    .attr("href", (d) => {
      const temp = d.tempdiff;
      if (temp < 3 && temp > -3) {
        return "imgs/Temp_equal.png";
      }
      else if (temp >= 3 && temp < 7) {
        return "imgs/Temp_plus.png";
      }
      else if (temp >= 7) {
        return "imgs/Temp_plusplus.png";
      }
      else if (temp <= -3 && temp > -7) {
        return "imgs/Temp_minus.png";
      }
      else if (temp <= -7) {
        return "imgs/Temp_minusminus.png";
      }
      else return "imgs/dummy.png";
    });
}


window.onresize = function () {
  console.log("resize");
  render(data);
};
