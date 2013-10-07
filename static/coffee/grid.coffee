jQuery ->

  # This is to make the Absolute Centering work for the grid hover states
  # We init to a class that isn't centered in case JS isn't availible
  # The we calculate the outerHeight and set that as the height and change the class to centered
  $('div#grid div.portfolio-item div.not-centered').each( () ->

    $(this).css('height', $(this).outerHeight())
    $(this).removeClass('not-centered').addClass('centered')

  )