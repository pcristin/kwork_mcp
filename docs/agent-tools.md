# Agent Tools

Auto-generated tool reference for `kwork-agent` / MCP server.

- Total tools: `284`
- Read tools: `87`
- Write tools: `197`

Regenerate:

```bash
kwork-agent tools export-markdown --include-write
```

## Read Tools

### `get_me`

- Description: Get current user profile.
- Access: read
- Parameter count: 0

Parameters: none

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {},
  "type": "object"
}
```

### `get_user`

- Description: Get user profile by user ID.
- Access: read
- Parameter count: 1

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `user_id` | `int` | yes | `-` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "user_id": {
      "description": "Kwork user ID.",
      "type": "integer"
    }
  },
  "required": [
    "user_id"
  ],
  "type": "object"
}
```

### `get_categories`

- Description: List Kwork categories.
- Access: read
- Parameter count: 0

Parameters: none

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {},
  "type": "object"
}
```

### `get_connects`

- Description: Get remaining connects info.
- Access: read
- Parameter count: 0

Parameters: none

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {},
  "type": "object"
}
```

### `get_notifications`

- Description: Get notifications payload.
- Access: read
- Parameter count: 0

Parameters: none

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {},
  "type": "object"
}
```

### `get_worker_orders`

- Description: Get worker orders.
- Access: read
- Parameter count: 0

Parameters: none

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {},
  "type": "object"
}
```

### `get_payer_orders`

- Description: Get payer orders.
- Access: read
- Parameter count: 0

Parameters: none

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {},
  "type": "object"
}
```

### `get_dialogs_page`

- Description: Get a page of dialogs.
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `page` | `int` | no | `1` |
| `excluded_ids` | `str` | no | `null` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "excluded_ids": {
      "description": "Comma-separated excluded dialog IDs.",
      "type": "string"
    },
    "page": {
      "description": "Dialogs page number (1-based).",
      "type": "integer"
    }
  },
  "type": "object"
}
```

### `get_all_dialogs`

- Description: Get all dialogs by paginating until empty page.
- Access: read
- Parameter count: 0

Parameters: none

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {},
  "type": "object"
}
```

### `get_dialog_with_user_page`

- Description: Get a page of dialog messages by username.
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `username` | `str` | yes | `-` |
| `page` | `int` | no | `1` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "page": {
      "description": "Messages page number (1-based).",
      "type": "integer"
    },
    "username": {
      "description": "Kwork username.",
      "type": "string"
    }
  },
  "required": [
    "username"
  ],
  "type": "object"
}
```

### `get_dialog_with_user`

- Description: Get full dialog with user by username.
- Access: read
- Parameter count: 1

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `username` | `str` | yes | `-` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "username": {
      "description": "Kwork username.",
      "type": "string"
    }
  },
  "required": [
    "username"
  ],
  "type": "object"
}
```

### `get_projects`

- Description: List exchange projects with filters.
- Access: read
- Parameter count: 8

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `categories_ids` | `int_or_str_list` | no | `[]` |
| `price_from` | `int` | no | `null` |
| `price_to` | `int` | no | `null` |
| `hiring_from` | `int` | no | `null` |
| `kworks_filter_from` | `int` | no | `null` |
| `kworks_filter_to` | `int` | no | `null` |
| `page` | `int` | no | `null` |
| `query` | `str` | no | `null` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "categories_ids": {
      "description": "Array of category IDs or strings; empty means favorites.",
      "items": {
        "anyOf": [
          {
            "type": "integer"
          },
          {
            "type": "string"
          }
        ]
      },
      "type": "array"
    },
    "hiring_from": {
      "description": "Minimum hiring percent.",
      "type": "integer"
    },
    "kworks_filter_from": {
      "description": "Minimum offers count (exclusive).",
      "type": "integer"
    },
    "kworks_filter_to": {
      "description": "Maximum offers count (inclusive).",
      "type": "integer"
    },
    "page": {
      "description": "Projects page number.",
      "type": "integer"
    },
    "price_from": {
      "description": "Minimum price.",
      "type": "integer"
    },
    "price_to": {
      "description": "Maximum price.",
      "type": "integer"
    },
    "query": {
      "description": "Search query.",
      "type": "string"
    }
  },
  "type": "object"
}
```

### `actor`

- Description: Auto-exposed KworkClient.actor()
- Access: read
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `catalog_categories`

- Description: Auto-exposed KworkClient.catalog_categories()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `catalog_filters`

- Description: Auto-exposed KworkClient.catalog_filters()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `catalog_main`

- Description: Auto-exposed KworkClient.catalog_main()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `catalog_mainv2`

- Description: Auto-exposed KworkClient.catalog_mainv2()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `catalog_rubrics`

- Description: Auto-exposed KworkClient.catalog_rubrics()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `categories`

- Description: Auto-exposed KworkClient.categories()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `category`

- Description: Auto-exposed KworkClient.category()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `check_login`

