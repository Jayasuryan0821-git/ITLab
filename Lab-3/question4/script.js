$(document).ready(function () {
  $("#bill").click(function () {
    let brand = $("#brands").val();
    let products = [];
    if ($("#laptop").is(":checked")) {
      products.push("Laptop");
    }
    if ($("#mobile").is(":checked")) {
      products.push("Mobile");
    }
    let quantity = parseInt(prompt("Enter the quantity"));
    let amt = computeTotal(brand, quantity);
    alert("Total amount: $" + amt.toFixed(2));
  });

  function computeTotal(brand, quantity) {
    let cost = 0;
    if (brand === "HP") {
      cost += 500;
    } else if (brand === "Nokia") {
      cost += 400;
    } else if (brand === "Apple") {
      cost += 1000;
    } else if (brand === "Motorola") {
      cost += 300;
    }
    let total = quantity * cost;
    return total;
  }
});
