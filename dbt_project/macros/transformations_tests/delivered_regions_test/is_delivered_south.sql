{% test is_delivered_south(model) %}
  SELECT *
  FROM {{ model }}
  WHERE orderstatus != 'Delivered' OR shippedregion != 'South' 
{% endtest %}