- Description: Auto-exposed KworkClient.check_login()
- Access: read
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `check_uad_duplicate`

- Description: Auto-exposed KworkClient.check_uad_duplicate()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `cities`

- Description: Auto-exposed KworkClient.cities()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `countries`

- Description: Auto-exposed KworkClient.countries()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `dialogs`

- Description: Auto-exposed KworkClient.dialogs()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `exchange_info`

- Description: Auto-exposed KworkClient.exchange_info()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `favorite_categories`

- Description: Auto-exposed KworkClient.favorite_categories()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `favorite_kworks`

- Description: Auto-exposed KworkClient.favorite_kworks()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_actor_info`

- Description: Auto-exposed KworkClient.get_actor_info()
- Access: read
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_arbitration_reasons`

- Description: Auto-exposed KworkClient.get_arbitration_reasons()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_available_features`

- Description: Auto-exposed KworkClient.get_available_features()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_badges_info`

- Description: Auto-exposed KworkClient.get_badges_info()
- Access: read
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_bill_refill_url`

- Description: Auto-exposed KworkClient.get_bill_refill_url()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_captcha_status`

- Description: Auto-exposed KworkClient.get_captcha_status()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_channel`

- Description: Auto-exposed KworkClient.get_channel()
- Access: read
- Parameter count: 0

Parameters: none

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {},
  "type": "object"
}
```

### `get_channel_api`

- Description: Auto-exposed KworkClient.get_channel_api()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_company_details`

- Description: Auto-exposed KworkClient.get_company_details()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_complain_categories`

- Description: Auto-exposed KworkClient.get_complain_categories()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_cookie`

- Description: Auto-exposed KworkClient.get_cookie()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_current_versions`

- Description: Auto-exposed KworkClient.get_current_versions()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_custom_options_presets`

- Description: Auto-exposed KworkClient.get_custom_options_presets()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_dialog`

- Description: Auto-exposed KworkClient.get_dialog()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_extras_available_for_order`

- Description: Auto-exposed KworkClient.get_extras_available_for_order()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_fishing_tutorial_questions`

- Description: Auto-exposed KworkClient.get_fishing_tutorial_questions()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_hidden_kworks`

- Description: Auto-exposed KworkClient.get_hidden_kworks()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_in_app_notification`

- Description: Auto-exposed KworkClient.get_in_app_notification()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_inbox_tracks`

- Description: Auto-exposed KworkClient.get_inbox_tracks()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_kwork_answers`

- Description: Auto-exposed KworkClient.get_kwork_answers()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_kwork_details`

- Description: Auto-exposed KworkClient.get_kwork_details()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_kwork_details_extra`

- Description: Auto-exposed KworkClient.get_kwork_details_extra()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_kwork_links_table`

- Description: Auto-exposed KworkClient.get_kwork_links_table()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_kwork_links_tablev2`

- Description: Auto-exposed KworkClient.get_kwork_links_tablev2()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_kwork_portfolios`

- Description: Auto-exposed KworkClient.get_kwork_portfolios()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_kwork_reviews`

- Description: Auto-exposed KworkClient.get_kwork_reviews()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_order_cancellation_reasons`

- Description: Auto-exposed KworkClient.get_order_cancellation_reasons()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_order_details`

- Description: Auto-exposed KworkClient.get_order_details()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_order_files`

- Description: Auto-exposed KworkClient.get_order_files()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_order_header`

- Description: Auto-exposed KworkClient.get_order_header()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_order_provided_data`

- Description: Auto-exposed KworkClient.get_order_provided_data()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_ordered_extras`

- Description: Auto-exposed KworkClient.get_ordered_extras()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_payer_company_modal_url`

- Description: Auto-exposed KworkClient.get_payer_company_modal_url()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_payment_methods`

- Description: Auto-exposed KworkClient.get_payment_methods()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_public_features`

- Description: Auto-exposed KworkClient.get_public_features()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_security_user_data`

- Description: Auto-exposed KworkClient.get_security_user_data()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_subscribers_statistics`

- Description: Auto-exposed KworkClient.get_subscribers_statistics()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_tracks`

- Description: Auto-exposed KworkClient.get_tracks()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_user_info`

- Description: Auto-exposed KworkClient.get_user_info()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_users_last_order_info`

- Description: Auto-exposed KworkClient.get_users_last_order_info()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_voice_message_convert_status`

- Description: Auto-exposed KworkClient.get_voice_message_convert_status()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_voice_message_transcription`

