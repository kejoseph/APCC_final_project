function fetchAndPopulateEnzymes(plasmidTerm,geneSeq) {
    $.ajax({
        url: 'scripts/get_plasmid.cgi',
        type: 'POST',
        data: { 
            plasmid_entry: plasmidTerm,
            gene_sequence: geneSeq 
        },
        success: function(data) {
            console.log('Response from server:', data);
            if (data.error) {
                alert(data.error);
                $('#error').text(data.error);  // display error in HTML
            }
            if (data.length == 0) {
                // Display an error message
                var errorMessage = document.createElement('p');
                errorMessage.textContent = 'Error: No restriction enzymes available.';
                document.getElementById('enzymeDropdownSection').appendChild(errorMessage);
            }
            else {
                // update HTML with good enzymes
                var dropdown = $('#enzymeDropdown');
                dropdown.empty();
                dropdown.append($('<option value="" selected disabled>Select Enzyme</option>')); // Add default option
                $.each(data, function(index, value) {
                    dropdown.append($('<option></option>').attr('value', value).text(value));
                });
                // Show the enzyme dropdown
                $('#enzymeDropdownSection').show();
            }
        },
        error: function(jqXHR, textStatus, errorThrown){
            console.error('jqXHR:', jqXHR);
            alert("Failed to find plasmid! Please try another entry.");
            $('#enzymeDropdownSection').empty();
        }
    });
}

// Function to handle the selection of an enzyme and make the AJAX request
function handleEnzymeSelection(selectedEnzyme, plasmidTerm, geneSeq) {
    // Make an AJAX request to the server to generate the sequence based on the selected enzyme
    $.ajax({
        url: 'scripts/get_final_seqs.cgi',
        type: 'POST',
        data: { 
            plasmid_entry: plasmidTerm,
            gene_sequence: geneSeq, 
            selectedEnzyme: selectedEnzyme 
        },  // Send the selected enzyme to the server
        success: function(data) {
            // Handle the received data
            console.log('Received data:', data);
            $('#finalSeq').text(data.full_seq);  // Update the HTML with the full sequence
            // Render the primers onto the HTML
            $('#fwdPrimer').text('Forward Primer: ' + data.primers[0]);  // Update the HTML with the forward primer
            $('#revPrimer').text('Reverse Primer: ' + data.primers[1]);  // Update the HTML with the reverse primer
            document.getElementById('processingMessage').style.display = 'none';
            $('#primersSection').show();
            $('#buttonSection').show();
        },
        error: function(jqXHR, textStatus, errorThrown){
            console.error('jqXHR:', jqXHR);
            alert("Failed to generate sequence");
        }
    });
}


// function plasmidAutocomplete

// run our javascript once the page is ready
$(document).ready(function() {
    $('#enzymeDropdownSection').hide();
    $('#primersSection').hide();
    $('#buttonSection').hide();
    $("#plasmidSearch").autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "scripts/fetch_all_plasmids.cgi",
                type: "GET",
                data: {
                    plasmidSearch: request.term
                },
                success: function(data) {
                    console.log(data);
                    response(data);
                },
                error: function(jqXHR, textStatus, errorThrown){
                    console.error('jqXHR:', jqXHR);
                    alert("search failed");
                }
            });
        },
        minLength: 1,
    });
    $('#cloningForm').submit(function(event) {
        event.preventDefault();  // prevents 'normal' form submission

        var plasmidTerm = $('#plasmidSearch').val();
        var geneSeq = $('#geneSequence').val();
        // Validate the gene sequence input using a regular expression
        var validCharacters = /^[ACGTNacgtn\s]+$/; // Allow only A, C, G, T, and whitespace characters

        if (!validCharacters.test(geneSeq)) {
        // If the input contains invalid characters, prevent the form submission and display an alert
        alert('Invalid characters detected in gene sequence. Please enter a valid gene sequence. Valid characters are A,C,G,T,N,a,c,g,t,n');
        } else {
        // Proceed with the form submission and further processing
        fetchAndPopulateEnzymes(plasmidTerm, geneSeq);
        console.log(plasmidTerm)
        console.log(geneSeq)
        }
    });

    // Selection of an enzyme from the dropdown
    $('#enzymeDropdown').on('change', function() {
        
        var selectedEnzyme = $(this).val();  // Get the selected enzyme
        console.log(selectedEnzyme)
        document.getElementById('processingMessage').style.display = 'block';
        // Call the function to handle the enzyme selection and make the AJAX request
        var plasmidTerm = $('#plasmidSearch').val();
        var geneSeq = $('#geneSequence').val();
        handleEnzymeSelection(selectedEnzyme, plasmidTerm, geneSeq);
    });

    // Copy to Clipboard Button
    document.getElementById('copyToClipboardBtn').addEventListener('click', function() {
        // Select the text to be copied
        var finalSequence = document.getElementById('finalSeq').textContent;
        // Create a temporary textarea element to hold the text
        var tempTextArea = document.createElement('textarea');
        tempTextArea.value = finalSequence;
        document.body.appendChild(tempTextArea);
        // Select the text within the textarea
        tempTextArea.select();
        tempTextArea.setSelectionRange(0, 99999);
        // Copy the selected text to the clipboard
        document.execCommand('copy');
        // Remove the temporary textarea
        document.body.removeChild(tempTextArea);
        alert('Final sequence copied to clipboard!');
    });

    $('#exportToTxtBtn').on('click', function() {
        var sequenceContent = $('#finalSeq').text();
        var blob = new Blob([sequenceContent], { type: 'text/plain' });
        var url = URL.createObjectURL(blob);
        var link = document.createElement('a');
        link.setAttribute('href', url);
        link.setAttribute('download', 'sequence.txt');
        document.body.appendChild(link);
        link.click();
    });
});