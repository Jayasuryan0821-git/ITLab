$(document).ready(function () {
  $("#btn").click(function () {
    let bgcolor = $("#bcol").find(":selected").val();
    let fontstyle = $("#fstyle").find(":selected").val();
    let fontsize = $("#fsize").val();
    let borderStyle = $("input.border:checked").val();
    let message = $("#area").val();
    let newBlk = $("<div>");

    if ($("#mycheckbox").is(":checked")) {
      let imgSrc = "spidey.jpg";
      let img = $("<img>");
      img.attr("src", imgSrc); // Use .attr() to set attributes
      newBlk.append(img); // Append img to newBlk
    }

    newBlk.attr("id", "div4"); // Use .attr() to set ID attribute

    newBlk.css({
      "background-color": bgcolor,
      "font-family": fontstyle,
      "font-size": fontsize + "px", // assuming the font size is in pixels
      border: borderStyle, // Use quotes for "border"
      position: "fixed",
      top: "0",
      right: "0",
    });

    newBlk.append("<p>" + message + "</p>"); // Append message to newBlk
    $("body").append(newBlk); // Append newBlk to body
  });
});