- Description: Auto-exposed KworkClient.get_voice_message_transcription()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_wants_count`

- Description: Auto-exposed KworkClient.get_wants_count()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `get_web_auth_token`

- Description: Auto-exposed KworkClient.get_web_auth_token()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `inboxes`

- Description: Auto-exposed KworkClient.inboxes()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `kworks`

- Description: Auto-exposed KworkClient.kworks()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `my_wants`

- Description: Auto-exposed KworkClient.my_wants()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `notifications`

- Description: Auto-exposed KworkClient.notifications()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `offers`

- Description: Auto-exposed KworkClient.offers()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `order`

- Description: Auto-exposed KworkClient.order()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `orders_between`

- Description: Auto-exposed KworkClient.orders_between()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `portfolio_list`

- Description: Auto-exposed KworkClient.portfolio_list()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `positive_reviews_count`

- Description: Auto-exposed KworkClient.positive_reviews_count()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `privacy`

- Description: Auto-exposed KworkClient.privacy()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `project`

- Description: Auto-exposed KworkClient.project()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `projects`

- Description: Auto-exposed KworkClient.projects()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `resolution`

- Description: Auto-exposed KworkClient.resolution()
- Access: read
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `web_check_is_template`

- Description: Auto-exposed KworkWebClient.check_is_template()
- Access: read
- Parameter count: 4

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `want_id` | `int` | yes | `-` |
| `description` | `str` | yes | `-` |
| `referer` | `str` | yes | `-` |
| `user_agent` | `str` | no | `null` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "description": {
      "description": "Parameter `description` for the underlying method.",
      "type": "string"
    },
    "referer": {
      "description": "Parameter `referer` for the underlying method.",
      "type": "string"
    },
    "user_agent": {
      "description": "Parameter `user_agent` for the underlying method.",
      "type": "string"
    },
    "want_id": {
      "description": "Parameter `want_id` for the underlying method.",
      "type": "integer"
    }
  },
  "required": [
    "want_id",
    "description",
    "referer"
  ],
  "type": "object"
}
```

### `web_quick_faq_init`

- Description: Auto-exposed KworkWebClient.quick_faq_init()
- Access: read
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `referer` | `str` | yes | `-` |
| `user_agent` | `str` | no | `null` |
| `page` | `str` | no | `'new_offer'` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "page": {
      "description": "Parameter `page` for the underlying method.",
      "type": "string"
    },
    "referer": {
      "description": "Parameter `referer` for the underlying method.",
      "type": "string"
    },
    "user_agent": {
      "description": "Parameter `user_agent` for the underlying method.",
      "type": "string"
    }
  },
  "required": [
    "referer"
  ],
  "type": "object"
}
```

## Write Tools

### `send_message`

- Description: Send a message to a user.
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `user_id` | `int` | yes | `-` |
| `text` | `str` | yes | `-` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "text": {
      "description": "Message text.",
      "type": "string"
    },
    "user_id": {
      "description": "Recipient user ID.",
      "type": "integer"
    }
  },
  "required": [
    "user_id",
    "text"
  ],
  "type": "object"
}
```

### `accept_extras`

- Description: Auto-exposed KworkClient.accept_extras()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `accept_stage_suggestion`

- Description: Auto-exposed KworkClient.accept_stage_suggestion()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `add_favorite_categories`

- Description: Auto-exposed KworkClient.add_favorite_categories()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `add_new_phone_number`

- Description: Auto-exposed KworkClient.add_new_phone_number()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `add_phone_number`

- Description: Auto-exposed KworkClient.add_phone_number()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `add_stage`

- Description: Auto-exposed KworkClient.add_stage()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `allow_inbox_request`

- Description: Auto-exposed KworkClient.allow_inbox_request()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `allow_mobile_push`

- Description: Auto-exposed KworkClient.allow_mobile_push()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `allow_order_portfolio_upload`

- Description: Auto-exposed KworkClient.allow_order_portfolio_upload()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `allow_push_notifications_sound`

- Description: Auto-exposed KworkClient.allow_push_notifications_sound()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `apple_sign_in`

- Description: Auto-exposed KworkClient.apple_sign_in()
- Access: write
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `apply_filters`

- Description: Auto-exposed KworkClient.apply_filters()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `approve_order`

- Description: Auto-exposed KworkClient.approve_order()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `approve_order_stage`

- Description: Auto-exposed KworkClient.approve_order_stage()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `archive_dialog`

- Description: Auto-exposed KworkClient.archive_dialog()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `block_dialog`

- Description: Auto-exposed KworkClient.block_dialog()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `blocked_dialog_list`

- Description: Auto-exposed KworkClient.blocked_dialog_list()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `cancel_order_awaiting_payment`

- Description: Auto-exposed KworkClient.cancel_order_awaiting_payment()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `cancel_order_by_payer`

- Description: Auto-exposed KworkClient.cancel_order_by_payer()
- Access: write
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `cancel_order_by_worker`

- Description: Auto-exposed KworkClient.cancel_order_by_worker()
- Access: write
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `category_attributes`

- Description: Auto-exposed KworkClient.category_attributes()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `change_password`

- Description: Auto-exposed KworkClient.change_password()
- Access: write
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `change_payer_sub_role`

- Description: Auto-exposed KworkClient.change_payer_sub_role()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `change_username`

- Description: Auto-exposed KworkClient.change_username()
- Access: write
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `clear_filters`

- Description: Auto-exposed KworkClient.clear_filters()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `confirm_cancel_order_request_by_payer`

