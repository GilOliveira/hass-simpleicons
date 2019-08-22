# hass-simple-icons

Fork of @thomasloven 's awesome-icons-set for homeassistant.

Use free icons from the [simpleicons](https://simpleicons.org/) set in Home-assistant.

## Install


Copy the html file for the set into `<config>/www/` where `<config>` is your home-assistant config directory (the directory where your `configuration.yaml` resides).

Add the folowing to the `frontend` section of your `configuration.yaml`

```yaml
frontend:
  extra_html_url:
    - /local/hass-simple-icons.html
```
Restart home-assistant.

## Using

Find the icon you want on [simpleicons.org](https://simpleicons.org/).

Prefix for this set is `si`
The name of the icon is defined by its filename.

Example usage in Home-Assistant:
`icon: si:github`


## Updating the Icons

Use the generate.py python-script (also provided by @thomasloven for fontawesome)
Slightly modified version for the simple-icon svgs in this repository.
