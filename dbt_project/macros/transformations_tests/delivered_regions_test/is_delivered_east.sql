{% test is_delivered_east(model) %}
  SELECT *
  FROM {{ model }}
  WHERE orderstatus != 'Delivered' OR shippedregion != 'East' 
{% endtest %}