- Description: Auto-exposed KworkClient.confirm_cancel_order_request_by_payer()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `confirm_cancel_order_request_by_worker`

- Description: Auto-exposed KworkClient.confirm_cancel_order_request_by_worker()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `create_answer`

- Description: Auto-exposed KworkClient.create_answer()
- Access: write
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `create_kwork_complain`

- Description: Auto-exposed KworkClient.create_kwork_complain()
- Access: write
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `create_portfolio`

- Description: Auto-exposed KworkClient.create_portfolio()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `create_review`

- Description: Auto-exposed KworkClient.create_review()
- Access: write
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `create_stage`

- Description: Auto-exposed KworkClient.create_stage()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `del_favorite_categories`

- Description: Auto-exposed KworkClient.del_favorite_categories()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `delete_account`

- Description: Auto-exposed KworkClient.delete_account()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `delete_cancel_order_request_by_payer`

- Description: Auto-exposed KworkClient.delete_cancel_order_request_by_payer()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `delete_cancel_order_request_by_worker`

- Description: Auto-exposed KworkClient.delete_cancel_order_request_by_worker()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `delete_cover`

- Description: Auto-exposed KworkClient.delete_cover()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `delete_kwork`

- Description: Auto-exposed KworkClient.delete_kwork()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `delete_message`

