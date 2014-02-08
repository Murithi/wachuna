$(function() {
        var scntDiv = $('#feature-field');
        var i = $('#feature-field').size() + 1;

        $('#add-feature-field').live('click', function() {
                $('<div class="form-group">
                    <label class="col-sm-2 control-label">Feature</label>
                    <div class="col-sm-6">
                        <input class="form-control" type="text">
                    </div>
                    <button class="btn btn-danger"><span></span>Remove Feature</button>
                   </div>').appendTo(scntDiv);
                i++;
                return false;
        });

        $('#add-feature-field').live('click', function() {
                if( i > 2 ) {
                        $(this).parents('div.form-group').remove();
                        i--;
                }
                return false;
        });
});
