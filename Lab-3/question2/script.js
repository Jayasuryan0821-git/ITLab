$(document).ready(function () {
  $(".btn").click(function () {
    // Get the clicked button's value
    var value = $(this).text();

    // Append the value to the input field
    $(".eqn").val($(".eqn").val() + value);
  });

  $(".opr").click(function () {
    // Get the clicked operator
    var operator = $(this).text();

    // Append the operator to the input field
    $(".eqn").val($(".eqn").val() + operator);
  });

  $(".equals").click(function () {
    // Evaluate the expression
    var expression = $(".eqn").val();
    var result = eval(expression);

    // Display the result
    $(".eqn").val(result);
  });

  $(".clear").click(function () {
    // Clear the input field
    $(".eqn").val("");
  });
});
