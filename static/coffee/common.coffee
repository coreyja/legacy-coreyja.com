# Stolen from a StackExchange answer here http://stackoverflow.com/a/4673436
# Basically just adds a format method to JS strings that functions similiar to what I was used to and wanted
if !String.prototype.format
    String.prototype.format = () ->
      args = arguments
      return this.replace(/{(\d+)}/g, (match, number) ->
        return if typeof args[number] != 'undefined' then args[number] else match
      )