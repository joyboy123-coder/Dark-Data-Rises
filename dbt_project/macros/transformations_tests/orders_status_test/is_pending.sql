{% test is_pending(model) %}
  SELECT *
  FROM {{ model }}
  WHERE orderstatus != 'Pending'
{% endtest %}
