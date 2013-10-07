jQuery ->

  $('div#gallery div.thumbnails img').click( () ->
    id = $(this).attr('data-picture-id')

    # Set previous main image to not active
    $('div#gallery div.main-image img.active').removeClass('active')

    $('div#gallery div.main-image img[data-picture-id="{0}"]'.format(id)).addClass('active')
  )