- Description: Auto-exposed KworkClient.delete_message()
- Access: write
- Parameter count: 1

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `message_id` | `int` | yes | `-` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "message_id": {
      "description": "Parameter `message_id` for the underlying method.",
      "type": "integer"
    }
  },
  "required": [
    "message_id"
  ],
  "type": "object"
}
```

### `delete_offer`

- Description: Auto-exposed KworkClient.delete_offer()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `delete_order_note`

- Description: Auto-exposed KworkClient.delete_order_note()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `delete_portfolio`

- Description: Auto-exposed KworkClient.delete_portfolio()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `delete_review`

- Description: Auto-exposed KworkClient.delete_review()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `delete_stage`

- Description: Auto-exposed KworkClient.delete_stage()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `delete_user_note`

- Description: Auto-exposed KworkClient.delete_user_note()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `delete_want`

- Description: Auto-exposed KworkClient.delete_want()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `edit_answer`

- Description: Auto-exposed KworkClient.edit_answer()
- Access: write
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `edit_portfolio`

- Description: Auto-exposed KworkClient.edit_portfolio()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `edit_review`

- Description: Auto-exposed KworkClient.edit_review()
- Access: write
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `edit_stage`

- Description: Auto-exposed KworkClient.edit_stage()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `email_verification_letter`

- Description: Auto-exposed KworkClient.email_verification_letter()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `fcm_notifications_read`

- Description: Auto-exposed KworkClient.fcm_notifications_read()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `fcm_notifications_received`

- Description: Auto-exposed KworkClient.fcm_notifications_received()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `fcm_token_request_failed`

- Description: Auto-exposed KworkClient.fcm_token_request_failed()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `file_delete`

- Description: Auto-exposed KworkClient.file_delete()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `file_upload`

- Description: Auto-exposed KworkClient.file_upload()
- Access: write
- Parameter count: 4

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `fields` | `object` | no | `null` |
| `files` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "fields": {
      "description": "Parameter `fields` for the underlying method.",
      "type": "object"
    },
    "files": {
      "description": "Parameter `files` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `hide_dialog`

- Description: Auto-exposed KworkClient.hide_dialog()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `hide_self_employed_notification`

- Description: Auto-exposed KworkClient.hide_self_employed_notification()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `hide_voice_message_settings_popup`

- Description: Auto-exposed KworkClient.hide_voice_message_settings_popup()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `inbox_complain_message`

- Description: Auto-exposed KworkClient.inbox_complain_message()
- Access: write
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `inbox_create`

- Description: Auto-exposed KworkClient.inbox_create()
- Access: write
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `inbox_custom_request_decline`

- Description: Auto-exposed KworkClient.inbox_custom_request_decline()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `inbox_delete`

- Description: Auto-exposed KworkClient.inbox_delete()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `inbox_edit`

- Description: Auto-exposed KworkClient.inbox_edit()
- Access: write
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `inbox_forward`

- Description: Auto-exposed KworkClient.inbox_forward()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `inbox_message`

- Description: Auto-exposed KworkClient.inbox_message()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `inbox_payer_decline`

- Description: Auto-exposed KworkClient.inbox_payer_decline()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `inbox_read`

- Description: Auto-exposed KworkClient.inbox_read()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `inbox_track_message`

- Description: Auto-exposed KworkClient.inbox_track_message()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `inbox_worker_decline`

- Description: Auto-exposed KworkClient.inbox_worker_decline()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `is_dialog_allow`

- Description: Auto-exposed KworkClient.is_dialog_allow()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `kworks_categories_list`

- Description: Auto-exposed KworkClient.kworks_categories_list()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `kworks_status_list`

- Description: Auto-exposed KworkClient.kworks_status_list()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `logout`

- Description: Auto-exposed KworkClient.logout()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `mark_inbox_tracks_as_read`

- Description: Auto-exposed KworkClient.mark_inbox_tracks_as_read()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `mark_kwork_as_favorite`

- Description: Auto-exposed KworkClient.mark_kwork_as_favorite()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `mark_kwork_as_hidden`

- Description: Auto-exposed KworkClient.mark_kwork_as_hidden()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `mark_kworks_black_friday`

- Description: Auto-exposed KworkClient.mark_kworks_black_friday()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `mark_voice_message_heard`

- Description: Auto-exposed KworkClient.mark_voice_message_heard()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `miniature`

- Description: Auto-exposed KworkClient.miniature()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `notifications_fetch`

- Description: Auto-exposed KworkClient.notifications_fetch()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `notifications_received`

- Description: Auto-exposed KworkClient.notifications_received()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `offer`

- Description: Auto-exposed KworkClient.offer()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `offer_order_options`

- Description: Auto-exposed KworkClient.offer_order_options()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `offline`

- Description: Auto-exposed KworkClient.offline()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `order_kwork`

- Description: Auto-exposed KworkClient.order_kwork()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `order_stage`

- Description: Auto-exposed KworkClient.order_stage()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `pause_kwork`

- Description: Auto-exposed KworkClient.pause_kwork()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `pay_order_awaiting_payment`

- Description: Auto-exposed KworkClient.pay_order_awaiting_payment()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `payer_buy_extras`

- Description: Auto-exposed KworkClient.payer_buy_extras()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `payer_decline_extras`

- Description: Auto-exposed KworkClient.payer_decline_extras()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `payer_declines_extra_removal_request`

- Description: Auto-exposed KworkClient.payer_declines_extra_removal_request()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `payer_extra_delete`

- Description: Auto-exposed KworkClient.payer_extra_delete()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `payer_orders`

- Description: Auto-exposed KworkClient.payer_orders()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `payer_upgrade_package`

- Description: Auto-exposed KworkClient.payer_upgrade_package()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `portfolio_categories_list`

- Description: Auto-exposed KworkClient.portfolio_categories_list()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `push_in_app_notification_log`

- Description: Auto-exposed KworkClient.push_in_app_notification_log()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `rate_arbitration`

- Description: Auto-exposed KworkClient.rate_arbitration()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `recharge_balance`

- Description: Auto-exposed KworkClient.recharge_balance()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `register_cloud_token`

- Description: Auto-exposed KworkClient.register_cloud_token()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `reject_cancel_order_request_by_payer`

- Description: Auto-exposed KworkClient.reject_cancel_order_request_by_payer()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `reject_cancel_order_request_by_worker`

- Description: Auto-exposed KworkClient.reject_cancel_order_request_by_worker()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `reject_stage_suggestion`

- Description: Auto-exposed KworkClient.reject_stage_suggestion()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `repeat_order`

- Description: Auto-exposed KworkClient.repeat_order()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `replace_uad`

- Description: Auto-exposed KworkClient.replace_uad()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `report_app_version`

- Description: Auto-exposed KworkClient.report_app_version()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `request_phone_changing`

- Description: Auto-exposed KworkClient.request_phone_changing()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `reset_password`

- Description: Auto-exposed KworkClient.reset_password()
- Access: write
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `restart_want`

- Description: Auto-exposed KworkClient.restart_want()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `save_order_note`

- Description: Auto-exposed KworkClient.save_order_note()
- Access: write
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `save_user_note`

- Description: Auto-exposed KworkClient.save_user_note()
- Access: write
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `search`

- Description: Auto-exposed KworkClient.search()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `search_dialogs`

- Description: Auto-exposed KworkClient.search_dialogs()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `search_inboxes`

- Description: Auto-exposed KworkClient.search_inboxes()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `search_kworks_catalog_query`

- Description: Auto-exposed KworkClient.search_kworks_catalog_query()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `search_messages`

- Description: Auto-exposed KworkClient.search_messages()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `search_order_tracks`

- Description: Auto-exposed KworkClient.search_order_tracks()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `search_tracks`

- Description: Auto-exposed KworkClient.search_tracks()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `send_bonus`

- Description: Auto-exposed KworkClient.send_bonus()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `send_company_for_verification`

- Description: Auto-exposed KworkClient.send_company_for_verification()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `send_order_for_approval`

- Description: Auto-exposed KworkClient.send_order_for_approval()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `send_order_for_arbitration`

- Description: Auto-exposed KworkClient.send_order_for_arbitration()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `send_order_for_revision`

- Description: Auto-exposed KworkClient.send_order_for_revision()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `send_order_receipt_link_for_verification`

- Description: Auto-exposed KworkClient.send_order_receipt_link_for_verification()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `send_order_requirements`

- Description: Auto-exposed KworkClient.send_order_requirements()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `send_report`

- Description: Auto-exposed KworkClient.send_report()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `send_self_employed_survey_result`

- Description: Auto-exposed KworkClient.send_self_employed_survey_result()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `send_user_status`

- Description: Auto-exposed KworkClient.send_user_status()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `send_whats_app_code`

- Description: Auto-exposed KworkClient.send_whats_app_code()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `set_available_at_weekends`

- Description: Auto-exposed KworkClient.set_available_at_weekends()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `set_dialog_starred`

- Description: Auto-exposed KworkClient.set_dialog_starred()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `set_favorite`

- Description: Auto-exposed KworkClient.set_favorite()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `set_fishing_tutorial_status`

- Description: Auto-exposed KworkClient.set_fishing_tutorial_status()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `set_offline`

- Description: Auto-exposed KworkClient.set_offline()
- Access: write
- Parameter count: 0

Parameters: none

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {},
  "type": "object"
}
```

