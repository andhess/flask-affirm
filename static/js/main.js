$(document).ready(function() {
  $(".affirm-pay").click(function() {
    var name = $("#name").val();
    var email = $("#email").val();
    var phone = $("#phone").val();
    var address1 = $("#address1").val();
    var address2 = $("#address2").val();
    var city = $("#city").val();
    var state = $("#state").val();
    var zip = $("#zip").val();

    p = affirm.checkout({ 
      "merchant": {
        "user_confirmation_url": "http://localhost:5000/success",
        "user_cancel_url": "http://localhost:5000/cancel",
        "user_confirmation_url_action": "POST"
      },
      "shipping":{
        "name":{
          "full": name
        },
        "address":{
          "line1": address1,
          "line2": address2,
          "city": city,
          "state": state,
          "zipcode": zip,
          "country":"USA"
        },
        "phone_number": phone,
        "email": email
      },
      "billing":{
        "name": {
          "full": name
        },
        "address":{
          "line1": address1,
          "line2": address2,
          "city": city,
          "state": state,
          "zipcode": zip,
          "country":"USA"
        },
        "phone_number": phone,
        "email": email
      },
      "items": [{
        "display_name":         "Digital Watch",
        "sku":                  "ABC-123",
        "unit_price":           50000,
        "qty":                  1,
        "item_image_url":       "http://www.andhess.com",
        "item_url":             "http://www.andhess.com"
      }],
      "shipping_amount":        0,
      "tax_amount":             0,
      "total":                  50000
  });
  affirm.checkout.open();
  });
});
