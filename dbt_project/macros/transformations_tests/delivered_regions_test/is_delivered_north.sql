{% test is_delivered_north(model) %}
  SELECT *
  FROM {{ model }}
  WHERE orderstatus != 'Delivered' OR shippedregion != 'North' 
{% endtest %}