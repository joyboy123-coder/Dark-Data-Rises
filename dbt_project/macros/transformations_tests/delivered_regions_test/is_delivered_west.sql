{% test is_delivered_west(model) %}
  SELECT *
  FROM {{ model }}
  WHERE orderstatus != 'Delivered' OR shippedregion != 'West' 
{% endtest %}