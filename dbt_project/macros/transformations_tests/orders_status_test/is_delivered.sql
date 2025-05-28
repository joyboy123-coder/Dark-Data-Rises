{% test is_delivered(model) %}
  SELECT *
  FROM {{ model }}
  WHERE orderstatus != 'Delivered'
{% endtest %}
