# Stolen from a StackExchange answer here http://stackoverflow.com/a/4673436
# Basically just adds a format method to JS strings that functions similiar to what I was used to and wanted
if !String.prototype.format
    String.prototype.format = () ->
      args = arguments
      return this.replace(/{(\d+)}/g, (match, number) ->
        return if typeof args[number] != 'undefined' then args[number] else match
      )

jQuery ->
  # About Me Drawer
  $('h3#about-link').click( ()->
    $('div#about-me').slideToggle(400, () ->
      if $(this).css('display') == 'block'
        $('h3#about-link i').removeClass().addClass('icon-angle-up')
      else
        $('h3#about-link i').removeClass().addClass('icon-angle-down')
    )
  )