### `set_order_rating`

- Description: Auto-exposed KworkClient.set_order_rating()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `set_taking_orders`

- Description: Auto-exposed KworkClient.set_taking_orders()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `set_typing`

- Description: Auto-exposed KworkClient.set_typing()
- Access: write
- Parameter count: 1

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `recipient_id` | `int` | yes | `-` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "recipient_id": {
      "description": "Parameter `recipient_id` for the underlying method.",
      "type": "integer"
    }
  },
  "required": [
    "recipient_id"
  ],
  "type": "object"
}
```

### `set_user_type`

- Description: Auto-exposed KworkClient.set_user_type()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `set_voice_message_receiving`

- Description: Auto-exposed KworkClient.set_voice_message_receiving()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `set_voice_message_speed`

- Description: Auto-exposed KworkClient.set_voice_message_speed()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `sign_in`

- Description: Auto-exposed KworkClient.sign_in()
- Access: write
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `sign_up`

- Description: Auto-exposed KworkClient.sign_up()
- Access: write
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `social_sign_in`

- Description: Auto-exposed KworkClient.social_sign_in()
- Access: write
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `social_sign_in_by_token`

- Description: Auto-exposed KworkClient.social_sign_in_by_token()
- Access: write
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `social_sign_in_by_tokenv2`

- Description: Auto-exposed KworkClient.social_sign_in_by_tokenv2()
- Access: write
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `social_sign_up`

- Description: Auto-exposed KworkClient.social_sign_up()
- Access: write
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `social_sign_up_by_token`

- Description: Auto-exposed KworkClient.social_sign_up_by_token()
- Access: write
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `start_kwork`

- Description: Auto-exposed KworkClient.start_kwork()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `stop_want`

- Description: Auto-exposed KworkClient.stop_want()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `suggest_stages`

- Description: Auto-exposed KworkClient.suggest_stages()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `terms`

- Description: Auto-exposed KworkClient.terms()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `terms_of_service`

- Description: Auto-exposed KworkClient.terms_of_service()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `timezones`

- Description: Auto-exposed KworkClient.timezones()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `tos`

- Description: Auto-exposed KworkClient.tos()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `track_delete`

- Description: Auto-exposed KworkClient.track_delete()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `track_edit`

- Description: Auto-exposed KworkClient.track_edit()
- Access: write
- Parameter count: 3

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `body` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "body": {
      "description": "Parameter `body` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `track_message`

- Description: Auto-exposed KworkClient.track_message()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `track_read`

- Description: Auto-exposed KworkClient.track_read()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `translation_languages`

- Description: Auto-exposed KworkClient.translation_languages()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `typing`

- Description: Auto-exposed KworkClient.typing()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `unarchive_dialog`

- Description: Auto-exposed KworkClient.unarchive_dialog()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `unblock_dialog`

- Description: Auto-exposed KworkClient.unblock_dialog()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `unread_dialog`

- Description: Auto-exposed KworkClient.unread_dialog()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `update_avatar`

- Description: Auto-exposed KworkClient.update_avatar()
- Access: write
- Parameter count: 4

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `fields` | `object` | no | `null` |
| `files` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "fields": {
      "description": "Parameter `fields` for the underlying method.",
      "type": "object"
    },
    "files": {
      "description": "Parameter `files` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `update_chat_draft_message`

- Description: Auto-exposed KworkClient.update_chat_draft_message()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `update_order_draft_message`

- Description: Auto-exposed KworkClient.update_order_draft_message()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `update_settings`

- Description: Auto-exposed KworkClient.update_settings()
- Access: write
- Parameter count: 4

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `fields` | `object` | no | `null` |
| `files` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "fields": {
      "description": "Parameter `fields` for the underlying method.",
      "type": "object"
    },
    "files": {
      "description": "Parameter `files` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `update_stage_progress`

- Description: Auto-exposed KworkClient.update_stage_progress()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `upload_cover`

- Description: Auto-exposed KworkClient.upload_cover()
- Access: write
- Parameter count: 4

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `fields` | `object` | no | `null` |
| `files` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "fields": {
      "description": "Parameter `fields` for the underlying method.",
      "type": "object"
    },
    "files": {
      "description": "Parameter `files` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `upload_log`

- Description: Auto-exposed KworkClient.upload_log()
- Access: write
- Parameter count: 4

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `fields` | `object` | no | `null` |
| `files` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "fields": {
      "description": "Parameter `fields` for the underlying method.",
      "type": "object"
    },
    "files": {
      "description": "Parameter `files` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `upload_portfolio_file`

- Description: Auto-exposed KworkClient.upload_portfolio_file()
- Access: write
- Parameter count: 4

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `fields` | `object` | no | `null` |
| `files` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "fields": {
      "description": "Parameter `fields` for the underlying method.",
      "type": "object"
    },
    "files": {
      "description": "Parameter `files` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `uploaded_file`

- Description: Auto-exposed KworkClient.uploaded_file()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `user`

- Description: Auto-exposed KworkClient.user()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `user_by_username`

- Description: Auto-exposed KworkClient.user_by_username()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `user_kworks`

- Description: Auto-exposed KworkClient.user_kworks()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `user_reviews`

- Description: Auto-exposed KworkClient.user_reviews()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `user_search`

- Description: Auto-exposed KworkClient.user_search()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `validate_event`

- Description: Auto-exposed KworkClient.validate_event()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `verify_phone_activation_code`

- Description: Auto-exposed KworkClient.verify_phone_activation_code()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `verify_sms_code_for_account_deleting`

- Description: Auto-exposed KworkClient.verify_sms_code_for_account_deleting()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `viewed_catalog_kworks`

- Description: Auto-exposed KworkClient.viewed_catalog_kworks()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `voice_upload`

- Description: Auto-exposed KworkClient.voice_upload()
- Access: write
- Parameter count: 4

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `False` |
| `fields` | `object` | no | `null` |
| `files` | `object` | no | `null` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "fields": {
      "description": "Parameter `fields` for the underlying method.",
      "type": "object"
    },
    "files": {
      "description": "Parameter `files` for the underlying method.",
      "type": "object"
    },
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `want`

- Description: Auto-exposed KworkClient.want()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `wants_status_list`

- Description: Auto-exposed KworkClient.wants_status_list()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `web_create_exchange_offer`

- Description: Auto-exposed KworkWebClient.create_exchange_offer()
- Access: write
- Parameter count: 10

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `want_id` | `int` | yes | `-` |
| `offer_type` | `str` | no | `'custom'` |
| `description` | `str` | yes | `-` |
| `kwork_duration` | `int` | yes | `-` |
| `kwork_price` | `int` | yes | `-` |
| `kwork_name` | `str` | yes | `-` |
| `user_agent` | `str` | no | `null` |
| `extra_headers` | `object` | no | `null` |
| `raise_on_error` | `bool` | no | `True` |
| `referer` | `str` | no | `null` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "description": {
      "description": "Parameter `description` for the underlying method.",
      "type": "string"
    },
    "extra_headers": {
      "description": "Parameter `extra_headers` for the underlying method.",
      "type": "object"
    },
    "kwork_duration": {
      "description": "Parameter `kwork_duration` for the underlying method.",
      "type": "integer"
    },
    "kwork_name": {
      "description": "Parameter `kwork_name` for the underlying method.",
      "type": "string"
    },
    "kwork_price": {
      "description": "Parameter `kwork_price` for the underlying method.",
      "type": "integer"
    },
    "offer_type": {
      "description": "Parameter `offer_type` for the underlying method.",
      "type": "string"
    },
    "raise_on_error": {
      "description": "Parameter `raise_on_error` for the underlying method.",
      "type": "boolean"
    },
    "referer": {
      "description": "Parameter `referer` for the underlying method.",
      "type": "string"
    },
    "user_agent": {
      "description": "Parameter `user_agent` for the underlying method.",
      "type": "string"
    },
    "want_id": {
      "description": "Parameter `want_id` for the underlying method.",
      "type": "integer"
    }
  },
  "required": [
    "want_id",
    "description",
    "kwork_duration",
    "kwork_price",
    "kwork_name"
  ],
  "type": "object"
}
```

