(function () {

    const quotesEl = document.querySelector('.leaderboardPlayersList');
    const loaderEl = document.querySelector('.loader');
    const loadingIcon = document.querySelector('.lds-ripple');
	let currentMember = 0;
    // get the quotes from API
    const getQuotes = async (page, limit) => {
        const API_URL = `https://gtaseriesvideos.com/proxy/users/all?page=${page}&size=${limit}&sort=totalXpAcquired,desc`;
        const response = await fetch(API_URL);
        // handle 404
        if (!response.ok) {
            throw new Error(`An error occurred: ${response.status}`);
        }
        return await response.json();
    }
	
	function kFormatter(num) {
		return Math.abs(num) > 999 ? Math.sign(num)*((Math.abs(num)/1000).toFixed(1)) + 'k' : Math.sign(num)*Math.abs(num)
	}
	
	function getPercent(num1, num2){
		return Math.round((num1 * 100.0) / num2);
	}

    // show the quotes
    const showQuotes = (quotes) => {
        quotes.forEach(rankUser => {
            const quoteEl = document.createElement('player');
			let specialRank = "";
			if(currentMember == 0){
				specialRank = "leaderboardRankFirst";
			}else if(currentMember == 1){
				specialRank = "leaderboardRankSecond";
			}else if(currentMember == 2){
				specialRank = "leaderboardRankThird";
			}
			let percent = getPercent(rankUser.currentXp, rankUser.xpRequiredToNextRank);
			let over50String = percent > 50 ? "over50" : "";
			
            quoteEl.innerHTML = `<div class="leaderboardPlayer">
                        <div class="leaderboardPlayerLeft">
                           <div class="leaderboardRank ${specialRank}">${currentMember + 1}</div>
						   <div class="leaderboardPlayerIcon"><img onerror="this.src='https://cdn.discordapp.com/embed/avatars/1.png';" src="${rankUser.lastUpdatedAvatar}"></div>
                           <div class="leaderboardPlayerUsername">${rankUser.lastUsername}</div>
                        </div>
                        <div class="leaderboardPlayerStats">
                           <div class="leaderboardPlayerStatBlock remove-mobile nonpriority">
                              <div class="leaderboardPlayerStatName">MESSAGES
                              </div>
                              <div class="leaderboardPlayerStatValue">${kFormatter(rankUser.numOfMessages)}
                              </div>
                           </div>
                           <div class="leaderboardPlayerStatBlock nonpriority">
                              <div class="leaderboardPlayerStatName">EXPERIENCE
                              </div>
                              <div class="leaderboardPlayerStatValue">${kFormatter(rankUser.totalXpAcquired)}
                              </div>
                           </div>
                           <div class="leaderboardPlayerStatBlock">
                              <div class="progress-circle ${over50String} p${percent}">
                                 <span>
                                    <div class="leaderboardPlayerStatName" style="margin-right: 1%; margin-top: 25%;">Level
                                    </div>
                                    <div class="leaderboardPlayerStatValue" style="margin-right: 3%;">${rankUser.currentLevel}
                                    </div>
                                 </span>
                                 <div class="left-half-clipper">
                                    <div class="first50-bar"></div>
                                    <div class="value-bar"></div>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                     <div class="leaderboardPlayerSep"></div>`;
					 
			currentMember++;
            quotesEl.appendChild(quoteEl);
        });
    };

    const hideLoader = () => {
        loadingIcon.classList.remove('showLoading');
    };

    const showLoader = () => {
        loadingIcon.classList.add('showLoading');
    };

    const hasMoreQuotes = (page, limit, total) => {
        const startIndex = (page - 1) * limit + 1;
        return total === 0 || startIndex < total;
    };

    // load quotes
    const loadQuotes = async (page, limit) => {

        // show the loader
        showLoader();
        // 0.5 second later
        setTimeout(async () => {
            try {
                // if having more quotes to fetch
                if (hasMoreQuotes(page, limit, total)) {
                    // call the API to get quotes
                    const response = await getQuotes(page, limit);
                    // show quotes
                    showQuotes(response.content);
                    // update the total
                    total = response.totalElements;
                }
            } catch (error) {
                console.log(error.message);
            } finally {
                hideLoader();
            }
        }, 500);

    };

    // control variables
    let currentPage = 0;
    const limit = 30;
    let total = 0;


    window.addEventListener('scroll', () => {
        const {
            scrollTop,
            scrollHeight,
            clientHeight
        } = document.documentElement;

        if (scrollTop + clientHeight >= scrollHeight - 15 &&
            hasMoreQuotes(currentPage, limit, total)) {
            currentPage++;
            loadQuotes(currentPage, limit);
        }
    }, {
        passive: true
    });

    // initialize
    loadQuotes(currentPage, limit);

})();