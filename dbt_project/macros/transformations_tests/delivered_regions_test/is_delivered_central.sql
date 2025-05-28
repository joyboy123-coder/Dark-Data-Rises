{% test is_delivered_central(model) %}
  SELECT *
  FROM {{ model }}
  WHERE orderstatus != 'Delivered' OR shippedregion != 'Central' 
{% endtest %}