### `web_create_offer_draft`

- Description: Auto-exposed KworkWebClient.create_offer_draft()
- Access: write
- Parameter count: 6

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `project_id` | `int` | yes | `-` |
| `csrftoken` | `str` | yes | `-` |
| `draft_key` | `str` | yes | `-` |
| `message` | `str` | no | `''` |
| `referer` | `str` | yes | `-` |
| `user_agent` | `str` | no | `null` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "csrftoken": {
      "description": "Parameter `csrftoken` for the underlying method.",
      "type": "string"
    },
    "draft_key": {
      "description": "Parameter `draft_key` for the underlying method.",
      "type": "string"
    },
    "message": {
      "description": "Parameter `message` for the underlying method.",
      "type": "string"
    },
    "project_id": {
      "description": "Parameter `project_id` for the underlying method.",
      "type": "integer"
    },
    "referer": {
      "description": "Parameter `referer` for the underlying method.",
      "type": "string"
    },
    "user_agent": {
      "description": "Parameter `user_agent` for the underlying method.",
      "type": "string"
    }
  },
  "required": [
    "project_id",
    "csrftoken",
    "draft_key",
    "referer"
  ],
  "type": "object"
}
```

### `web_login`

- Description: Auto-exposed KworkClient.web_login()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `url_to_redirect` | `str` | no | `'/'` |
| `user_agent` | `str` | no | `null` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "url_to_redirect": {
      "description": "Parameter `url_to_redirect` for the underlying method.",
      "type": "string"
    },
    "user_agent": {
      "description": "Parameter `user_agent` for the underlying method.",
      "type": "string"
    }
  },
  "type": "object"
}
```

### `web_login_via_mobile_web_auth_token`

- Description: Auto-exposed KworkWebClient.login_via_mobile_web_auth_token()
- Access: write
- Parameter count: 5

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `url_to_redirect` | `str` | no | `'/'` |
| `user_agent` | `str` | no | `null` |
| `allow_redirects` | `bool` | no | `True` |
| `max_redirects` | `int` | no | `10` |
| `timeout` | `float` | no | `null` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "allow_redirects": {
      "description": "Parameter `allow_redirects` for the underlying method.",
      "type": "boolean"
    },
    "max_redirects": {
      "description": "Parameter `max_redirects` for the underlying method.",
      "type": "integer"
    },
    "timeout": {
      "description": "Parameter `timeout` for the underlying method.",
      "type": "number"
    },
    "url_to_redirect": {
      "description": "Parameter `url_to_redirect` for the underlying method.",
      "type": "string"
    },
    "user_agent": {
      "description": "Parameter `user_agent` for the underlying method.",
      "type": "string"
    }
  },
  "type": "object"
}
```

### `web_open_new_offer_page`

- Description: Auto-exposed KworkWebClient.open_new_offer_page()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `project_id` | `int` | yes | `-` |
| `user_agent` | `str` | no | `null` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "project_id": {
      "description": "Parameter `project_id` for the underlying method.",
      "type": "integer"
    },
    "user_agent": {
      "description": "Parameter `user_agent` for the underlying method.",
      "type": "string"
    }
  },
  "required": [
    "project_id"
  ],
  "type": "object"
}
```

### `web_submit_exchange_offer`

- Description: Auto-exposed KworkWebClient.submit_exchange_offer()
- Access: write
- Parameter count: 8

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `project_id` | `int` | yes | `-` |
| `offer_type` | `str` | no | `'custom'` |
| `description` | `str` | yes | `-` |
| `kwork_duration` | `int` | yes | `-` |
| `kwork_price` | `int` | yes | `-` |
| `kwork_name` | `str` | yes | `-` |
| `user_agent` | `str` | no | `null` |
| `raise_on_error` | `bool` | no | `True` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "description": {
      "description": "Parameter `description` for the underlying method.",
      "type": "string"
    },
    "kwork_duration": {
      "description": "Parameter `kwork_duration` for the underlying method.",
      "type": "integer"
    },
    "kwork_name": {
      "description": "Parameter `kwork_name` for the underlying method.",
      "type": "string"
    },
    "kwork_price": {
      "description": "Parameter `kwork_price` for the underlying method.",
      "type": "integer"
    },
    "offer_type": {
      "description": "Parameter `offer_type` for the underlying method.",
      "type": "string"
    },
    "project_id": {
      "description": "Parameter `project_id` for the underlying method.",
      "type": "integer"
    },
    "raise_on_error": {
      "description": "Parameter `raise_on_error` for the underlying method.",
      "type": "boolean"
    },
    "user_agent": {
      "description": "Parameter `user_agent` for the underlying method.",
      "type": "string"
    }
  },
  "required": [
    "project_id",
    "description",
    "kwork_duration",
    "kwork_price",
    "kwork_name"
  ],
  "type": "object"
}
```

### `worker_confirms_extra_removal_request`

- Description: Auto-exposed KworkClient.worker_confirms_extra_removal_request()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `worker_decline_extras`

- Description: Auto-exposed KworkClient.worker_decline_extras()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `worker_declines_extra_removal_request`

- Description: Auto-exposed KworkClient.worker_declines_extra_removal_request()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `worker_extra_delete`

- Description: Auto-exposed KworkClient.worker_extra_delete()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `worker_inprogress`

- Description: Auto-exposed KworkClient.worker_inprogress()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

### `worker_orders`

- Description: Auto-exposed KworkClient.worker_orders()
- Access: write
- Parameter count: 2

| Parameter | Type | Required | Default |
|---|---|---:|---|
| `use_token` | `bool` | no | `True` |
| `params` | `object` | no | `{}` |

MCP input schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "params": {
      "description": "Additional keyword arguments passed through to the underlying method.",
      "type": "object"
    },
    "use_token": {
      "description": "Parameter `use_token` for the underlying method.",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

