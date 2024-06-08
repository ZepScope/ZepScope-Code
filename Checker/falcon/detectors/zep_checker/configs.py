
string_sim_threshold=0.6
infothreshold=0.9
MATCH_NUM=3
EXTRACT_ERROR_MSG=True
import gensim.downloader as api
model = api.load('glove-wiki-gigaword-50')
def_req={
    "ERC721._safeMint(address,uint256) returns()": [
        [
            [
                "_checkOnERC721Received(address(0),to,tokenId,data)"
            ],
            "#High#ERROR_MSG:ERC721: transfer to non ERC721Receiver implementer"
        ],
        [
            "NEQ",
            [
                "to",
                "address_1",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: mint to the zero address"
        ],
        [
            "NOT",
            [
                "_exists(tokenId)",
                [
                    "NEQ",
                    [
                        "_ownerOf(tokenId)",
                        [
                            "_owners@tokenId"
                        ]
                    ],
                    [
                        "address(0)"
                    ]
                ]
            ],
            "#Low#ERROR_MSG:ERC721: token already minted"
        ]
    ],
    "IGovernorCompatibilityBravo.queue(uint256) returns()": [],
    "ERC20VotesLegacyMock._afterTokenTransfer(address,address,uint256) returns()": [
        [
            "LTE",
            [
                "value",
                "newWeight"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ]
    ],
    "Governor.proposalThreshold() returns(uint256)": [],
    "Governor.constructor(string) returns()": [],
    "BridgeOptimismMock.xDomainMessageSender() returns(address)": [],
    "Governor.name() returns(string)": [],
    "IGovernor.castVote(uint256,uint8) returns(uint256)": [],
    "ERC721._exists(uint256) returns(bool)": [],
    "ERC721.constructor(string,string) returns()": [],
    "ERC20._beforeTokenTransfer(address,address,uint256) returns()": [],
    "ERC20._afterTokenTransfer(address,address,uint256) returns()": [],
    "ERC20._transfer(address,address,uint256) returns()": [
        [
            "NEQ",
            [
                "from",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: transfer to the zero address"
        ],
        [
            "NEQ",
            [
                "to",
                "address_2"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: transfer to the zero address"
        ],
        [
            "GTE",
            [
                "_balances@from",
                "fromBalance"
            ],
            [
                "amount",
                "uint256_1"
            ],
            "#Medium#ERROR_MSG:ERC20: transfer amount exceeds balance"
        ]
    ],
    "ERC20.increaseAllowance(address,uint256) returns(bool)": [
        [
            "NEQ",
            [
                "owner",
                "_msgSender()",
                "msgsender"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve from the zero address"
        ],
        [
            "NEQ",
            [
                "spender",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve to the zero address"
        ]
    ],
    "EIP712._buildDomainSeparator() returns(bytes32)": [],
    "Pausable._requirePaused() returns()": [],
    "Initializable._isInitializing() returns(bool)": [],
    "IGovernorCompatibilityBravo.execute(uint256) returns()": [],
    "Governor.getVotesWithParams(address,uint256,bytes) returns(uint256)": [],
    "ERC4626.deposit(uint256,address) returns(uint256)": [
        [
            "LTE",
            [
                "assets",
                "uint256_1",
                "x",
                "value"
            ],
            [
                "maxDeposit(receiver)",
                "max@type()(uint256)"
            ],
            "#Medium#ERROR_MSG:ERC4626: deposit more than max"
        ],
        [
            "NEQ",
            [
                "to",
                "account",
                "address_1",
                "receiver"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: mint to the zero address"
        ],
        [
            [
                [
                    "EQ",
                    [
                        "length@functionCall(data,SafeERC20: low-level call failed)",
                        "length@returndata"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ],
                [
                    "decode(returndata,(bool))"
                ]
            ],
            "#High#ERROR_MSG:SafeERC20: ERC20 operation did not succeed"
        ],
        [
            "GT",
            [
                "denominator"
            ],
            [
                "prod1"
            ],
            "#Medium#:Math: mulDiv overflow"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "BridgePolygonChildMock.relayAs(address,bytes,address) returns()": [],
    "ERC20VotesLegacyMock._delegate(address,address) returns()": [
        [
            "LTE",
            [
                "value",
                "newWeight"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ]
    ],
    "ERC721ReceiverMock.onERC721Received(address,address,uint256,bytes) returns(bytes4)": [],
    "ERC20Votes._writeCheckpoint(ERC20Votes.Checkpoint[],function(uint256,uint256) returns(uint256),uint256) returns(uint256,uint256)": [
        [
            "LTE",
            [
                "value",
                "newWeight"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "Governor.proposalSnapshot(uint256) returns(uint256)": [],
    "IGovernor.proposalDeadline(uint256) returns(uint256)": [],
    "ERC20._burn(address,uint256) returns()": [
        [
            "NEQ",
            [
                "from",
                "account",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#:ERC20: burn from the zero address"
        ],
        [
            "GTE",
            [
                "_balances@from",
                "_balances@account",
                "accountBalance"
            ],
            [
                "amount",
                "uint256_1"
            ],
            "#Medium#:ERC20: burn amount exceeds balance"
        ]
    ],
    "Governor.cancel(address[],uint256[],bytes[],bytes32) returns(uint256)": [
        [
            "EQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Pending@ProposalState"
            ],
            "#Medium#:Governor: too late to cancel"
        ],
        [
            "EQ",
            [
                "_msgSender()",
                "msgsender"
            ],
            [
                "proposer@_proposals@hashProposal(targets,values,calldatas,descriptionHash)",
                "proposer@_proposals@encode(targets,values,calldatas,descriptionHash)))",
                "proposer@_proposals@proposalId"
            ],
            "#High#:Governor: only proposer can cancel"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Canceled@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "EQ",
            [
                "0"
            ],
            [
                "proposalSnapshot(proposalId)",
                "REF_1872",
                "voteStart@_proposals@hashProposal(targets,values,calldatas,descriptionHash)",
                "voteStart@_proposals@encode(targets,values,calldatas,descriptionHash)))",
                "voteStart@_proposals@proposalId",
                "snapshot",
                "voteStart@proposal"
            ],
            "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
        ]
    ],
    "Pausable._pause() returns()": [
        [
            "whenNotPaused"
        ]
    ],
    "IGovernorCompatibilityBravo.cancel(uint256) returns()": [],
    "Receiver.crossChainRestricted() returns()": [
        [
            "onlyCrossChain"
        ]
    ],
    "ERC20VotesLegacyMock._moveVotingPower(address,address,uint256) returns()": [
        [
            "LTE",
            [
                "value",
                "newWeight"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ]
    ],
    "IGovernor.cancel(address[],uint256[],bytes[],bytes32) returns(uint256)": [],
    "ERC1967Proxy.constructor(address,bytes) returns()": [],
    "ShortStrings.slitherConstructorConstantVariables() returns()": [],
    "PullPayment._asyncTransfer(address,uint256) returns()": [
        [
            [
                "onlyOwner",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ]
    ],
    "IGovernorCompatibilityBravo.getActions(uint256) returns(address[],uint256[],string[],bytes[])": [],
    "Governor._castVote(uint256,address,uint8,string) returns(uint256)": [
        [
            "EQ",
            [
                "state(proposalId)"
            ],
            [
                "Active@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: vote not currently active"
        ],
        [
            "EQ",
            [
                "0"
            ],
            [
                "proposalSnapshot(proposalId)",
                "REF_1872",
                "voteStart@_proposals@proposalId",
                "voteStart@proposal",
                "snapshot"
            ],
            "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
        ]
    ],
    "Votes._moveDelegateVotes(address,address,uint256) returns()": [
        [
            "LTE",
            [
                "value",
                "uint256_1",
                "amount"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ],
        [
            "LTE",
            [
                "_key@_unsafeAccess(self,pos - 1)",
                "_key@last"
            ],
            [
                "key"
            ],
            "#Medium#ERROR_MSG:Checkpoint: decreasing keys"
        ]
    ],
    "GovernorVotesQuorumFraction.constructor(uint256) returns()": [],
    "ERC20VotesLegacyMock._writeCheckpoint(ERC20VotesLegacyMock.Checkpoint[],function(uint256,uint256) returns(uint256),uint256) returns(uint256,uint256)": [
        [
            "LTE",
            [
                "value",
                "newWeight"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ]
    ],
    "Governor.supportsInterface(bytes4) returns(bool)": [],
    "ERC1967Proxy._implementation() returns(address)": [],
    "Pausable._unpause() returns()": [
        [
            "whenPaused"
        ]
    ],
    "Receiver.crossChainOwnerRestricted() returns()": [
        [
            "onlyCrossChainSender"
        ]
    ],
    "Governor._tryHexToUint(bytes1) returns(bool,uint8)": [],
    "ERC1155._beforeTokenTransfer(address,address,address,uint256[],uint256[],bytes) returns()": [],
    "IGovernorCompatibilityBravo.getReceipt(uint256,address) returns(IGovernorCompatibilityBravo.Receipt)": [],
    "ERC20.constructor(string,string) returns()": [],
    "ERC20._approve(address,address,uint256) returns()": [
        [
            "NEQ",
            [
                "owner",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve from the zero address"
        ],
        [
            "NEQ",
            [
                "spender",
                "address_2"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve to the zero address"
        ]
    ],
    "ERC20VotesLegacyMock._add(uint256,uint256) returns(uint256)": [],
    "UpgradeableBeacon.constructor(address) returns()": [],
    "Context._msgSender() returns(address)": [],
    "CrossChainEnabledAMBMock.constructor(address) returns()": [],
    "ERC4626.totalAssets() returns(uint256)": [],
    "EIP712.eip712Domain() returns(bytes1,string,string,uint256,address,bytes32,uint256[])": [
        [
            "LTE",
            [
                "31"
            ],
            [
                "result",
                "unwrap(sstr)) & 0xFF"
            ],
            "#Low#ERROR_MSG:InvalidShortString()()"
        ]
    ],
    "IGovernor.votingDelay() returns(uint256)": [],
    "Governor.hashProposal(address[],uint256[],bytes[],bytes32) returns(uint256)": [],
    "Governor.proposalDeadline(uint256) returns(uint256)": [],
    "IGovernorTimelock.timelock() returns(address)": [],
    "ERC20VotesLegacyMock._subtract(uint256,uint256) returns(uint256)": [],
    "ERC721.isApprovedForAll(address,address) returns(bool)": [],
    "ERC721.balanceOf(address) returns(uint256)": [
        [
            "NEQ",
            [
                "owner",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: address zero is not a valid owner"
        ]
    ],
    "CrossChainEnabledArbitrumL1Mock.constructor(address) returns()": [],
    "Governor.castVoteWithReason(uint256,uint8,string) returns(uint256)": [
        [
            "EQ",
            [
                "state(proposalId)"
            ],
            [
                "Active@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: vote not currently active"
        ],
        [
            "EQ",
            [
                "0"
            ],
            [
                "proposalSnapshot(proposalId)",
                "REF_1872",
                "voteStart@_proposals@proposalId",
                "voteStart@proposal",
                "snapshot"
            ],
            "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
        ]
    ],
    "Context._msgData() returns(bytes)": [],
    "UpgradeableBeacon.implementation() returns(address)": [],
    "ERC20.decreaseAllowance(address,uint256) returns(bool)": [
        [
            "GTE",
            [
                "allowance(owner,spender)",
                "currentAllowance",
                "_allowances@owner@spender"
            ],
            [
                "uint256_1",
                "subtractedValue"
            ],
            "#High#ERROR_MSG:ERC20: decreased allowance below zero"
        ],
        [
            "NEQ",
            [
                "owner",
                "_msgSender()",
                "msgsender"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve from the zero address"
        ],
        [
            "NEQ",
            [
                "spender",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve to the zero address"
        ]
    ],
    "IGovernorTimelock.proposalEta(uint256) returns(uint256)": [],
    "ERC721._mint(address,uint256) returns()": [
        [
            "NEQ",
            [
                "to",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: mint to the zero address"
        ],
        [
            "NOT",
            [
                "_exists(tokenId)",
                [
                    "NEQ",
                    [
                        "_ownerOf(tokenId)",
                        [
                            "_owners@tokenId"
                        ]
                    ],
                    [
                        "address(0)"
                    ]
                ]
            ],
            "#Low#ERROR_MSG:ERC721: token already minted"
        ]
    ],
    "ERC20VotesLegacyMock._unsafeAccess(ERC20VotesLegacyMock.Checkpoint[],uint256) returns(ERC20VotesLegacyMock.Checkpoint)": [],
    "Governor.proposalProposer(uint256) returns(address)": [],
    "ERC20Permit.slitherConstructorConstantVariables() returns()": [],
    "CrossChainEnabledOptimismMock.constructor(address) returns()": [],
    "UpgradeableBeacon.upgradeTo(address) returns()": [
        [
            [
                "onlyOwner",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ],
        [
            [
                "isContract(newImplementation)"
            ],
            "#Low#ERROR_MSG:UpgradeableBeacon: implementation is not a contract"
        ]
    ],
    "GovernorCompatibilityBravo.queue(uint256) returns()": [],
    "IGovernorTimelock.queue(address[],uint256[],bytes[],bytes32) returns(uint256)": [],
    "Initializable.reinitializer(uint8) returns()": [
        [
            "NOT",
            [
                "_initializing",
                "bool"
            ],
            "#Low#ERROR_MSG:Initializable: contract is already initialized"
        ],
        [
            "LT",
            [
                "_initialized",
                "uint8"
            ],
            [
                "uint8_1",
                "version"
            ],
            "#Low#ERROR_MSG:Initializable: contract is already initialized"
        ]
    ],
    "GovernorVotesQuorumFraction.quorumNumerator(uint256) returns(uint256)": [
        [
            "LTE",
            [
                "value",
                "timepoint",
                "uint256_1"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ]
    ],
    "ERC4626.withdraw(uint256,address,address) returns(uint256)": [
        [
            "LTE",
            [
                "uint256_1",
                "assets",
                "x",
                "shares",
                "value"
            ],
            [
                "maxWithdraw(owner)",
                "Down"
            ],
            "#Medium#ERROR_MSG:ERC4626: withdraw more than max"
        ],
        [
            "NEQ",
            [
                "owner",
                "account",
                "from",
                "address_2"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: burn from the zero address"
        ],
        [
            "GTE",
            [
                "_balances@from",
                "_balances@account",
                "_balances@owner",
                "accountBalance"
            ],
            [
                "shares",
                "amount",
                "Up)",
                "previewWithdraw(assets)"
            ],
            "#Medium#ERROR_MSG:ERC20: burn amount exceeds balance"
        ],
        [
            "GTE",
            [
                "allowance(owner,spender)",
                "_allowances@owner@spender",
                "_allowances@owner@caller",
                "currentAllowance"
            ],
            [
                "shares",
                "amount",
                "Up)",
                "previewWithdraw(assets)"
            ],
            "#High#ERROR_MSG:ERC20: insufficient allowance"
        ],
        [
            "NEQ",
            [
                "owner",
                "account",
                "from",
                "address_2"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve from the zero address"
        ],
        [
            "NEQ",
            [
                "spender",
                "caller"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve to the zero address"
        ],
        [
            [
                [
                    "EQ",
                    [
                        "length@functionCall(data,SafeERC20: low-level call failed)",
                        "length@returndata"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ],
                [
                    "decode(returndata,(bool))"
                ]
            ],
            "#Medium#ERROR_MSG:SafeERC20: ERC20 operation did not succeed"
        ],
        [
            "GT",
            [
                "denominator"
            ],
            [
                "prod1"
            ],
            "#Medium#ERROR_MSG:Math: mulDiv overflow"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "Governor.version() returns(string)": [],
    "ERC4626OffsetMock.constructor(uint8) returns()": [],
    "Governor.propose(address[],uint256[],bytes[],string) returns(uint256)": [
        [
            [
                "_isValidDescriptionForProposer(proposer,description)"
            ],
            "#High#ERROR_MSG:Governor: proposer restricted"
        ],
        [
            "GTE",
            [
                "getVotes(proposer,currentTimepoint - 1)",
                "_getVotes(account,timepoint,_defaultParams())"
            ],
            [
                "proposalThreshold()",
                "1000e18"
            ],
            "#Medium#ERROR_MSG:Governor: proposer votes below proposal threshold"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@values"
            ],
            "#Medium#ERROR_MSG:Governor: invalid proposal length"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@calldatas"
            ],
            "#Low#ERROR_MSG:Governor: invalid proposal length"
        ],
        [
            "GT",
            [
                "length@targets"
            ],
            [
                "0"
            ],
            "#Low#ERROR_MSG:Governor: empty proposal"
        ],
        [
            "EQ",
            [
                "voteStart@_proposals@hashProposal(targets,values,calldatas,keccak256(bytes)(bytes(description)))",
                "voteStart@_proposals@encode(targets,values,calldatas,descriptionHash)))",
                "voteStart@_proposals@proposalId"
            ],
            [
                "0"
            ],
            "#Low#ERROR_MSG:Governor: proposal already exists"
        ],
        [
            "LTE",
            [
                "value",
                "snapshot",
                "deadline",
                "snapshot + votingPeriod()",
                "currentTimepoint + votingDelay()"
            ],
            [
                "max@type()(uint64)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 64 bits"
        ]
    ],
    "ERC20._spendAllowance(address,address,uint256) returns()": [
        [
            "GTE",
            [
                "allowance(owner,spender)",
                "currentAllowance",
                "_allowances@owner@spender"
            ],
            [
                "uint256_1",
                "amount"
            ],
            "#High#ERROR_MSG:ERC20: insufficient allowance"
        ],
        [
            "NEQ",
            [
                "owner",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve from the zero address"
        ],
        [
            "NEQ",
            [
                "spender",
                "address_2"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve to the zero address"
        ]
    ],
    "BadBeaconNotContract.implementation() returns(address)": [],
    "UpgradeableBeacon._setImplementation(address) returns()": [
        [
            [
                "isContract(newImplementation)"
            ],
            "#Medium#ERROR_MSG:UpgradeableBeacon: implementation is not a contract"
        ]
    ],
    "ERC4626.convertToAssets(uint256) returns(uint256)": [
        [
            "GT",
            [
                "denominator"
            ],
            [
                "prod1"
            ],
            "#Medium#ERROR_MSG:Math: mulDiv overflow"
        ]
    ],
    "ClashingImplementation.admin() returns(address)": [],
    "ERC4626OffsetMock._decimalsOffset() returns(uint8)": [],
    "ERC20.symbol() returns(string)": [],
    "ProxyAdmin.getProxyImplementation(ITransparentUpgradeableProxy) returns(address)": [],
    "IGovernor.castVoteWithReasonAndParams(uint256,uint8,string,bytes) returns(uint256)": [],
    "IGovernor.quorum(uint256) returns(uint256)": [],
    "ClashingImplementation.delegatedFunction() returns(bool)": [],
    "ERC4626FeesMock.constructor(uint256,address,uint256,address) returns()": [],
    "ProxyAdmin.getProxyAdmin(ITransparentUpgradeableProxy) returns(address)": [],
    "Votes._add(uint224,uint224) returns(uint224)": [],
    "ERC1155.supportsInterface(bytes4) returns(bool)": [],
    "IGovernor.votingPeriod() returns(uint256)": [],
    "Governor._quorumReached(uint256) returns(bool)": [],
    "GovernorCountingSimple.slitherConstructorConstantVariables() returns()": [],
    "GovernorCompatibilityBravo.cancel(uint256) returns()": [
        [
            [
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "proposer@_proposalDetails@encode(targets,values,calldatas,descriptionHash)))",
                        "proposer@details",
                        "proposer@_proposalDetails@hashProposal(targets,values,calldatas,descriptionHash)",
                        "proposer",
                        "proposer@_proposalDetails@proposalId",
                        "account"
                    ]
                ],
                [
                    "LT",
                    [
                        "getVotes(proposer,clock() - 1)",
                        "_getVotes(account,timepoint,_defaultParams())"
                    ],
                    [
                        "proposalThreshold()",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:GovernorBravo: proposer above threshold"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Canceled@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Expired@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Executed@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "EQ",
            [
                "0"
            ],
            [
                "proposalSnapshot(proposalId)",
                "REF_1872",
                "voteStart@_proposals@encode(targets,values,calldatas,descriptionHash)))",
                "voteStart@_proposals@proposalId",
                "snapshot",
                "voteStart@_proposals@hashProposal(targets,values,calldatas,descriptionHash)",
                "voteStart@proposal"
            ],
            "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
        ]
    ],
    "NonUpgradeableMock.current() returns(uint256)": [],
    "SampleFather.initialize(string,uint256) returns()": [
        [
            "initializer"
        ],
        [
            [
                [
                    [
                        "! _initializing",
                        "isTopLevelCall"
                    ],
                    [
                        "LT",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ],
                [
                    [
                        "NOT",
                        [
                            "isContract(address(this))"
                        ]
                    ],
                    [
                        "EQ",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ]
            ],
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ],
        [
            "onlyInitializing"
        ],
        [
            "_initializing",
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "ProxyAdmin.changeProxyAdmin(ITransparentUpgradeableProxy,address) returns()": [
        [
            [
                "onlyOwner",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ]
    ],
    "ERC20.name() returns(string)": [],
    "ERC721.name() returns(string)": [],
    "Governor.state(uint256) returns(IGovernor.ProposalState)": [
        [
            "EQ",
            [
                "0"
            ],
            [
                "proposalSnapshot(proposalId)",
                "REF_1872",
                "voteStart@_proposals@proposalId",
                "snapshot"
            ],
            "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
        ]
    ],
    "ERC721.safeTransferFrom(address,address,uint256) returns()": [
        [
            [
                "_isApprovedOrOwner(_msgSender(),tokenId)",
                "_isApprovedOrOwner(msgsender,tokenId)",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "spender"
                    ],
                    [
                        "ownerOf(tokenId)",
                        "owner"
                    ]
                ],
                "isApprovedForAll(_msgSender(),tokenId)",
                "isApprovedForAll(msgsender,tokenId)",
                "_operatorApprovals@_msgSender()@tokenId",
                "_operatorApprovals@msgsender@tokenId",
                [
                    "EQ",
                    "getApproved(tokenId)",
                    [
                        "_msgSender()",
                        "msgsender"
                    ]
                ]
            ],
            "#High#ERROR_MSG:ERC721: caller is not token owner or approved"
        ],
        [
            [
                "_checkOnERC721Received(from,to,tokenId,data)"
            ],
            "#High#ERROR_MSG:ERC721: transfer to non ERC721Receiver implementer"
        ],
        [
            "EQ",
            [
                "ownerOf(tokenId)",
                "owner"
            ],
            [
                "from",
                "address_1"
            ],
            "#Medium#ERROR_MSG:ERC721: transfer from incorrect owner"
        ],
        [
            "NEQ",
            [
                "to",
                "address_2",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC721: transfer to the zero address"
        ],
        [
            "NEQ",
            [
                "_ownerOf(tokenId)",
                "_owners@tokenId",
                "_owners@firstTokenId",
                "owner"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: invalid token ID"
        ]
    ],
    "ProxyAdmin.upgrade(ITransparentUpgradeableProxy,address) returns()": [
        [
            [
                "onlyOwner",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ]
    ],
    "AccessControl.renounceRole(bytes32,address) returns()": [
        [
            "EQ",
            [
                "account",
                "address_1"
            ],
            [
                "_msgSender()",
                "msgsender"
            ],
            "#High#ERROR_MSG:AccessControl: can only renounce roles for self"
        ]
    ],
    "ERC721Wrapper.depositFor(address,uint256[]) returns(bool)": [
        [
            [
                "_checkOnERC721Received(address(0),to,tokenId,data)"
            ],
            "#High#ERROR_MSG:ERC721: transfer to non ERC721Receiver implementer"
        ],
        [
            "NEQ",
            [
                "to",
                "account",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: mint to the zero address"
        ],
        [
            "NOT",
            [
                "_exists(tokenId)",
                [
                    "NEQ",
                    [
                        "_ownerOf(tokenId)",
                        [
                            "_owners@tokenId"
                        ]
                    ],
                    [
                        "address(0)"
                    ]
                ]
            ],
            "#Low#ERROR_MSG:ERC721: token already minted"
        ]
    ],
    "GovernorTimelockControl._executor() returns(address)": [],
    "ERC721._requireMinted(uint256) returns()": [],
    "IGovernor.CLOCK_MODE() returns(string)": [],
    "Votes._useNonce(address) returns(uint256)": [],
    "GovernorVotes.constructor(IVotes) returns()": [],
    "ERC721Wrapper.withdrawTo(address,uint256[]) returns(bool)": [
        [
            [
                "_isApprovedOrOwner(_msgSender(),tokenId)",
                "_isApprovedOrOwner(msgsender,tokenId)",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "spender"
                    ],
                    [
                        "ownerOf(tokenId)",
                        "owner"
                    ]
                ],
                "isApprovedForAll(_msgSender(),tokenId)",
                "isApprovedForAll(msgsender,tokenId)",
                "_operatorApprovals@_msgSender()@tokenId",
                "_operatorApprovals@msgsender@tokenId",
                [
                    "EQ",
                    "getApproved(tokenId)",
                    [
                        "_msgSender()",
                        "msgsender"
                    ]
                ]
            ],
            "#High#ERROR_MSG:ERC721Wrapper: caller is not token owner or approved"
        ],
        [
            "NEQ",
            [
                "_ownerOf(tokenId)",
                "_owners@tokenId",
                "_owners@tokenIds@i",
                "_owners@firstTokenId",
                "owner"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: invalid token ID"
        ]
    ],
    "ERC20Votes.numCheckpoints(address) returns(uint32)": [
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ]
    ],
    "ERC1820Implementer.slitherConstructorConstantVariables() returns()": [],
    "Votes.nonces(address) returns(uint256)": [],
    "ERC777.burn(uint256,bytes) returns()": [
        [
            "NEQ",
            [
                "account",
                "from"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC777: burn from the zero address"
        ],
        [
            "GTE",
            [
                "fromBalance",
                "_balances@from",
                "_balances@account"
            ],
            [
                "amount",
                "uint256_1"
            ],
            "#Medium#ERROR_MSG:ERC777: burn amount exceeds balance"
        ]
    ],
    "Governor._execute(uint256,address[],uint256[],bytes[],bytes32) returns()": [
    ],
    "ERC721Wrapper.onERC721Received(address,address,uint256,bytes) returns(bytes4)": [
        [
            "EQ",
            [
                "address(underlying())"
            ],
            [
                "_msgSender()",
                "msgsender"
            ],
            "#High#ERROR_MSG:ERC721Wrapper: caller is not underlying"
        ],
        [
            [
                "_checkOnERC721Received(address(0),to,tokenId,data)"
            ],
            "#High#ERROR_MSG:ERC721: transfer to non ERC721Receiver implementer"
        ],
        [
            "NEQ",
            [
                "to",
                "from",
                "address_2",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: mint to the zero address"
        ],
        [
            "NOT",
            [
                "_exists(tokenId)",
                [
                    "NEQ",
                    [
                        "_ownerOf(tokenId)",
                        [
                            "_owners@tokenId"
                        ]
                    ],
                    [
                        "address(0)"
                    ]
                ]
            ],
            "#Low#ERROR_MSG:ERC721: token already minted"
        ]
    ],
    "Votes.DOMAIN_SEPARATOR() returns(bytes32)": [],
    "GovernorCountingSimple.proposalVotes(uint256) returns(uint256,uint256,uint256)": [],
    "ERC721Wrapper._recover(address,uint256) returns(uint256)": [
        [
            "EQ",
            [
                "ownerOf(tokenId)"
            ],
            [
                "address(this)"
            ],
            "#High#ERROR_MSG:ERC721Wrapper: wrapper is not token owner"
        ],
        [
            [
                "_checkOnERC721Received(address(0),to,tokenId,data)"
            ],
            "#High#ERROR_MSG:ERC721: transfer to non ERC721Receiver implementer"
        ],
        [
            "NEQ",
            [
                "to",
                "account",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: mint to the zero address"
        ],
        [
            "NOT",
            [
                "_exists(tokenId)",
                [
                    "NEQ",
                    [
                        "_ownerOf(tokenId)",
                        [
                            "_owners@tokenId"
                        ]
                    ],
                    [
                        "address(0)"
                    ]
                ]
            ],
            "#Low#ERROR_MSG:ERC721: token already minted"
        ]
    ],
    "GovernorVotes.CLOCK_MODE() returns(string)": [],
    "ERC4626.previewDeposit(uint256) returns(uint256)": [
        [
            "GT",
            [
                "denominator"
            ],
            [
                "prod1"
            ],
            "#Medium#ERROR_MSG:Math: mulDiv overflow"
        ]
    ],
    "Governor.relay(address,uint256,bytes) returns()": [
        [
            [
                "onlyGovernance"
            ],
            [
                "EQ",
                [
                    "_msgSender()",
                    "msgsender"
                ],
                [
                    "_executor()",
                    "address(this)"
                ]
            ],
            "#High#ERROR_MSG:Governor: onlyGovernance"
        ]
    ],
    "Votes._getVotingUnits(address) returns(uint256)": [],
    "IVotes.getPastVotes(address,uint256) returns(uint256)": [],
    "ERC20Votes.checkpoints(address,uint32) returns(ERC20Votes.Checkpoint)": [],
    "AccessControlEnumerable.getRoleMemberCount(bytes32) returns(uint256)": [],
    "ERC721Wrapper.underlying() returns(IERC721)": [],
    "ERC721._safeTransfer(address,address,uint256,bytes) returns()": [
        [
            [
                "_checkOnERC721Received(from,to,tokenId,data)"
            ],
            "#High#ERROR_MSG:ERC721: transfer to non ERC721Receiver implementer"
        ],
        [
            "EQ",
            [
                "ownerOf(tokenId)"
            ],
            [
                "from",
                "address_1"
            ],
            "#Medium#ERROR_MSG:ERC721: transfer from incorrect owner"
        ],
        [
            "NEQ",
            [
                "to",
                "address_2",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC721: transfer to the zero address"
        ],
        [
            "NEQ",
            [
                "_ownerOf(tokenId)",
                "_owners@tokenId",
                "_owners@firstTokenId",
                "_owners@index",
                "owner"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: invalid token ID"
        ]
    ],
    "IGovernor.hashProposal(address[],uint256[],bytes[],bytes32) returns(uint256)": [],
    "ERC20Mock.constructor() returns()": [],
    "IGovernor.proposalSnapshot(uint256) returns(uint256)": [],
    "ERC1967Upgrade._setImplementation(address) returns()": [
        [
            [
                "isContract(newImplementation)"
            ],
            "#Medium#ERROR_MSG:ERC1967: new implementation is not a contract"
        ]
    ],
    "ERC721PresetMinterPauserAutoId.constructor(string,string,string) returns()": [],
    "AccessControl._setRoleAdmin(bytes32,bytes32) returns()": [],
    "ERC721._beforeTokenTransfer(address,address,uint256,uint256) returns()": [],
    "ERC20Mock.mint(address,uint256) returns()": [
        [
            "NEQ",
            [
                "to",
                "account",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: mint to the zero address"
        ]
    ],
    "Votes._transferVotingUnits(address,address,uint256) returns()": [
        [
            "LTE",
            [
                "value",
                "amount",
                "uint256_1"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ],
        [
            "LTE",
            [
                "_key@_unsafeAccess(self,pos - 1)",
                "_key@last"
            ],
            [
                "key"
            ],
            "#Medium#ERROR_MSG:Checkpoint: decreasing keys"
        ]
    ],
    "BridgeArbitrumL1Inbox.slitherConstructorVariables() returns()": [],
    "ERC20Mock.burn(address,uint256) returns()": [
        [
            "NEQ",
            [
                "account",
                "address_1",
                "from"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: burn from the zero address"
        ],
        [
            "GTE",
            [
                "_balances@from",
                "_balances@account",
                "accountBalance"
            ],
            [
                "amount",
                "uint256_1"
            ],
            "#Medium#ERROR_MSG:ERC20: burn amount exceeds balance"
        ]
    ],
    "GovernorCompatibilityBravo.slitherConstructorConstantVariables() returns()": [],
    "ERC20Votes.getVotes(address) returns(uint256)": [],
    "GovernorTimelockControl._updateTimelock(TimelockController) returns()": [],
    "ERC20Reentrant.scheduleReenter(ERC20Reentrant.Type,address,bytes) returns()": [],
    "ERC721PresetMinterPauserAutoId._baseURI() returns(string)": [],
    "ERC777.authorizeOperator(address) returns()": [
        [
            "NEQ",
            [
                "_msgSender()",
                "msgsender"
            ],
            [
                "operator",
                "address_1"
            ],
            "#Low#ERROR_MSG:ERC777: authorizing self as operator"
        ]
    ],
    "EnumerableMap.tryGet(EnumerableMap.Bytes32ToUintMap,bytes32) returns(bool,uint256)": [],
    "IGovernor.castVoteWithReasonAndParamsBySig(uint256,uint8,string,bytes,uint8,bytes32,bytes32) returns(uint256)": [],
    "ERC721PresetMinterPauserAutoId.mint(address) returns()": [
        [
            [
                "hasRole(MINTER_ROLE,_msgSender())",
                [
                    "members@_roles@role@account"
                ],
                "OnlyRole",
                [
                    "EQ",
                    [
                        "msgsender",
                        "_msgSender()"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth",
                        "gov"
                    ]
                ]
            ],
            "#High#ERROR_MSG:ERC721PresetMinterPauserAutoId: must have minter role to mint"
        ],
        [
            "NEQ",
            [
                "to",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: mint to the zero address"
        ],
        [
            "NOT",
            [
                "_exists(tokenId)",
                [
                    "NEQ",
                    [
                        "_ownerOf(tokenId)",
                        [
                            "_owners@tokenId"
                        ]
                    ],
                    [
                        "address(0)"
                    ]
                ]
            ],
            "#Low#ERROR_MSG:ERC721: token already minted"
        ]
    ],
    "Governor.onERC721Received(address,address,uint256,bytes) returns(bytes4)": [],
    "ERC4626.previewWithdraw(uint256) returns(uint256)": [
        [
            "GT",
            [
                "denominator"
            ],
            [
                "prod1"
            ],
            "#Medium#ERROR_MSG:Math: mulDiv overflow"
        ]
    ],
    "ERC1967Upgrade._upgradeToAndCall(address,bytes,bool) returns()": [
        [
            [
                "isContract(newImplementation)"
            ],
            "#Medium#ERROR_MSG:ERC1967: new implementation is not a contract"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "ERC20Votes.delegates(address) returns(address)": [],
    "ERC721PresetMinterPauserAutoId.pause() returns()": [
        [
            [
                "hasRole(PAUSER_ROLE,_msgSender())",
                [
                    "members@_roles@role@account"
                ],
                "onlyRole",
                [
                    "EQ",
                    [
                        "msgsender",
                        "_msgSender()"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth",
                        "gov"
                    ]
                ]
            ],
            "#High#ERROR_MSG:ERC721PresetMinterPauserAutoId: must have pauser role to pause"
        ],
        [
            "whenNotPaused"
        ]
    ],
    "IVotes.delegates(address) returns(address)": [],
    "ERC20._mint(address,uint256) returns()": [
        [
            "NEQ",
            [
                "to",
                "address_1",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: mint to the zero address"
        ]
    ],
    "ERC20Reentrant.functionCall(address,bytes) returns(bytes)": [
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "Governor._cancel(address[],uint256[],bytes[],bytes32) returns(uint256)": [
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Canceled@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Expired@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Executed@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "EQ",
            [
                "0"
            ],
            [
                "proposalSnapshot(proposalId)",
                "REF_1872",
                "voteStart@_proposals@encode(targets,values,calldatas,descriptionHash)))",
                "voteStart@_proposals@proposalId",
                "voteStart@_proposals@hashProposal(targets,values,calldatas,descriptionHash)",
                "snapshot",
                "voteStart@proposal"
            ],
            "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
        ]
    ],
    "AccessControlEnumerable._revokeRole(bytes32,address) returns()": [],
    "IGovernor.proposalProposer(uint256) returns(address)": [],
    "ERC20Votes._subtract(uint256,uint256) returns(uint256)": [],
    "GovernorCountingSimple._voteSucceeded(uint256) returns(bool)": [],
    "ERC721PresetMinterPauserAutoId.unpause() returns()": [
        [
            [
                "hasRole(PAUSER_ROLE,_msgSender())",
                [
                    "members@_roles@role@account"
                ],
                "onlyRole",
                [
                    "EQ",
                    [
                        "msgsender",
                        "_msgSender()"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth",
                        "gov"
                    ]
                ]
            ],
            "#High#ERROR_MSG:ERC721PresetMinterPauserAutoId: must have pauser role to unpause"
        ],
        [
            "whenPaused"
        ]
    ],
    "AccessControl._revokeRole(bytes32,address) returns()": [],
    "ERC20Reentrant._beforeTokenTransfer(address,address,uint256) returns()": [
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "Governor.slitherConstructorConstantVariables() returns()": [],
    "ERC4626.asset() returns(address)": [],
    "IGovernor.castVoteBySig(uint256,uint8,uint8,bytes32,bytes32) returns(uint256)": [],
    "IGovernor.execute(address[],uint256[],bytes[],bytes32) returns(uint256)": [],
    "Governor._executor() returns(address)": [],
    "AccessControl.hasRole(bytes32,address) returns(bool)": [],
    "ERC20.transfer(address,uint256) returns(bool)": [
        [
            "NEQ",
            [
                "owner",
                "from",
                "_msgSender()",
                "msgsender",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: transfer to the zero address"
        ],
        [
            "NEQ",
            [
                "to",
                "address_1",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: transfer to the zero address"
        ],
        [
            "GTE",
            [
                "_balances@from",
                "_balances@owner",
                "_balances@account",
                "_balances@_msgSender()",
                "fromBalance",
                "_balances@msgsender"
            ],
            [
                "amount",
                "delta",
                "uint256_1"
            ],
            "#Medium#ERROR_MSG:ERC20: transfer amount exceeds balance"
        ]
    ],
    "Governor._voteSucceeded(uint256) returns(bool)": [],
    "ERC165.supportsInterface(bytes4) returns(bool)": [],
    "AccessControl._checkRole(bytes32) returns()": [
        [
            "EQ",
            [
                "Strings.toHexString(uint256,uint256).value"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:Strings: hex length insufficient"
        ],
        [
            "NOT",
            [
                "hasRole(role,account)",
                [
                    "REF_605",
                    "members@_roles@role@account"
                ]
            ],
            "#High#ERROR_MSG:(string(abi.encodePacked(AccessControl: account ,Strings.toHexString(account), is missing role ,Strings.toHexString(uint256(role),32))))"
        ]
    ],
    "ERC4626.convertToShares(uint256) returns(uint256)": [
        [
            "GT",
            [
                "denominator"
            ],
            [
                "prod1"
            ],
            "#Medium#ERROR_MSG:Math: mulDiv overflow"
        ]
    ],
    "ERC721._ownerOf(uint256) returns(address)": [],
    "Governor.execute(address[],uint256[],bytes[],bytes32) returns(uint256)": [
        [
            [
                [
                    "EQ",
                    [
                        "state(proposalId)",
                        "currentState"
                    ],
                    [
                        "Succeeded@ProposalState"
                    ]
                ],
                [
                    "EQ",
                    [
                        "state(proposalId)",
                        "currentState"
                    ],
                    [
                        "Queued@ProposalState"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Governor: proposal not successful"
        ],
        [
            "EQ",
            [
                "id",
                "_timelockIds@",
                "_timelockIds@targets",
                "_timelockIds@values",
                "_timelockIds@descriptionHash",
                "_timelockIds@proposalId",
                "predecessor",
                "_timelockIds@salt",
                "_timelockIds@calldatas",
                "_timelockIds@payloads",
                "_timelockIds@encode(targets,values,calldatas,descriptionHash)))",
                "hashOperationBatch(targets,values,payloads,predecessor,salt)",
                "_timelockIds@hashProposal(targets,values,calldatas,descriptionHash)",
                "queueid",
                "encode(targets,values,payloads,predecessor,salt))",
                "0"
            ],
            [
                "proposalSnapshot(proposalId)",
                "REF_1872",
                "voteStart@_proposals@proposalId",
                "voteStart@_proposals@targets",
                "voteStart@_proposals@descriptionHash",
                "voteStart@_proposals@values",
                "voteStart@_proposals@salt",
                "snapshot",
                "voteStart@_proposals@calldatas",
                "voteStart@_proposals@hashProposal(targets,values,calldatas,descriptionHash)",
                "voteStart@_proposals@payloads",
                "voteStart@_proposals@",
                "voteStart@proposal",
                "voteStart@_proposals@encode(targets,values,calldatas,descriptionHash)))"
            ],
            "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
        ]
    ],
    "AccessControl.getRoleAdmin(bytes32) returns(bytes32)": [],
    "AccessControl._checkRole(bytes32,address) returns()": [
        [
            "EQ",
            [
                "Strings.toHexString(uint256,uint256).value"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:Strings: hex length insufficient"
        ],
        [
            "NOT",
            [
                "hasRole(role,account)",
                [
                    "REF_2147",
                    "members@_roles@role@account"
                ]
            ],
            "#High#ERROR_MSG:(string(abi.encodePacked(AccessControl: account ,Strings.toHexString(account), is missing role ,Strings.toHexString(uint256(role),32))))"
        ]
    ],
    "Governor._countVote(uint256,address,uint8,uint256,bytes) returns()": [],
    "ERC721.__unsafe_increaseBalance(address,uint256) returns()": [],
    "ERC20Wrapper.depositFor(address,uint256) returns(bool)": [
        [
            "NEQ",
            [
                "_msgSender()",
                "msgsender",
                "sender",
                "from"
            ],
            [
                "address(this)"
            ],
            "#Medium#ERROR_MSG:ERC20Wrapper: wrapper can't deposit"
        ],
        [
            "NEQ",
            [
                "account",
                "address_1",
                "to"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: mint to the zero address"
        ],
        [
            [
                [
                    "EQ",
                    [
                        "length@functionCall(data,SafeERC20: low-level call failed)",
                        "length@returndata"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ],
                [
                    "decode(returndata,(bool))"
                ]
            ],
            "#Medium#ERROR_MSG:SafeERC20: ERC20 operation did not succeed"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "Governor.castVoteWithReasonAndParams(uint256,uint8,string,bytes) returns(uint256)": [
        [
            "EQ",
            [
                "state(proposalId)"
            ],
            [
                "Active@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: vote not currently active"
        ],
        [
            "EQ",
            [
                "0"
            ],
            [
                "proposalSnapshot(proposalId)",
                "REF_1872",
                "voteStart@proposal",
                "voteStart@_proposals@proposalId",
                "snapshot"
            ],
            "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
        ]
    ],
    "GovernorVotesQuorumFraction._updateQuorumNumerator(uint256) returns()": [
        [
            "LTE",
            [
                "value",
                "uint256_1",
                "newQuorumNumerator"
            ],
            [
                "quorumDenominator()",
                "100"
            ],
            "#Medium#ERROR_MSG:GovernorVotesQuorumFraction: quorumNumerator over quorumDenominator"
        ],
        [
            "LTE",
            [
                "oldQuorumNumerator",
                "value",
                "quorumNumerator()",
                "uint256_1",
                "newQuorumNumerator"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ],
        [
            "LTE",
            [
                "_key@_unsafeAccess(self,pos - 1)",
                "_key@last"
            ],
            [
                "key"
            ],
            "#Medium#ERROR_MSG:Checkpoint: decreasing keys"
        ]
    ],
    "ERC4626.maxDeposit(address) returns(uint256)": [],
    "ERC721.safeTransferFrom(address,address,uint256,bytes) returns()": [
        [
            [
                "_isApprovedOrOwner(_msgSender(),tokenId)",
                "_isApprovedOrOwner(msgsender,tokenId)",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "spender"
                    ],
                    [
                        "ownerOf(tokenId)",
                        "owner"
                    ]
                ],
                "isApprovedForAll(_msgSender(),tokenId)",
                "isApprovedForAll(msgsender,tokenId)",
                "_operatorApprovals@_msgSender()@tokenId",
                "_operatorApprovals@msgsender@tokenId",
                [
                    "EQ",
                    "getApproved(tokenId)",
                    [
                        "_msgSender()",
                        "msgsender"
                    ]
                ]
            ],
            "#High#ERROR_MSG:ERC721: caller is not token owner or approved"
        ],
        [
            [
                "_checkOnERC721Received(from,to,tokenId,data)"
            ],
            "#High#ERROR_MSG:ERC721: transfer to non ERC721Receiver implementer"
        ],
        [
            "EQ",
            [
                "ownerOf(tokenId)",
                "owner"
            ],
            [
                "from",
                "address_1"
            ],
            "#Medium#ERROR_MSG:ERC721: transfer from incorrect owner"
        ],
        [
            "NEQ",
            [
                "to",
                "address_2",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC721: transfer to the zero address"
        ],
        [
            "NEQ",
            [
                "_ownerOf(tokenId)",
                "_owners@tokenId",
                "_owners@firstTokenId",
                "owner"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: invalid token ID"
        ]
    ],
    "AccessControl.grantRole(bytes32,address) returns()": [
        [
            [
                "onlyRole",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ]
    ],
    "ERC4626.maxMint(address) returns(uint256)": [],
    "ERC20Votes._unsafeAccess(ERC20Votes.Checkpoint[],uint256) returns(ERC20Votes.Checkpoint)": [],
    "Governor.onERC1155Received(address,address,uint256,uint256,bytes) returns(bytes4)": [],
    "AccessControl.revokeRole(bytes32,address) returns()": [
        [
            [
                "onlyRole",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ]
    ],
    "ERC4626.maxWithdraw(address) returns(uint256)": [
        [
            "GT",
            [
                "denominator"
            ],
            [
                "prod1"
            ],
            "#Medium#ERROR_MSG:Math: mulDiv overflow"
        ]
    ],
    "ERC20.approve(address,uint256) returns(bool)": [
        [
            "NEQ",
            [
                "owner",
                "msgsender",
                "_msgSender()"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve from the zero address"
        ],
        [
            "NEQ",
            [
                "spender",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve to the zero address"
        ]
    ],
    "ERC20Permit.constructor(string) returns()": [],
    "ERC4626.maxRedeem(address) returns(uint256)": [],
    "ConditionalEscrow.withdrawalAllowed(address) returns(bool)": [],
    "GovernorCompatibilityBravo.COUNTING_MODE() returns(string)": [],
    "AccessControl._setupRole(bytes32,address) returns()": [],
    "GovernorVotes.clock() returns(uint48)": [
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "ERC20Permit.DOMAIN_SEPARATOR() returns(bytes32)": [],
    "Pausable.whenPaused() returns()": [],
    "ERC20Wrapper._recover(address) returns(uint256)": [
        [
            "NEQ",
            [
                "to",
                "address_1",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: mint to the zero address"
        ]
    ],
    "ERC4626.previewMint(uint256) returns(uint256)": [
        [
            "GT",
            [
                "denominator"
            ],
            [
                "prod1"
            ],
            "#Medium#ERROR_MSG:Math: mulDiv overflow"
        ]
    ],
    "ERC721._isApprovedOrOwner(address,uint256) returns(bool)": [
        [
            "NEQ",
            [
                "_ownerOf(tokenId)",
                "_owners@tokenId",
                "owner"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: invalid token ID"
        ]
    ],
    "AccessControl._grantRole(bytes32,address) returns()": [],
    "ERC1155.balanceOf(address,uint256) returns(uint256)": [
        [
            "NEQ",
            [
                "address_1",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC1155: address zero is not a valid owner"
        ]
    ],
    "EIP712._domainSeparatorV4() returns(bytes32)": [],
    "IGovernor.getVotes(address,uint256) returns(uint256)": [],
    "Escrow.depositsOf(address) returns(uint256)": [],
    "GovernorCompatibilityBravo.propose(address[],uint256[],string[],bytes[],string) returns(uint256)": [
        [
            "EQ",
            [
                "length@signatures"
            ],
            [
                "length@calldatas"
            ],
            "#Medium#ERROR_MSG:GovernorBravo: invalid signatures length"
        ],
        [
            [
                "_isValidDescriptionForProposer(proposer,description)"
            ],
            "#Medium#ERROR_MSG:Governor: proposer restricted"
        ],
        [
            "GTE",
            [
                "getVotes(proposer,currentTimepoint - 1)",
                "_getVotes(account,timepoint,_defaultParams())"
            ],
            [
                "proposalThreshold()",
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: proposer votes below proposal threshold"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@values"
            ],
            "#Medium#ERROR_MSG:Governor: invalid proposal length"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@calldatas"
            ],
            "#Medium#ERROR_MSG:Governor: invalid proposal length"
        ],
        [
            "GT",
            [
                "length@targets"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: empty proposal"
        ],
        [
            "EQ",
            [
                "voteStart@_proposals@hashProposal(targets,values,calldatas,keccak256(bytes)(bytes(description)))",
                "voteStart@_proposals@encode(targets,values,calldatas,descriptionHash)))",
                "voteStart@_proposals@proposalId"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: proposal already exists"
        ],
        [
            "LTE",
            [
                "value",
                "snapshot",
                "deadline",
                "snapshot + votingPeriod()",
                "currentTimepoint + votingDelay()"
            ],
            [
                "max@type()(uint64)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 64 bits"
        ]
    ],
    "ERC20Permit.nonces(address) returns(uint256)": [],
    "ERC4626.previewRedeem(uint256) returns(uint256)": [
        [
            "GT",
            [
                "denominator"
            ],
            [
                "prod1"
            ],
            "#Medium#ERROR_MSG:Math: mulDiv overflow"
        ]
    ],
    "ERC20FlashMint.slitherConstructorConstantVariables() returns()": [],
    "ERC721.tokenURI(uint256) returns(string)": [],
    "ERC4626._deposit(address,address,uint256,uint256) returns()": [
        [
            "NEQ",
            [
                "receiver",
                "address_2",
                "to",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: mint to the zero address"
        ],
        [
            [
                [
                    "EQ",
                    [
                        "length@functionCall(data,SafeERC20: low-level call failed)",
                        "length@returndata"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ],
                [
                    "decode(returndata,(bool))"
                ]
            ],
            "#Medium#ERROR_MSG:SafeERC20: ERC20 operation did not succeed"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "Implementation1.initialize() returns()": [
        [
            "initializer"
        ],
        [
            [
                [
                    [
                        "! _initializing",
                        "isTopLevelCall"
                    ],
                    [
                        "LT",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ],
                [
                    [
                        "NOT",
                        [
                            "isContract(address(this))"
                        ]
                    ],
                    [
                        "EQ",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ]
            ],
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "IGovernor.getVotesWithParams(address,uint256,bytes) returns(uint256)": [],
    "IAccessControl.renounceRole(bytes32,address) returns()": [],
    "Governor.castVoteBySig(uint256,uint8,uint8,bytes32,bytes32) returns(uint256)": [
        [
            "EQ",
            [
                "state(proposalId)"
            ],
            [
                "Active@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: vote not currently active"
        ],
        [
            "EQ",
            [
                "InvalidSignature@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature)"
        ],
        [
            "EQ",
            [
                "InvalidSignatureLength@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature length)"
        ],
        [
            "EQ",
            [
                "InvalidSignatureS@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature 's' value)"
        ],
        [
            "EQ",
            [
                "0"
            ],
            [
                "proposalSnapshot(proposalId)",
                "REF_1872",
                "voteStart@_proposals@proposalId",
                "voteStart@proposal",
                "snapshot"
            ],
            "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
        ]
    ],
    "IVotes.getPastTotalSupply(uint256) returns(uint256)": [],
    "IGovernor.state(uint256) returns(IGovernor.ProposalState)": [],
    "ContextMockCaller.callSender(ContextMock) returns()": [],
    "ERC721.transferFrom(address,address,uint256) returns()": [
        [
            [
                "_isApprovedOrOwner(_msgSender(),tokenId)",
                "_isApprovedOrOwner(msgsender,tokenId)",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "spender"
                    ],
                    [
                        "ownerOf(tokenId)",
                        "owner"
                    ]
                ],
                "isApprovedForAll(_msgSender(),tokenId)",
                "isApprovedForAll(msgsender,tokenId)",
                "_operatorApprovals@_msgSender()@tokenId",
                "_operatorApprovals@msgsender@tokenId",
                [
                    "EQ",
                    "getApproved(tokenId)",
                    [
                        "_msgSender()",
                        "msgsender"
                    ]
                ]
            ],
            "#High#ERROR_MSG:ERC721: caller is not token owner or approved"
        ],
        [
            "EQ",
            [
                "ownerOf(tokenId)",
                "owner"
            ],
            [
                "from",
                "address_1"
            ],
            "#Medium#ERROR_MSG:ERC721: transfer from incorrect owner"
        ],
        [
            "NEQ",
            [
                "to",
                "address_2"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC721: transfer to the zero address"
        ],
        [
            "NEQ",
            [
                "_ownerOf(tokenId)",
                "_owners@tokenId",
                "_owners@firstTokenId",
                "owner"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: invalid token ID"
        ]
    ],
    "GovernorVotesQuorumFraction.quorumNumerator() returns(uint256)": [],
    "Implementation1.setValue(uint256) returns()": [],
    "EIP712._hashTypedDataV4(bytes32) returns(bytes32)": [],
    "ContextMockCaller.callData(ContextMock,uint256,string) returns()": [],
    "Initializable._disableInitializers() returns()": [
        [
            "NOT",
            [
                "_initializing",
                "bool"
            ],
            "#High#ERROR_MSG:Initializable: contract is initializing"
        ]
    ],
    "Ownable.constructor() returns()": [],
    "GovernorPreventLateQuorumMock.slitherConstructorConstantVariables() returns()": [],
    "ERC1967Upgrade._upgradeBeaconToAndCall(address,bytes,bool) returns()": [
        [
            [
                "isContract(newBeacon)"
            ],
            "#Medium#ERROR_MSG:ERC1967: new beacon is not a contract"
        ],
        [
            [
                "implementation())"
            ],
            "#Medium#ERROR_MSG:ERC1967: beacon implementation is not a contract"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "Implementation2.initialize() returns()": [
        [
            "initializer"
        ],
        [
            [
                [
                    [
                        "! _initializing",
                        "isTopLevelCall"
                    ],
                    [
                        "LT",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ],
                [
                    [
                        "NOT",
                        [
                            "isContract(address(this))"
                        ]
                    ],
                    [
                        "EQ",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ]
            ],
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "ERC1820Implementer._registerInterfaceForAddress(bytes32,address) returns()": [],
    "Ownable.renounceOwnership() returns()": [
        [
            [
                "onlyOwner",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ]
    ],
    "ERC721._baseURI() returns(string)": [],
    "Impl.version() returns(string)": [],
    "GovernorVotesQuorumFraction.quorumDenominator() returns(uint256)": [],
    "DummyImplementation.initializeNonPayable() returns()": [],
    "Implementation2.setValue(uint256) returns()": [],
    "GovernorVotesQuorumFraction.quorum(uint256) returns(uint256)": [
        [
            "LTE",
            [
                "value",
                "timepoint",
                "uint256_1"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ]
    ],
    "ERC721.supportsInterface(bytes4) returns(bool)": [],
    "IGovernor.propose(address[],uint256[],bytes[],string) returns(uint256)": [],
    "Ownable._checkOwner() returns()": [
        [
            "EQ",
            [
                "owner()",
                [
                    "_owner"
                ]
            ],
            [
                "_msgSender()",
                "msgsender"
            ],
            "#High#ERROR_MSG:Ownable: caller is not the owner"
        ]
    ],
    "Implementation2.getValue() returns(uint256)": [],
    "Ownable._transferOwnership(address) returns()": [],
    "GovernorVotesQuorumFraction.updateQuorumNumerator(uint256) returns()": [
        [
            [
                "onlyGovernance"
            ],
            [
                "EQ",
                [
                    "_msgSender()",
                    "msgsender"
                ],
                [
                    "_executor()"
                ]
            ],
            "#High#ERROR_MSG:Governor: onlyGovernance"
        ],
        [
            "LTE",
            [
                "uint256_1",
                "newQuorumNumerator",
                "value"
            ],
            [
                "quorumDenominator()",
                "100"
            ],
            "#Medium#ERROR_MSG:GovernorVotesQuorumFraction: quorumNumerator over quorumDenominator"
        ],
        [
            "LTE",
            [
                "uint256_1",
                "newQuorumNumerator",
                "value",
                "quorumNumerator()",
                "oldQuorumNumerator"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ],
        [
            "LTE",
            [
                "_key@_unsafeAccess(self,pos - 1)",
                "_key@last"
            ],
            [
                "key"
            ],
            "#Medium#ERROR_MSG:Checkpoint: decreasing keys"
        ]
    ],
    "IAccessControlEnumerable.getRoleMemberCount(bytes32) returns(uint256)": [],
    "DummyImplementation.initializePayable() returns()": [],
    "Implementation3.initialize() returns()": [
        [
            "initializer"
        ],
        [
            [
                [
                    [
                        "! _initializing",
                        "isTopLevelCall"
                    ],
                    [
                        "LT",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ],
                [
                    [
                        "NOT",
                        [
                            "isContract(address(this))"
                        ]
                    ],
                    [
                        "EQ",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ]
            ],
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "AccessControlEnumerable.supportsInterface(bytes4) returns(bool)": [],
    "IVotes.delegate(address) returns()": [],
    "IGovernor.name() returns(string)": [],
    "IGovernor.version() returns(string)": [],
    "DummyImplementation.initializeNonPayableWithValue(uint256) returns()": [],
    "Votes.clock() returns(uint48)": [
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "EIP712.constructor(string,string) returns()": [],
    "ERC721.getApproved(uint256) returns(address)": [],
    "Implementation3.setValue(uint256) returns()": [],
    "Ownable.transferOwnership(address) returns()": [
        [
            "NEQ",
            [
                "newOwner",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:Ownable: new owner is the zero address"
        ],
        [
            [
                "onlyOwner",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ]
    ],
    "DummyImplementation.initializePayableWithValue(uint256) returns()": [],
    "GovernorTimelockControl.updateTimelock(TimelockController) returns()": [
        [
            [
                "onlyGovernance"
            ],
            [
                "EQ",
                [
                    "_msgSender()",
                    "msgsender"
                ],
                [
                    "_executor()",
                    "address(_timelock)"
                ]
            ],
            "#High#ERROR_MSG:Governor: onlyGovernance"
        ]
    ],
    "ERC721._transfer(address,address,uint256) returns()": [
        [
            "EQ",
            [
                "ownerOf(tokenId)"
            ],
            [
                "from",
                "address_1"
            ],
            "#Medium#ERROR_MSG:ERC721: transfer from incorrect owner"
        ],
        [
            "NEQ",
            [
                "to",
                "address_2"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC721: transfer to the zero address"
        ],
        [
            "NEQ",
            [
                "_ownerOf(tokenId)",
                "_owners@tokenId",
                "_owners@firstTokenId",
                "owner"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: invalid token ID"
        ]
    ],
    "Implementation3.getValue(uint256) returns(uint256)": [],
    "Governor.receive() returns()": [],
    "ERC721._safeMint(address,uint256,bytes) returns()": [
        [
            [
                "_checkOnERC721Received(address(0),to,tokenId,data)"
            ],
            "#High#ERROR_MSG:ERC721: transfer to non ERC721Receiver implementer"
        ],
        [
            "NEQ",
            [
                "to",
                "address_1",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: mint to the zero address"
        ],
        [
            "NOT",
            [
                "_exists(tokenId)",
                [
                    "NEQ",
                    [
                        "_ownerOf(tokenId)",
                        [
                            "_owners@tokenId"
                        ]
                    ],
                    [
                        "address(0)"
                    ]
                ]
            ],
            "#Low#ERROR_MSG:ERC721: token already minted"
        ]
    ],
    "DummyImplementation.initialize(uint256,string,uint256[]) returns()": [],
    "ERC1155.safeBatchTransferFrom(address,address,uint256[],uint256[],bytes) returns()": [
        [
            [
                [
                    "EQ",
                    [
                        "from",
                        "address_1",
                        "account"
                    ],
                    [
                        "_msgSender()",
                        "operator",
                        "msgsender"
                    ]
                ],
                [
                    "isApprovedForAll(from,_msgSender())",
                    [
                        "_operatorApprovals@account@operator"
                    ]
                ]
            ],
            "#High#ERROR_MSG:ERC1155: caller is not token owner or approved"
        ],
        [
            "EQ",
            [
                "length@ids"
            ],
            [
                "length@amounts"
            ],
            "#Low#ERROR_MSG:ERC1155: ids and amounts length mismatch"
        ],
        [
            "NEQ",
            [
                "to",
                "address_2",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC1155: transfer to the zero address"
        ],
        [
            "GTE",
            [
                "_balances@id",
                "_balances@ids@i@from",
                "_balances@id@from",
                "fromBalance",
                "_balances@ids@i@account",
                "_balances@ids",
                "_balances@ids@i",
                "_balances@id@account"
            ],
            [
                "amounts",
                "amount",
                "values",
                "amounts@i"
            ],
            "#Medium#ERROR_MSG:ERC1155: insufficient balance for transfer"
        ],
        [
            "NEQ",
            [
                "selector@onERC1155BatchReceived@IERC1155Receiver"
            ],
            [
                "response"
            ],
            "#High#ERROR_MSG:ERC1155: ERC1155Receiver rejected tokens"
        ]
    ],
    "GovernorProposalThreshold.slitherConstructorConstantVariables() returns()": [],
    "Implementation4.initialize() returns()": [
        [
            "initializer"
        ],
        [
            [
                [
                    [
                        "! _initializing",
                        "isTopLevelCall"
                    ],
                    [
                        "LT",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ],
                [
                    [
                        "NOT",
                        [
                            "isContract(address(this))"
                        ]
                    ],
                    [
                        "EQ",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ]
            ],
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "IGovernor.hasVoted(uint256,address) returns(bool)": [],
    "ERC721.ownerOf(uint256) returns(address)": [
        [
            "NEQ",
            [
                "_ownerOf(tokenId)",
                "_owners@tokenId",
                "owner"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: invalid token ID"
        ]
    ],
    "DummyImplementation.get() returns(bool)": [],
    "Votes.CLOCK_MODE() returns(string)": [
        [
            "EQ",
            [
                "clock()",
                "timestamp"
            ],
            [
                "number"
            ],
            "#Medium#ERROR_MSG:Votes: broken clock mode"
        ],
        [
            "LTE",
            [
                "value",
                "timestamp"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "ERC165Checker.slitherConstructorConstantVariables() returns()": [],
    "CrossChainEnabled.onlyCrossChainSender(address) returns()": [
        [
            "NEQ",
            [
                "_crossChainSender()",
                "actual"
            ],
            [
                "expected",
                "address_1"
            ],
            "#High#ERROR_MSG:InvalidCrossChainSender(address,address)(actual,expected)"
        ]
    ],
    "ERC721._burn(uint256) returns()": [
        [
            "NEQ",
            [
                "_ownerOf(tokenId)",
                "_owners@tokenId",
                "_owners@firstTokenId",
                "owner"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: invalid token ID"
        ]
    ],
    "DummyImplementation.version() returns(string)": [],
    "Implementation4.setValue(uint256) returns()": [],
    "ERC4626._decimalsOffset() returns(uint8)": [],
    "Votes.getVotes(address) returns(uint256)": [],
    "IGovernorCompatibilityBravo.proposals(uint256) returns(uint256,address,uint256,uint256,uint256,uint256,uint256,uint256,bool,bool)": [],
    "EnumerableMap.remove(EnumerableMap.UintToAddressMap,uint256) returns(bool)": [],
    "PaymentSplitter._pendingPayment(address,uint256,uint256) returns(uint256)": [],
    "ERC721Consecutive._mintConsecutive(address,uint96) returns(uint96)": [
        [
            "NOT",
            [
                "isContract(address(this))"
            ],
            "#Medium#ERROR_MSG:ERC721Consecutive: batch minting restricted to constructor"
        ],
        [
            "NEQ",
            [
                "account",
                "to",
                "address_1",
                "from",
                "owner"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721Consecutive: mint to the zero address"
        ],
        [
            "LTE",
            [
                "amount",
                "batchSize",
                "uint96_1"
            ],
            [
                "_maxBatchSize()",
                "5000"
            ],
            "#Low#ERROR_MSG:ERC721Consecutive: batch too large"
        ],
        [
            "EQ",
            [
                "amount",
                "batchSize",
                "uint96_1"
            ],
            [
                "1"
            ],
            "#Low#ERROR_MSG:ERC721Consecutive: batch burn not supported"
        ],
        [
            "LTE",
            [
                "_key@_unsafeAccess(self,pos - 1)",
                "_key@last"
            ],
            [
                "key",
                "last",
                "first + batchSize - 1"
            ],
            "#Medium#ERROR_MSG:Checkpoint: decreasing keys"
        ]
    ],
    "ERC20Votes._mint(address,uint256) returns()": [
        [
            "LTE",
            [
                "totalSupply()",
                [
                    "_totalSupply"
                ]
            ],
            [
                "_maxSupply()",
                "max@type()(uint224)"
            ],
            "#Medium#ERROR_MSG:ERC20Votes: total supply risks overflowing votes"
        ],
        [
            "NEQ",
            [
                "account",
                "to",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: mint to the zero address"
        ],
        [
            "LTE",
            [
                "value",
                "newWeight"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "GovernorTimelockCompound.updateTimelock(ICompoundTimelock) returns()": [
        [
            [
                "onlyGovernance"
            ],
            [
                "EQ",
                [
                    "_msgSender()",
                    "msgsender"
                ],
                [
                    "_executor()",
                    "address(_timelock)"
                ]
            ],
            "#High#ERROR_MSG:Governor: onlyGovernance"
        ]
    ],
    "ERC165Checker.getSupportedInterfaces(address,bytes4[]) returns(bool[])": [],
    "EnumerableMap.contains(EnumerableMap.UintToAddressMap,uint256) returns(bool)": [],
    "IAccessControl.revokeRole(bytes32,address) returns()": [],
    "PaymentSplitter._addPayee(address,uint256) returns()": [
        [
            "NEQ",
            [
                "address_1",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:PaymentSplitter: account is the zero address"
        ],
        [
            "GT",
            [
                "uint256_1",
                "shares_"
            ],
            [
                "0"
            ],
            "#Low#ERROR_MSG:PaymentSplitter: shares are 0"
        ],
        [
            "EQ",
            [
                "_shares@account"
            ],
            [
                "0"
            ],
            "#Low#ERROR_MSG:PaymentSplitter: account already has shares"
        ]
    ],
    "GovernorCountingSimple.COUNTING_MODE() returns(string)": [],
    "ERC721Consecutive._mint(address,uint256) returns()": [
        [
            [
                "isContract(address(this))"
            ],
            "#Medium#ERROR_MSG:ERC721Consecutive: can't mint during construction"
        ],
        [
            "NEQ",
            [
                "to",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: mint to the zero address"
        ],
        [
            "NOT",
            [
                "_exists(tokenId)",
                [
                    "NEQ",
                    [
                        "_ownerOf(tokenId)"
                    ],
                    [
                        "address(0)"
                    ]
                ]
            ],
            "#Low#ERROR_MSG:ERC721: token already minted"
        ]
    ],
    "ERC20.allowance(address,address) returns(uint256)": [],
    "GovernorTimelockCompound._updateTimelock(ICompoundTimelock) returns()": [],
    "ERC20Votes._burn(address,uint256) returns()": [
        [
            "NEQ",
            [
                "from",
                "account",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: burn from the zero address"
        ],
        [
            "GTE",
            [
                "_balances@from",
                "_balances@account",
                "accountBalance"
            ],
            [
                "amount",
                "uint256_1",
                "delta"
            ],
            "#Medium#ERROR_MSG:ERC20: burn amount exceeds balance"
        ],
        [
            "LTE",
            [
                "value",
                "newWeight"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "GovernorTimelockControl.queue(address[],uint256[],bytes[],bytes32) returns(uint256)": [
        [
            "EQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Succeeded@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not successful"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@values"
            ],
            "#Medium#ERROR_MSG:TimelockController: length mismatch"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@payloads"
            ],
            "#Medium#ERROR_MSG:TimelockController: length mismatch"
        ],
        [
            [
                "onlyRole",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ],
        [
            "NOT",
            [
                "isOperation(id)",
                [
                    "GT",
                    [
                        "getTimestamp(id)",
                        [
                            "_timestamps@id"
                        ]
                    ],
                    [
                        "predecessor",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:TimelockController: operation already scheduled"
        ],
        [
            "GTE",
            [
                "delay",
                "getMinDelay()"
            ],
            [
                "getMinDelay()",
                [
                    "_minDelay"
                ]
            ],
            "#Medium#ERROR_MSG:TimelockController: insufficient delay"
        ],
        [
            "EQ",
            [
                "predecessor",
                "0"
            ],
            [
                "proposalSnapshot(proposalId)",
                "REF_2245",
                "voteStart@_proposals@encode(targets,values,calldatas,descriptionHash)))",
                "voteStart@_proposals@proposalId",
                "voteStart@_proposals@hashProposal(targets,values,calldatas,descriptionHash)",
                "snapshot",
                "voteStart@proposal"
            ],
            "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
        ]
    ],
    "ERC165Checker.supportsAllInterfaces(address,bytes4[]) returns(bool)": [],
    "EnumerableMap.length(EnumerableMap.UintToAddressMap) returns(uint256)": [],
    "VestingWallet.constructor(address,uint64,uint64) returns()": [
        [
            "NEQ",
            [
                "address_1",
                "beneficiaryAddress"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:VestingWallet: beneficiary is zero address"
        ]
    ],
    "ERC721Consecutive._afterTokenTransfer(address,address,uint256,uint256) returns()": [
        [
            "EQ",
            [
                "batchSize",
                "uint256_2"
            ],
            [
                "1"
            ],
            "#Medium#ERROR_MSG:ERC721Consecutive: batch burn not supported"
        ]
    ],
    "SampleGramps.initialize(string) returns()": [
        [
            "initializer"
        ],
        [
            [
                [
                    [
                        "! _initializing",
                        "isTopLevelCall"
                    ],
                    [
                        "LT",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ],
                [
                    [
                        "NOT",
                        [
                            "isContract(address(this))"
                        ]
                    ],
                    [
                        "EQ",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ]
            ],
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ],
        [
            "onlyInitializing"
        ],
        [
            "_initializing",
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "GovernorTimelockControl.constructor(TimelockController) returns()": [],
    "ERC165Checker.supportsERC165InterfaceUnchecked(address,bytes4) returns(bool)": [],
    "ERC20Votes._afterTokenTransfer(address,address,uint256) returns()": [
        [
            "LTE",
            [
                "value",
                "newWeight"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "timestamp"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "EnumerableMap.at(EnumerableMap.UintToAddressMap,uint256) returns(uint256,address)": [],
    "ERC721Consecutive._totalConsecutiveSupply() returns(uint96)": [],
    "ERC721URIStorage.tokenURI(uint256) returns(string)": [],
    "Math.max(uint256,uint256) returns(uint256)": [],
    "EnumerableMap.tryGet(EnumerableMap.UintToAddressMap,uint256) returns(bool,address)": [],
    "ERC20Votes._delegate(address,address) returns()": [
        [
            "LTE",
            [
                "value",
                "newWeight"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "ERC721Enumerable.supportsInterface(bytes4) returns(bool)": [],
    "GovernorTimelockControl.supportsInterface(bytes4) returns(bool)": [],
    "Math.min(uint256,uint256) returns(uint256)": [],
    "ERC20Votes._moveVotingPower(address,address,uint256) returns()": [
        [
            "LTE",
            [
                "value",
                "newWeight"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "timestamp"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "ShortStrings.byteLengthWithFallback(ShortString,string) returns(uint256)": [
        [
            "LTE",
            [
                "31"
            ],
            [
                "result",
                "unwrap(sstr)) & 0xFF"
            ],
            "#Low#ERROR_MSG:InvalidShortString()()"
        ]
    ],
    "EnumerableMap.get(EnumerableMap.UintToAddressMap,uint256) returns(address)": [
        [
            [
                [
                    "NEQ",
                    [
                        "value",
                        "_values@map",
                        "_values@map@value",
                        "_values@map@key"
                    ],
                    [
                        "0"
                    ]
                ],
                [
                    "contains(map,key)",
                    "contains(key)"
                ]
            ],
            "#Medium#ERROR_MSG:EnumerableMap: nonexistent key"
        ]
    ],
    "VestingWallet.receive() returns()": [],
    "SampleGramps.__SampleGramps_init_unchained(string) returns()": [
        [
            "onlyInitializing"
        ],
        [
            "_initializing",
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "GovernorTimelockControl.state(uint256) returns(IGovernor.ProposalState)": [
        [
            "EQ",
            [
                "0"
            ],
            [
                "proposalSnapshot(proposalId)",
                "REF_2245",
                "voteStart@_proposals@proposalId",
                "snapshot",
                "voteStart@proposal"
            ],
            "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
        ]
    ],
    "Math.average(uint256,uint256) returns(uint256)": [],
    "Governor.castVote(uint256,uint8) returns(uint256)": [
        [
            "EQ",
            [
                "state(proposalId)"
            ],
            [
                "Active@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: vote not currently active"
        ],
        [
            "EQ",
            [
                "0"
            ],
            [
                "proposalSnapshot(proposalId)",
                "REF_1872",
                "voteStart@_proposals@proposalId",
                "voteStart@proposal",
                "snapshot"
            ],
            "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
        ]
    ],
    "EnumerableMap.get(EnumerableMap.UintToAddressMap,uint256,string) returns(address)": [
        [
            [
                [
                    "NEQ",
                    [
                        "_values@map",
                        "_values@map@value",
                        "value",
                        "_values@map@key"
                    ],
                    [
                        "0"
                    ]
                ],
                [
                    "contains(map,key)",
                    "contains(key)"
                ]
            ],
            "#Low#ERROR_MSG:errorMessage"
        ]
    ],
    "ERC721._checkOnERC721Received(address,address,uint256,bytes) returns(bool)": [
    ],
    "ERC20Votes.CLOCK_MODE() returns(string)": [
        [
            "EQ",
            [
                "clock()",
                "number)"
            ],
            [
                "value",
                "number"
            ],
            "#Medium#ERROR_MSG:ERC20Votes: broken clock mode"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "IGovernor.castVoteWithReason(uint256,uint8,string) returns(uint256)": [],
    "VestingWallet.beneficiary() returns(address)": [],
    "GovernorTimelockControl.timelock() returns(address)": [],
    "Math.ceilDiv(uint256,uint256) returns(uint256)": [],
    "ERC721Enumerable.tokenOfOwnerByIndex(address,uint256) returns(uint256)": [
        [
            "LT",
            [
                "uint256_1",
                "index"
            ],
            [
                "balanceOf(owner)"
            ],
            "#Low#ERROR_MSG:ERC721Enumerable: owner index out of bounds"
        ],
        [
            "NEQ",
            [
                "owner",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: address zero is not a valid owner"
        ]
    ],
    "EnumerableMap.keys(EnumerableMap.UintToAddressMap) returns(uint256[])": [],
    "ERC20Votes._add(uint256,uint256) returns(uint256)": [],
    "Escrow.deposit(address) returns()": [
        [
            [
                "onlyOwner",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ]
    ],
    "VestingWallet.start() returns(uint256)": [],
    "GovernorTimelockControl.proposalEta(uint256) returns(uint256)": [],
    "Math.mulDiv(uint256,uint256,uint256) returns(uint256)": [
        [
            "GT",
            [
                "denominator",
                "uint256_3"
            ],
            [
                "prod1"
            ],
            "#Medium#ERROR_MSG:Math: mulDiv overflow"
        ]
    ],
    "ERC721Enumerable.totalSupply() returns(uint256)": [],
    "EnumerableMap.set(EnumerableMap.AddressToUintMap,address,uint256) returns(bool)": [],
    "ERC1967Proxy.slitherConstructorConstantVariables() returns()": [],
    "VestingWallet.duration() returns(uint256)": [],
    "Governor._beforeExecute(uint256,address[],uint256[],bytes[],bytes32) returns()": [],
    "ERC20.decimals() returns(uint8)": [],
    "ERC20.transferFrom(address,address,uint256) returns(bool)": [
        [
            "GTE",
            [
                "allowance(owner,spender)",
                "_allowances@owner@spender",
                "_allowances@owner@_msgSender()",
                "currentAllowance",
                "_allowances@owner@msgsender"
            ],
            [
                "amount",
                "uint256_1"
            ],
            "#High#ERROR_MSG:ERC20: insufficient allowance"
        ],
        [
            "NEQ",
            [
                "owner",
                "from",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: transfer to the zero address"
        ],
        [
            "NEQ",
            [
                "to",
                "address_2"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: transfer to the zero address"
        ],
        [
            "GTE",
            [
                "_balances@from",
                "fromBalance",
                "_balances@owner"
            ],
            [
                "amount",
                "uint256_1"
            ],
            "#Medium#ERROR_MSG:ERC20: transfer amount exceeds balance"
        ],
        [
            "NEQ",
            [
                "owner",
                "from",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve from the zero address"
        ],
        [
            "NEQ",
            [
                "spender",
                "_msgSender()",
                "msgsender"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve to the zero address"
        ]
    ],
    "Math.mulDiv(uint256,uint256,uint256,Math.Rounding) returns(uint256)": [
        [
            "GT",
            [
                "denominator",
                "uint256_3"
            ],
            [
                "prod1"
            ],
            "#Medium#ERROR_MSG:Math: mulDiv overflow"
        ]
    ],
    "ERC721Enumerable.tokenByIndex(uint256) returns(uint256)": [
        [
            "LT",
            [
                "uint256_1",
                "index"
            ],
            [
                "totalSupply()"
            ],
            "#Low#ERROR_MSG:ERC721Enumerable: global index out of bounds"
        ]
    ],
    "EnumerableMap.remove(EnumerableMap.AddressToUintMap,address) returns(bool)": [],
    "ERC721URIStorage._burn(uint256) returns()": [
        [
            "NEQ",
            [
                "_ownerOf(tokenId)",
                "_owners@tokenId",
                "_owners@firstTokenId",
                "owner"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: invalid token ID"
        ]
    ],
    "VestingWallet.released() returns(uint256)": [],
    "SampleHuman.__SampleHuman_init() returns()": [
        [
            "onlyInitializing"
        ],
        [
            "_initializing",
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "GovernorTimelockControl._execute(uint256,address[],uint256[],bytes[],bytes32) returns()": [
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@values"
            ],
            "#Medium#ERROR_MSG:TimelockController: length mismatch"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@payloads"
            ],
            "#Medium#ERROR_MSG:TimelockController: length mismatch"
        ],
        [
            "onlyRoleOrOpenRole"
        ],
        [
            [
                "isOperationReady(id)"
            ],
            "#Medium#ERROR_MSG:TimelockController: operation is not ready"
        ],
        [
            [
                [
                    "EQ",
                    [
                        "predecessor",
                        "hashOperationBatch(targets,values,payloads,predecessor,salt)",
                        "0",
                        "id",
                        "encode(targets,values,payloads,predecessor,salt))"
                    ],
                    [
                        "bytes32(0)"
                    ]
                ],
                [
                    "isOperationDone(predecessor)",
                    [
                        "EQ",
                        [
                            "getTimestamp(id)",
                            [
                                "_timestamps@id",
                                "_timestamps@0",
                                "_timestamps@predecessor",
                                "_timestamps@hashOperationBatch(targets,values,payloads,predecessor,salt)",
                                "_timestamps@encode(targets,values,payloads,predecessor,salt))",
                                "timestamp",
                                "getTimestamp(id)"
                            ]
                        ],
                        [
                            "_DONE_TIMESTAMP",
                            "uint256(1)",
                            "uint256"
                        ]
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:TimelockController: missing dependency"
        ],
        [
            "success",
            "#Medium#ERROR_MSG:TimelockController: underlying transaction reverted"
        ]
    ],
    "ERC1155._safeTransferFrom(address,address,uint256,uint256,bytes) returns()": [
        [
            "NEQ",
            [
                "to",
                "address_2",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC1155: transfer to the zero address"
        ],
        [
            "GTE",
            [
                "fromBalance",
                "_balances@element",
                "_balances@id@from",
                "_balances@id"
            ],
            [
                "element",
                "amount",
                "value",
                "uint256_2"
            ],
            "#Medium#ERROR_MSG:ERC1155: insufficient balance for transfer"
        ],
        [
            "NEQ",
            [
                "selector@onERC1155Received@IERC1155Receiver"
            ],
            [
                "response"
            ],
            "#Medium#ERROR_MSG:(ERC1155: ERC1155Receiver rejected tokens)"
        ]
    ],
    "GovernorTimelockCompound._executor() returns(address)": [],
    "ERC777._send(address,address,uint256,bytes,bytes,bool) returns()": [
        [
            "NEQ",
            [
                "to",
                "account",
                "from",
                "address_2",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC777: transfer from the zero address"
        ],
        [
            "NEQ",
            [
                "to",
                "account",
                "from",
                "address_2",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC777: transfer to the zero address"
        ],
        [
            "NOT",
            [
                "isContract()"
            ],
            "#Medium#ERROR_MSG:ERC777: token recipient contract has no implementer for ERC777TokensRecipient"
        ],
        [
            "GTE",
            [
                "_balances@to",
                "_balances@from",
                "fromBalance",
                "_balances@account"
            ],
            [
                "amount",
                "uint256_1"
            ],
            "#Medium#ERROR_MSG:ERC777: transfer amount exceeds balance"
        ]
    ],
    "ERC721Enumerable._beforeTokenTransfer(address,address,uint256,uint256) returns()": [
        [
            "NEQ",
            [
                "to",
                "address_1",
                "from",
                "owner",
                "address_2"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: address zero is not a valid owner"
        ],
        [
            "LTE",
            [
                "1"
            ],
            [
                "batchSize",
                "uint256_2"
            ],
            "#Low#ERROR_MSG:(ERC721Enumerable: consecutive transfers not supported)"
        ]
    ],
    "GovernorTimelockControl._cancel(address[],uint256[],bytes[],bytes32) returns(uint256)": [
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Canceled@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Expired@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Executed@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            [
                "isOperationPending(id)",
                [
                    "GT",
                    [
                        "getTimestamp(id)",
                        [
                            "_timestamps@id"
                        ]
                    ],
                    [
                        "_DONE_TIMESTAMP",
                        "uint256(1)",
                        "uint256"
                    ]
                ]
            ],
            "#High#ERROR_MSG:TimelockController: operation cannot be cancelled"
        ],
        [
            [
                "onlyRole",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ],
        [
            "EQ",
            [
                "0"
            ],
            [
                "proposalSnapshot(proposalId)",
                "REF_1872",
                "voteStart@_proposals@encode(targets,values,calldatas,descriptionHash)))",
                "voteStart@_proposals@proposalId",
                "snapshot",
                "voteStart@_proposals@hashProposal(targets,values,calldatas,descriptionHash)",
                "voteStart@proposal"
            ],
            "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
        ]
    ],
    "Math.sqrt(uint256) returns(uint256)": [],
    "EnumerableMap.contains(EnumerableMap.AddressToUintMap,address) returns(bool)": [],
    "ERC20VotesComp.getCurrentVotes(address) returns(uint96)": [
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint96)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 96 bits"
        ]
    ],
    "VestingWallet.released(address) returns(uint256)": [],
    "Math.sqrt(uint256,Math.Rounding) returns(uint256)": [],
    "ERC721Enumerable._addTokenToOwnerEnumeration(address,uint256) returns()": [
        [
            "NEQ",
            [
                "owner",
                "to",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: address zero is not a valid owner"
        ]
    ],
    "EnumerableMap.length(EnumerableMap.AddressToUintMap) returns(uint256)": [],
    "ERC20VotesComp.getPriorVotes(address,uint256) returns(uint96)": [
        [
            "LT",
            [
                "timepoint",
                "uint256_1",
                "blockNumber"
            ],
            [
                "clock()",
                "number)"
            ],
            "#Medium#ERROR_MSG:ERC20Votes: future lookup"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint96)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 96 bits"
        ],
        [
            "LTE",
            [
                "value",
                "timestamp"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "VestingWallet.releasable() returns(uint256)": [],
    "ERC20ForceApproveMock.approve(address,uint256) returns(bool)": [
        [
            [
                [
                    "EQ",
                    [
                        "amount",
                        "uint256_1"
                    ],
                    [
                        "0"
                    ]
                ],
                [
                    "EQ",
                    [
                        "allowance(msgsender,spender)",
                        [
                            "_allowances@owner@spender"
                        ]
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#High#ERROR_MSG:USDT approval failure"
        ],
        [
            "NEQ",
            [
                "owner",
                "msgsender",
                "_msgSender()"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve from the zero address"
        ],
        [
            "NEQ",
            [
                "spender",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve to the zero address"
        ]
    ],
    "EnumerableSet.contains(EnumerableSet.Bytes32Set,bytes32) returns(bool)": [],
    "SafeCast.toUint104(uint256) returns(uint104)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint104)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 104 bits"
        ]
    ],
    "Votes._getTotalSupply() returns(uint256)": [],
    "Timers.isStarted(Timers.Timestamp) returns(bool)": [],
    "ReentrancyGuard.nonReentrant() returns()": [],
    "ERC20NoReturnMock.transfer(address,uint256) returns(bool)": [
        [
            "NEQ",
            [
                "owner",
                "from",
                "_msgSender()",
                "msgsender"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: transfer to the zero address"
        ],
        [
            "NEQ",
            [
                "to",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: transfer to the zero address"
        ],
        [
            "GTE",
            [
                "_balances@from",
                "_balances@_msgSender()",
                "fromBalance",
                "_balances@msgsender",
                "_balances@owner"
            ],
            [
                "amount",
                "uint256_1"
            ],
            "#Medium#ERROR_MSG:ERC20: transfer amount exceeds balance"
        ]
    ],
    "ERC4626Fees._withdraw(address,address,address,uint256,uint256) returns()": [
        [
            "NEQ",
            [
                "owner",
                "from",
                "account",
                "address_3"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: burn from the zero address"
        ],
        [
            "GTE",
            [
                "_balances@from",
                "_balances@owner",
                "_balances@account",
                "accountBalance"
            ],
            [
                "amount",
                "shares",
                "uint256_2"
            ],
            "#Medium#ERROR_MSG:ERC20: burn amount exceeds balance"
        ],
        [
            "GTE",
            [
                "allowance(owner,spender)",
                "_allowances@owner@caller",
                "_allowances@owner@spender",
                "currentAllowance"
            ],
            [
                "amount",
                "shares",
                "uint256_2"
            ],
            "#High#ERROR_MSG:ERC20: insufficient allowance"
        ],
        [
            [
                [
                    "EQ",
                    [
                        "length@functionCall(data,SafeERC20: low-level call failed)",
                        "length@returndata"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ],
                [
                    "decode(returndata,(bool))"
                ]
            ],
            "#Medium#ERROR_MSG:SafeERC20: ERC20 operation did not succeed"
        ],
        [
            "GT",
            [
                "denominator",
                "100000"
            ],
            [
                "prod1"
            ],
            "#Medium#ERROR_MSG:Math: mulDiv overflow"
        ],
        [
            "NEQ",
            [
                "owner",
                "from",
                "account",
                "address_3"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve from the zero address"
        ],
        [
            "NEQ",
            [
                "spender",
                "caller",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve to the zero address"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "Proxy.receive() returns()": [],
    "EnumerableSet.length(EnumerableSet.Bytes32Set) returns(uint256)": [],
    "SafeCast.toUint96(uint256) returns(uint96)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint96)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 96 bits"
        ]
    ],
    "Timers.isPending(Timers.Timestamp) returns(bool)": [],
    "ERC20NoReturnMock.transferFrom(address,address,uint256) returns(bool)": [
        [
            "GTE",
            [
                "allowance(owner,spender)",
                "_allowances@owner@spender",
                "_allowances@owner@_msgSender()",
                "currentAllowance",
                "_allowances@owner@msgsender"
            ],
            [
                "amount",
                "uint256_1"
            ],
            "#High#ERROR_MSG:ERC20: insufficient allowance"
        ],
        [
            "NEQ",
            [
                "owner",
                "from",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: transfer to the zero address"
        ],
        [
            "NEQ",
            [
                "to",
                "address_2"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: transfer to the zero address"
        ],
        [
            "GTE",
            [
                "_balances@from",
                "fromBalance",
                "_balances@owner"
            ],
            [
                "amount",
                "uint256_1"
            ],
            "#Medium#ERROR_MSG:ERC20: transfer amount exceeds balance"
        ],
        [
            "NEQ",
            [
                "owner",
                "from",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve from the zero address"
        ],
        [
            "NEQ",
            [
                "spender",
                "_msgSender()",
                "msgsender"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve to the zero address"
        ]
    ],
    "EnumerableSet.at(EnumerableSet.Bytes32Set,uint256) returns(bytes32)": [],
    "SafeCast.toUint88(uint256) returns(uint88)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint88)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 88 bits"
        ]
    ],
    "Timers.isExpired(Timers.Timestamp) returns(bool)": [],
    "ERC20NoReturnMock.approve(address,uint256) returns(bool)": [
        [
            "NEQ",
            [
                "owner",
                "msgsender",
                "_msgSender()"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve from the zero address"
        ],
        [
            "NEQ",
            [
                "spender",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve to the zero address"
        ]
    ],
    "ReentrancyGuard.constructor() returns()": [],
    "EnumerableSet.values(EnumerableSet.Bytes32Set) returns(bytes32[])": [],
    "SafeCast.toUint80(uint256) returns(uint80)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint80)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 80 bits"
        ]
    ],
    "AccessControlCrossChain._crossChainRoleAlias(bytes32) returns(bytes32)": [],
    "Timers.getDeadline(Timers.BlockNumber) returns(uint64)": [],
    "ERC1155._setApprovalForAll(address,address,bool) returns()": [
        [
            "NEQ",
            [
                "owner",
                "address_1"
            ],
            [
                "operator",
                "address_2"
            ],
            "#Low#ERROR_MSG:ERC1155: setting approval status for self"
        ]
    ],
    "ReentrancyGuard._nonReentrantBefore() returns()": [
        [
            "NEQ",
            [
                "_status",
                "uint256"
            ],
            [
                "2",
                "_ENTERED",
                "uint256"
            ],
            "#Medium#ERROR_MSG:ReentrancyGuard: reentrant call"
        ]
    ],
    "EnumerableSet.add(EnumerableSet.AddressSet,address) returns(bool)": [],
    "ERC20PermitNoRevertMock.permitThatMayRevert(address,address,uint256,uint256,uint8,bytes32,bytes32) returns()": [
        [
            "LTE",
            [
                "timestamp"
            ],
            [
                "uint256_2",
                "deadline"
            ],
            "#Medium#ERROR_MSG:ERC20Permit: expired deadline"
        ],
        [
            "EQ",
            [
                "recover(hash,v,r,s)",
                "signer"
            ],
            [
                "owner",
                "address_1"
            ],
            "#High#ERROR_MSG:ERC20Permit: invalid signature"
        ],
        [
            "NEQ",
            [
                "owner",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve from the zero address"
        ],
        [
            "NEQ",
            [
                "spender",
                "address_2"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve to the zero address"
        ]
    ],
    "SafeCast.toUint72(uint256) returns(uint72)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint72)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 72 bits"
        ]
    ],
    "Timers.setDeadline(Timers.BlockNumber,uint64) returns()": [],
    "SampleHuman.initialize() returns()": [
        [
            "initializer"
        ],
        [
            [
                [
                    [
                        "! _initializing",
                        "isTopLevelCall"
                    ],
                    [
                        "LT",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ],
                [
                    [
                        "NOT",
                        [
                            "isContract(address(this))"
                        ]
                    ],
                    [
                        "EQ",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ]
            ],
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ],
        [
            "onlyInitializing"
        ],
        [
            "_initializing",
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "Votes.delegate(address) returns()": [
        [
            "LTE",
            [
                "value",
                "amount"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ],
        [
            "LTE",
            [
                "_key@_unsafeAccess(self,pos - 1)",
                "_key@last"
            ],
            [
                "key"
            ],
            "#Medium#ERROR_MSG:Checkpoint: decreasing keys"
        ]
    ],
    "ReentrancyGuard._nonReentrantAfter() returns()": [],
    "EnumerableSet.remove(EnumerableSet.AddressSet,address) returns(bool)": [],
    "MinimalForwarder.slitherConstructorConstantVariables() returns()": [],
    "ERC20PermitNoRevertMock.permit(address,address,uint256,uint256,uint8,bytes32,bytes32) returns()": [
        [
            "LTE",
            [
                "timestamp"
            ],
            [
                "uint256_2",
                "deadline"
            ],
            "#Medium#ERROR_MSG:ERC20Permit: expired deadline"
        ],
        [
            "EQ",
            [
                "recover(hash,v,r,s)",
                "signer"
            ],
            [
                "owner",
                "address_1"
            ],
            "#High#ERROR_MSG:ERC20Permit: invalid signature"
        ],
        [
            "NEQ",
            [
                "owner",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve from the zero address"
        ],
        [
            "NEQ",
            [
                "spender",
                "address_2"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve to the zero address"
        ]
    ],
    "SafeCast.toUint64(uint256) returns(uint64)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint64)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 64 bits"
        ]
    ],
    "Timers.reset(Timers.BlockNumber) returns()": [],
    "EnumerableSet.contains(EnumerableSet.AddressSet,address) returns(bool)": [],
    "ERC20ReturnFalseMock.transfer(address,uint256) returns(bool)": [],
    "ReentrancyGuard._reentrancyGuardEntered() returns(bool)": [],
    "Timers.isUnset(Timers.BlockNumber) returns(bool)": [],
    "SafeCast.toUint56(uint256) returns(uint56)": [
        [
            "LTE",
            [
                "value",
                "uint256_1"
            ],
            [
                "max@type()(uint56)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 56 bits"
        ]
    ],
    "SampleHuman.__SampleHuman_init_unchained() returns()": [
        [
            "onlyInitializing"
        ],
        [
            "_initializing",
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "Governor.onERC1155BatchReceived(address,address,uint256[],uint256[],bytes) returns(bytes4)": [],
    "EnumerableSet.length(EnumerableSet.AddressSet) returns(uint256)": [],
    "ERC20ReturnFalseMock.transferFrom(address,address,uint256) returns(bool)": [],
    "SafeCast.toUint48(uint256) returns(uint48)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "Timers.isStarted(Timers.BlockNumber) returns(bool)": [],
    "ERC20ReturnFalseMock.approve(address,uint256) returns(bool)": [],
    "SafeCast.toUint40(uint256) returns(uint40)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint40)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 40 bits"
        ]
    ],
    "EnumerableSet.at(EnumerableSet.AddressSet,uint256) returns(address)": [],
    "Timers.isPending(Timers.BlockNumber) returns(bool)": [],
    "EnumerableSet.values(EnumerableSet.AddressSet) returns(address[])": [],
    "SafeCast.toUint32(uint256) returns(uint32)": [
        [
            "LTE",
            [
                "value",
                "uint256_1"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ]
    ],
    "Initializable._getInitializedVersion() returns(uint8)": [],
    "Timers.isExpired(Timers.BlockNumber) returns(bool)": [],
    "ERC20VotesLegacyMock.checkpoints(address,uint32) returns(ERC20VotesLegacyMock.Checkpoint)": [],
    "ERC4626Fees._entryFeeRecipient() returns(address)": [],
    "Votes._delegate(address,address) returns()": [
        [
            "LTE",
            [
                "value",
                "amount"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ],
        [
            "LTE",
            [
                "_key@_unsafeAccess(self,pos - 1)",
                "_key@last"
            ],
            [
                "key"
            ],
            "#Medium#ERROR_MSG:Checkpoint: decreasing keys"
        ]
    ],
    "IVotes.delegateBySig(address,uint256,uint256,uint8,bytes32,bytes32) returns()": [],
    "EnumerableSet.add(EnumerableSet.UintSet,uint256) returns(bool)": [],
    "SafeCast.toUint24(uint256) returns(uint24)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint24)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 24 bits"
        ]
    ],
    "ECDSA._throwError(ECDSA.RecoverError) returns()": [
        [
            "EQ",
            [
                "InvalidSignature@RecoverError"
            ],
            [
                "UserDefinedType_1",
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature)"
        ],
        [
            "EQ",
            [
                "InvalidSignatureLength@RecoverError"
            ],
            [
                "UserDefinedType_1",
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature length)"
        ],
        [
            "EQ",
            [
                "InvalidSignatureS@RecoverError"
            ],
            [
                "UserDefinedType_1",
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature 's' value)"
        ]
    ],
    "ERC1155._afterTokenTransfer(address,address,address,uint256[],uint256[],bytes) returns()": [],
    "GovernorCompatibilityBravo.proposals(uint256) returns(uint256,address,uint256,uint256,uint256,uint256,uint256,uint256,bool,bool)": [
        [
            "EQ",
            [
                "0"
            ],
            [
                "proposalSnapshot(proposalId)",
                "REF_2974",
                "voteStart@_proposals@proposalId",
                "snapshot",
                "voteStart@proposal"
            ],
            "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
        ]
    ],
    "SafeCast.toUint16(uint256) returns(uint16)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint16)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 16 bits"
        ]
    ],
    "EnumerableSet.remove(EnumerableSet.UintSet,uint256) returns(bool)": [],
    "ECDSA.tryRecover(bytes32,bytes) returns(address,ECDSA.RecoverError)": [],
    "LibArbitrumL1.isCrossChain(address) returns(bool)": [],
    "GovernorTimelockCompound.timelock() returns(address)": [],
    "GovernorPreventLateQuorum._setLateQuorumVoteExtension(uint64) returns()": [],
    "SafeCast.toInt72(int256) returns(int72)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "value",
                "int256_1"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 72 bits"
        ]
    ],
    "CrossChainEnabled._crossChainSender() returns(address)": [],
    "GovernorCompatibilityBravo._voteSucceeded(uint256) returns(bool)": [],
    "SampleMother.__SampleMother_init_unchained(uint256) returns()": [
        [
            "onlyInitializing"
        ],
        [
            "_initializing",
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "LibArbitrumL1.crossChainSender(address) returns(address)": [
        [
            "NEQ",
            [
                "sender",
                "l2ToL1Sender()"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:LibArbitrumL1: system messages without sender"
        ],
        [
            "NOT",
            [
                "isCrossChain(bridge)",
                [
                    "EQ",
                    [
                        "msgsender"
                    ],
                    [
                        "bridge",
                        "address_1"
                    ]
                ]
            ],
            "#High#ERROR_MSG:NotCrossChainCall()()"
        ]
    ],
    "GovernorProposalThreshold.propose(address[],uint256[],bytes[],string) returns(uint256)": [
        [
            [
                "_isValidDescriptionForProposer(proposer,description)"
            ],
            "#High#ERROR_MSG:Governor: proposer restricted"
        ],
        [
            "GTE",
            [
                "getVotes(proposer,currentTimepoint - 1)",
                "_getVotes(account,timepoint,_defaultParams())"
            ],
            [
                "proposalThreshold()",
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: proposer votes below proposal threshold"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@values"
            ],
            "#Medium#ERROR_MSG:Governor: invalid proposal length"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@calldatas"
            ],
            "#Medium#ERROR_MSG:Governor: invalid proposal length"
        ],
        [
            "GT",
            [
                "length@targets"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: empty proposal"
        ],
        [
            "EQ",
            [
                "voteStart@_proposals@hashProposal(targets,values,calldatas,keccak256(bytes)(bytes(description)))",
                "voteStart@_proposals@encode(targets,values,calldatas,descriptionHash)))",
                "voteStart@_proposals@proposalId"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: proposal already exists"
        ],
        [
            "LTE",
            [
                "value",
                "snapshot",
                "deadline",
                "snapshot + votingPeriod()",
                "currentTimepoint + votingDelay()"
            ],
            [
                "max@type()(uint64)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 64 bits"
        ]
    ],
    "SafeCast.toInt64(int256) returns(int64)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "int256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 64 bits"
        ]
    ],
    "LibArbitrumL2.isCrossChain(address) returns(bool)": [],
    "GovernorSettings.constructor(uint256,uint256,uint256) returns()": [],
    "SafeCast.toInt56(int256) returns(int56)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "int256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 56 bits"
        ]
    ],
    "LibOptimism.isCrossChain(address) returns(bool)": [],
    "SampleGramps.__SampleGramps_init(string) returns()": [
        [
            "onlyInitializing"
        ],
        [
            "_initializing",
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "SafeCast.toInt48(int256) returns(int48)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "int256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "LibArbitrumL2.crossChainSender(address) returns(address)": [
        [
            "NOT",
            [
                "isCrossChain(arbsys)",
                "wasMyCallersAddressAliased()"
            ],
            "#High#ERROR_MSG:NotCrossChainCall()()"
        ]
    ],
    "GovernorCompatibilityBravo.getActions(uint256) returns(address[],uint256[],string[],bytes[])": [],
    "SafeCast.toInt40(int256) returns(int40)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "int256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 40 bits"
        ]
    ],
    "AccessControlCrossChain.slitherConstructorConstantVariables() returns()": [],
    "GovernorSettings.votingDelay() returns(uint256)": [],
    "GovernorTimelockCompound.queue(address[],uint256[],bytes[],bytes32) returns(uint256)": [
        [
            "EQ",
            [
                "state(proposalId)"
            ],
            [
                "Succeeded@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not successful"
        ],
        [
            "NOT",
            [
                "encode(targets[i],values[i],,calldatas[i],eta)))"
            ],
            "#Low#ERROR_MSG:GovernorTimelockCompound: identical proposal action already queued"
        ],
        [
            "LTE",
            [
                "eta",
                "value",
                "delay()"
            ],
            [
                "max@type()(uint64)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 64 bits"
        ],
        [
            "EQ",
            [
                "0"
            ],
            [
                "proposalSnapshot(proposalId)",
                "REF_2545",
                "voteStart@_proposals@encode(targets,values,calldatas,descriptionHash)))",
                "voteStart@_proposals@proposalId",
                "voteStart@_proposals@hashProposal(targets,values,calldatas,descriptionHash)",
                "snapshot",
                "voteStart@proposal"
            ],
            "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
        ]
    ],
    "SafeCast.toInt32(int256) returns(int32)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "int256_1",
                "value"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ]
    ],
    "LibOptimism.crossChainSender(address) returns(address)": [
        [
            "NOT",
            [
                "isCrossChain(messenger)",
                [
                    "EQ",
                    [
                        "msgsender"
                    ],
                    [
                        "messenger",
                        "address_1"
                    ]
                ]
            ],
            "#High#ERROR_MSG:NotCrossChainCall()()"
        ]
    ],
    "GovernorSettings.votingPeriod() returns(uint256)": [],
    "IGovernorCompatibilityBravo.quorumVotes() returns(uint256)": [],
    "ERC721._setApprovalForAll(address,address,bool) returns()": [
        [
            "NEQ",
            [
                "owner",
                "address_1"
            ],
            [
                "operator",
                "address_2"
            ],
            "#Low#ERROR_MSG:ERC721: approve to caller"
        ]
    ],
    "SafeCast.toInt24(int256) returns(int24)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "int256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 24 bits"
        ]
    ],
    "IAccessControl.hasRole(bytes32,address) returns(bool)": [],
    "SafeMathMemoryCheck.addMemoryCheck() returns(uint256)": [],
    "ERC4626.redeem(uint256,address,address) returns(uint256)": [
        [
            "LTE",
            [
                "shares",
                "amount",
                "x",
                "uint256_1"
            ],
            [
                "maxRedeem(owner)",
                "balanceOf(owner)"
            ],
            "#Medium#ERROR_MSG:ERC4626: redeem more than max"
        ],
        [
            "NEQ",
            [
                "owner",
                "account",
                "from",
                "address_2"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: burn from the zero address"
        ],
        [
            "GTE",
            [
                "_balances@from",
                "_balances@account",
                "_balances@owner",
                "accountBalance"
            ],
            [
                "shares",
                "amount",
                "x",
                "uint256_1"
            ],
            "#Medium#ERROR_MSG:ERC20: burn amount exceeds balance"
        ],
        [
            "GTE",
            [
                "allowance(owner,spender)",
                "_allowances@owner@spender",
                "_allowances@owner@caller",
                "currentAllowance"
            ],
            [
                "shares",
                "amount",
                "x",
                "uint256_1"
            ],
            "#High#ERROR_MSG:ERC20: insufficient allowance"
        ],
        [
            "NEQ",
            [
                "owner",
                "account",
                "from",
                "address_2"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve from the zero address"
        ],
        [
            "NEQ",
            [
                "spender",
                "caller"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve to the zero address"
        ],
        [
            [
                [
                    "EQ",
                    [
                        "length@functionCall(data,SafeERC20: low-level call failed)",
                        "length@returndata"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ],
                [
                    "decode(returndata,(bool))"
                ]
            ],
            "#Medium#ERROR_MSG:SafeERC20: ERC20 operation did not succeed"
        ],
        [
            "GT",
            [
                "denominator"
            ],
            [
                "prod1"
            ],
            "#Medium#ERROR_MSG:Math: mulDiv overflow"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "GovernorSettings.proposalThreshold() returns(uint256)": [],
    "SampleFather.__SampleFather_init(string,uint256) returns()": [
        [
            "onlyInitializing"
        ],
        [
            "_initializing",
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "ERC777PresetFixedSupply.slitherConstructorConstantVariables() returns()": [],
    "SafeCast.toInt16(int256) returns(int16)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "int256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 16 bits"
        ]
    ],
    "SafeMathMemoryCheck.subMemoryCheck() returns(uint256)": [],
    "GovernorSettings.setVotingDelay(uint256) returns()": [
        [
            [
                "onlyGovernance"
            ],
            [
                "EQ",
                [
                    "_msgSender()",
                    "msgsender"
                ],
                [
                    "_executor()"
                ]
            ],
            "#High#ERROR_MSG:Governor: onlyGovernance"
        ],
        [
            "EQ",
            [
                "_msgSender()",
                "msgsender"
            ],
            [
                "_executor()",
                "address(this)"
            ],
            "#High#ERROR_MSG:Governor: onlyGovernance"
        ]
    ],
    "SampleFather.__SampleFather_init_unchained(uint256) returns()": [
        [
            "onlyInitializing"
        ],
        [
            "_initializing",
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "ERC777.defaultOperators() returns(address[])": [],
    "SafeCast.toInt8(int256) returns(int8)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "value",
                "int256_1"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 8 bits"
        ]
    ],
    "SafeMathMemoryCheck.mulMemoryCheck() returns(uint256)": [],
    "GovernorSettings.setVotingPeriod(uint256) returns()": [
        [
            [
                "onlyGovernance"
            ],
            [
                "EQ",
                [
                    "_msgSender()",
                    "msgsender"
                ],
                [
                    "_executor()",
                    "address(this)"
                ]
            ],
            "#High#ERROR_MSG:Governor: onlyGovernance"
        ],
        [
            "GT",
            [
                "uint256_1",
                "newVotingPeriod"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:GovernorSettings: voting period too low"
        ]
    ],
    "SampleChild.initialize(uint256,string,uint256,uint256) returns()": [
        [
            "initializer"
        ],
        [
            [
                [
                    [
                        "! _initializing",
                        "isTopLevelCall"
                    ],
                    [
                        "LT",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ],
                [
                    [
                        "NOT",
                        [
                            "isContract(address(this))"
                        ]
                    ],
                    [
                        "EQ",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ]
            ],
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ],
        [
            "onlyInitializing"
        ],
        [
            "_initializing",
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "ERC1155._setURI(string) returns()": [],
    "SafeCast.toInt256(uint256) returns(int256)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in an int256"
        ]
    ],
    "SafeMathMemoryCheck.divMemoryCheck() returns(uint256)": [],
    "GovernorSettings.setProposalThreshold(uint256) returns()": [
        [
            [
                "onlyGovernance"
            ],
            [
                "EQ",
                [
                    "_msgSender()",
                    "msgsender"
                ],
                [
                    "_executor()"
                ]
            ],
            "#High#ERROR_MSG:Governor: onlyGovernance"
        ]
    ],
    "ERC20.balanceOf(address) returns(uint256)": [],
    "SampleChild.__SampleChild_init(uint256,string,uint256,uint256) returns()": [
        [
            "onlyInitializing"
        ],
        [
            "_initializing",
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "IVotes.getVotes(address) returns(uint256)": [],
    "SafeMath.tryAdd(uint256,uint256) returns(bool,uint256)": [],
    "SafeMathMemoryCheck.modMemoryCheck() returns(uint256)": [],
    "GovernorSettings._setVotingDelay(uint256) returns()": [],
    "SampleChild.__SampleChild_init_unchained(uint256) returns()": [
        [
            "onlyInitializing"
        ],
        [
            "_initializing",
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "SafeMath.trySub(uint256,uint256) returns(bool,uint256)": [],
    "Clones.clone(address) returns(address)": [
        [
            "NEQ",
            [
                "instance"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC1167: create failed"
        ]
    ],
    "GovernorSettings._setVotingPeriod(uint256) returns()": [
        [
            "GT",
            [
                "uint256_1",
                "newVotingPeriod"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:GovernorSettings: voting period too low"
        ]
    ],
    "ERC20.totalSupply() returns(uint256)": [],
    "Ownable2Step.transferOwnership(address) returns()": [
        [
            [
                "onlyOwner",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ]
    ],
    "ERC1967Upgrade._getBeacon() returns(address)": [],
    "BitMaps.unset(BitMaps.BitMap,uint256) returns()": [],
    "ERC721._afterTokenTransfer(address,address,uint256,uint256) returns()": [],
    "ERC1155PresetMinterPauser.supportsInterface(bytes4) returns(bool)": [],
    "TimersTimestampImpl.isExpired() returns(bool)": [],
    "Checkpoints.push(Checkpoints.History,uint256) returns(uint256,uint256)": [
        [
            "LTE",
            [
                "_blockNumber@_unsafeAccess(self,pos - 1)",
                "_blockNumber@last"
            ],
            [
                "key"
            ],
            "#Medium#ERROR_MSG:Checkpoint: decreasing keys"
        ],
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ]
    ],
    "Ownable2Step._transferOwnership(address) returns()": [],
    "ERC20Permit._useNonce(address) returns(uint256)": [],
    "DisableNew.constructor() returns()": [],
    "CompTimelock.constructor(address,uint256) returns()": [],
    "ERC20Votes.clock() returns(uint48)": [
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "Governor.getVotes(address,uint256) returns(uint256)": [],
    "ERC1155PresetMinterPauser._beforeTokenTransfer(address,address,address,uint256[],uint256[],bytes) returns()": [
        [
            "NOT",
            [
                "paused()",
                [
                    "_paused"
                ]
            ],
            "#Medium#ERROR_MSG:ERC1155Pausable: token transfer while paused"
        ]
    ],
    "Ownable2Step.acceptOwnership() returns()": [
        [
            "EQ",
            [
                "pendingOwner()",
                [
                    "_pendingOwner"
                ]
            ],
            [
                "_msgSender()",
                "newOwner",
                "sender",
                "msgsender"
            ],
            "#Medium#ERROR_MSG:Ownable2Step: caller is not the new owner"
        ]
    ],
    "Checkpoints.push(Checkpoints.History,function(uint256,uint256) returns(uint256),uint256) returns(uint256,uint256)": [
        [
            "LTE",
            [
                "_blockNumber@_unsafeAccess(self,pos - 1)",
                "_blockNumber@last"
            ],
            [
                "key"
            ],
            "#Medium#ERROR_MSG:Checkpoint: decreasing keys"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ]
    ],
    "DoubleEndedQueue.pushBack(DoubleEndedQueue.Bytes32Deque,bytes32) returns()": [],
    "ERC1155Receiver.supportsInterface(bytes4) returns(bool)": [],
    "Checkpoints.latest(Checkpoints.History) returns(uint224)": [],
    "CrossChainEnabledPolygonChild.constructor(address) returns()": [],
    "DoubleEndedQueue.popBack(DoubleEndedQueue.Bytes32Deque) returns(bytes32)": [
        [
            "NOT",
            [
                "empty(deque)",
                [
                    "LTE",
                    [
                        "_end@deque"
                    ],
                    [
                        "_begin@deque"
                    ]
                ]
            ],
            "#Low#ERROR_MSG:Empty()()"
        ]
    ],
    "ERC20PresetMinterPauser.constructor(string,string) returns()": [],
    "Checkpoints.latestCheckpoint(Checkpoints.History) returns(bool,uint32,uint224)": [],
    "DoubleEndedQueue.pushFront(DoubleEndedQueue.Bytes32Deque,bytes32) returns()": [],
    "Checkpoints.length(Checkpoints.History) returns(uint256)": [],
    "CrossChainEnabledPolygonChild._isCrossChain() returns(bool)": [],
    "ERC721.approve(address,uint256) returns()": [
        [
            "NEQ",
            [
                "to",
                "address_1"
            ],
            [
                "ownerOf(tokenId)",
                "owner"
            ],
            "#Low#ERROR_MSG:ERC721: approval to current owner"
        ],
        [
            [
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "ownerOf(tokenId)",
                        "owner"
                    ]
                ],
                [
                    "isApprovedForAll(owner,_msgSender())",
                    [
                        "_operatorApprovals@owner@operator"
                    ]
                ]
            ],
            "#High#ERROR_MSG:ERC721: approve caller is not token owner or approved for all"
        ],
        [
            "NEQ",
            [
                "_ownerOf(tokenId)",
                "_owners@tokenId",
                "owner"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: invalid token ID"
        ]
    ],
    "DoubleEndedQueue.popFront(DoubleEndedQueue.Bytes32Deque) returns(bytes32)": [
        [
            "NOT",
            [
                "empty(deque)",
                [
                    "LTE",
                    [
                        "_end@deque"
                    ],
                    [
                        "frontIndex",
                        "_begin@deque"
                    ]
                ]
            ],
            "#Low#ERROR_MSG:Empty()()"
        ]
    ],
    "Uint256ArraysMock.constructor(uint256[]) returns()": [],
    "CompTimelock.receive() returns()": [],
    "ERC20PresetMinterPauser.mint(address,uint256) returns()": [
        [
            [
                "hasRole(MINTER_ROLE,_msgSender())",
                [
                    "members@_roles@role@account"
                ],
                "onlyRole",
                [
                    "EQ",
                    [
                        "msgsender",
                        "_msgSender()"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth",
                        "gov"
                    ]
                ]
            ],
            "#High#ERROR_MSG:ERC20PresetMinterPauser: must have minter role to mint"
        ],
        [
            "NEQ",
            [
                "to",
                "account",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: mint to the zero address"
        ]
    ],
    "Checkpoints._insert(Checkpoints.Checkpoint[],uint32,uint224) returns(uint224,uint224)": [
        [
            "LTE",
            [
                "_blockNumber@_unsafeAccess(self,pos - 1)",
                "_blockNumber@last"
            ],
            [
                "uint32_1",
                "key"
            ],
            "#Medium#ERROR_MSG:Checkpoint: decreasing keys"
        ]
    ],
    "ERC777.name() returns(string)": [],
    "ERC1155._doSafeTransferAcceptanceCheck(address,address,address,uint256,uint256,bytes) returns()": [
        [
            "NEQ",
            [
                "selector@onERC1155Received@IERC1155Receiver"
            ],
            [
                "response"
            ],
            "#High#ERROR_MSG:(ERC1155: ERC1155Receiver rejected tokens)"
        ]
    ],
    "CrossChainEnabledPolygonChild._crossChainSender() returns(address)": [
        [
            "onlyCrossChain"
        ],
        [
            "NOT",
            [
                "_isCrossChain()",
                [
                    "EQ",
                    [
                        "msgsender"
                    ],
                    [
                        "_fxChild",
                        "address"
                    ]
                ]
            ],
            "#High#ERROR_MSG:NotCrossChainCall()()"
        ]
    ],
    "DoubleEndedQueue.front(DoubleEndedQueue.Bytes32Deque) returns(bytes32)": [
        [
            "NOT",
            [
                "empty(deque)",
                [
                    "LTE",
                    [
                        "_end@deque"
                    ],
                    [
                        "frontIndex",
                        "_begin@deque"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Empty()()"
        ]
    ],
    "CompTimelock.setDelay(uint256) returns()": [
        [
            "EQ",
            [
                "msgsender"
            ],
            [
                "address(this)"
            ],
            "#Medium#ERROR_MSG:Timelock::setDelay: Call must come from Timelock."
        ],
        [
            "GTE",
            [
                "uint256_1",
                "delay_"
            ],
            [
                "MINIMUM_DELAY",
                "172800",
                "uint256"
            ],
            "#Medium#ERROR_MSG:Timelock::setDelay: Delay must exceed minimum delay."
        ],
        [
            "LTE",
            [
                "uint256_1",
                "delay_"
            ],
            [
                "2592000",
                "MAXIMUM_DELAY",
                "uint256"
            ],
            "#Medium#ERROR_MSG:Timelock::setDelay: Delay must not exceed maximum delay."
        ]
    ],
    "Uint256ArraysMock.findUpperBound(uint256) returns(uint256)": [],
    "ERC20PresetMinterPauser.pause() returns()": [
        [
            [
                "hasRole(MINTER_ROLE,_msgSender())",
                [
                    "members@_roles@role@account"
                ],
                "onlyRole",
                [
                    "EQ",
                    [
                        "msgsender",
                        "_msgSender()"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth",
                        "gov"
                    ]
                ]
            ],
            "#High#ERROR_MSG:ERC20PresetMinterPauser: must have pauser role to pause"
        ],
        [
            "whenNotPaused"
        ]
    ],
    "Checkpoints._upperBinaryLookup(Checkpoints.Checkpoint[],uint32,uint256,uint256) returns(uint256)": [],
    "CrossChainEnabledPolygonChild.processMessageFromRoot(uint256,address,bytes) returns()": [
        [
            "nonReentrant"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ],
        [
            "NOT",
            [
                "_isCrossChain()",
                [
                    "EQ",
                    [
                        "msgsender"
                    ],
                    [
                        "_fxChild",
                        "address"
                    ]
                ]
            ],
            "#High#ERROR_MSG:NotCrossChainCall()()"
        ]
    ],
    "DoubleEndedQueue.back(DoubleEndedQueue.Bytes32Deque) returns(bytes32)": [
        [
            "NOT",
            [
                "empty(deque)",
                [
                    "LTE",
                    [
                        "_end@deque"
                    ],
                    [
                        "_begin@deque"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Empty()()"
        ]
    ],
    "CompTimelock.acceptAdmin() returns()": [
        [
            "EQ",
            [
                "msgsender"
            ],
            [
                "pendingAdmin",
                "address"
            ],
            "#Medium#ERROR_MSG:Timelock::acceptAdmin: Call must come from pendingAdmin."
        ]
    ],
    "ERC20PresetMinterPauser.unpause() returns()": [
        [
            [
                "hasRole(PAUSER_ROLE,_msgSender())",
                [
                    "members@_roles@role@account"
                ],
                "onlyRole",
                [
                    "EQ",
                    [
                        "msgsender",
                        "_msgSender()"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth",
                        "gov"
                    ]
                ]
            ],
            "#High#ERROR_MSG:ERC20PresetMinterPauser: must have pauser role to unpause"
        ],
        [
            "whenPaused"
        ]
    ],
    "Uint256ArraysMock.unsafeAccess(uint256) returns(uint256)": [],
    "Checkpoints._lowerBinaryLookup(Checkpoints.Checkpoint[],uint32,uint256,uint256) returns(uint256)": [],
    "PaymentSplitter.constructor(address[],uint256[]) returns()": [],
    "DoubleEndedQueue.at(DoubleEndedQueue.Bytes32Deque,uint256) returns(bytes32)": [
        [
            "LTE",
            [
                "value",
                "uint256_1",
                "index"
            ],
            [
                "max)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in an int256"
        ],
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "value"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 128 bits"
        ],
        [
            "LT",
            [
                "_end@deque"
            ],
            [
                "idx",
                "toInt256(index))"
            ],
            "#Medium#ERROR_MSG:OutOfBounds()()"
        ]
    ],
    "CompTimelock.setPendingAdmin(address) returns()": [
        [
            "EQ",
            [
                "msgsender"
            ],
            [
                "address(this)"
            ],
            "#Medium#ERROR_MSG:Timelock::setPendingAdmin: Call must come from Timelock."
        ]
    ],
    "ERC20PresetMinterPauser._beforeTokenTransfer(address,address,uint256) returns()": [
        [
            "NOT",
            [
                "paused()",
                [
                    "_paused"
                ]
            ],
            "#Medium#ERROR_MSG:ERC20Pausable: token transfer while paused"
        ]
    ],
    "Checkpoints._unsafeAccess(Checkpoints.Checkpoint[],uint256) returns(Checkpoints.Checkpoint)": [],
    "AddressArraysMock.constructor(address[]) returns()": [],
    "CrossChainEnabled.onlyCrossChain() returns()": [
        [
            "NOT",
            [
                "_isCrossChain()",
                "None"
            ],
            "#High#ERROR_MSG:NotCrossChainCall()()"
        ]
    ],
    "GovernorWithParamsMock.slitherConstructorConstantVariables() returns()": [],
    "DoubleEndedQueue.clear(DoubleEndedQueue.Bytes32Deque) returns()": [],
    "Proxy._implementation() returns(address)": [],
    "CompTimelock.queueTransaction(address,uint256,string,bytes,uint256) returns(bytes32)": [
        [
            "EQ",
            [
                "msgsender"
            ],
            [
                "admin",
                "address"
            ],
            "#Medium#ERROR_MSG:Timelock::queueTransaction: Call must come from admin."
        ],
        [
            "GTE",
            [
                "eta",
                "uint256_2"
            ],
            [
                "ADD",
                [
                    "getBlockTimestamp()",
                    "timestamp"
                ],
                [
                    "delay",
                    "uint256"
                ]
            ],
            "#Medium#ERROR_MSG:Timelock::queueTransaction: Estimated execution block must satisfy delay."
        ]
    ],
    "Checkpoints.push(Checkpoints.Trace224,uint32,uint224) returns(uint224,uint224)": [
        [
            "LTE",
            [
                "_key@_unsafeAccess(self,pos - 1)",
                "_key@last"
            ],
            [
                "key",
                "uint32_1"
            ],
            "#Medium#ERROR_MSG:Checkpoint: decreasing keys"
        ]
    ],
    "ERC721.setApprovalForAll(address,bool) returns()": [
        [
            "NEQ",
            [
                "_msgSender()",
                "msg.sender",
                "owner"
            ],
            [
                "operator",
                "address_1"
            ],
            "#Low#ERROR_MSG:ERC721: approve to caller"
        ]
    ],
    "AddressArraysMock.unsafeAccess(uint256) returns(address)": [],
    "DoubleEndedQueue.length(DoubleEndedQueue.Bytes32Deque) returns(uint256)": [],
    "CompTimelock.cancelTransaction(address,uint256,string,bytes,uint256) returns()": [
        [
            "EQ",
            [
                "msgsender"
            ],
            [
                "admin",
                "address"
            ],
            "#Medium#ERROR_MSG:Timelock::cancelTransaction: Call must come from admin."
        ]
    ],
    "Checkpoints.lowerLookup(Checkpoints.Trace224,uint32) returns(uint224)": [],
    "Bytes32ArraysMock.constructor(bytes32[]) returns()": [],
    "ERC777.decimals() returns(uint8)": [],
    "DoubleEndedQueue.empty(DoubleEndedQueue.Bytes32Deque) returns(bool)": [],
    "GovernorMock.proposalThreshold() returns(uint256)": [],
    "GovernorVoteMocks.votingDelay() returns(uint256)": [],
    "ERC1967Upgrade._getAdmin() returns(address)": [],
    "ERC20Snapshot._getCurrentSnapshotId() returns(uint256)": [],
    "GovernorMock.propose(address[],uint256[],bytes[],string) returns(uint256)": [
        [
            [
                "_isValidDescriptionForProposer(proposer,description)"
            ],
            "#High#ERROR_MSG:Governor: proposer restricted"
        ],
        [
            "GTE",
            [
                "getVotes(proposer,currentTimepoint - 1)",
                "_getVotes(account,timepoint,_defaultParams())"
            ],
            [
                "proposalThreshold()",
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: proposer votes below proposal threshold"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@values"
            ],
            "#Medium#ERROR_MSG:Governor: invalid proposal length"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@calldatas"
            ],
            "#Medium#ERROR_MSG:Governor: invalid proposal length"
        ],
        [
            "GT",
            [
                "length@targets"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: empty proposal"
        ],
        [
            "EQ",
            [
                "voteStart@_proposals@hashProposal(targets,values,calldatas,keccak256(bytes)(bytes(description)))",
                "voteStart@_proposals@encode(targets,values,calldatas,descriptionHash)))",
                "voteStart@_proposals@proposalId"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: proposal already exists"
        ],
        [
            "LTE",
            [
                "value",
                "snapshot",
                "deadline",
                "snapshot + votingPeriod()",
                "currentTimepoint + votingDelay()"
            ],
            [
                "max@type()(uint64)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 64 bits"
        ]
    ],
    "Governor._castVote(uint256,address,uint8,string,bytes) returns(uint256)": [
        [
            "EQ",
            [
                "state(proposalId)"
            ],
            [
                "Active@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: vote not currently active"
        ],
        [
            "EQ",
            [
                "0"
            ],
            [
                "proposalSnapshot(proposalId)",
                "REF_1872",
                "voteStart@proposal",
                "voteStart@_proposals@proposalId",
                "snapshot"
            ],
            "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
        ]
    ],
    "GovernorVoteMocks.votingPeriod() returns(uint256)": [],
    "ERC20Snapshot.balanceOfAt(address,uint256) returns(uint256)": [
        [
            "GT",
            [
                "uint256_1",
                "snapshotId",
                "element"
            ],
            [
                "0"
            ],
            "#Low#ERROR_MSG:ERC20Snapshot: id is 0"
        ],
        [
            "LTE",
            [
                "uint256_1",
                "snapshotId",
                "element"
            ],
            [
                "_getCurrentSnapshotId()",
                "current()"
            ],
            "#Low#ERROR_MSG:ERC20Snapshot: nonexistent id"
        ]
    ],
    "GovernorPreventLateQuorumMock.constructor(uint256) returns()": [],
    "GovernorWithParamsMock.quorum(uint256) returns(uint256)": [],
    "Proxy._delegate(address) returns()": [],
    "ERC20Snapshot.totalSupplyAt(uint256) returns(uint256)": [
        [
            "GT",
            [
                "snapshotId",
                "element",
                "uint256_1"
            ],
            [
                "0"
            ],
            "#Low#ERROR_MSG:ERC20Snapshot: id is 0"
        ],
        [
            "LTE",
            [
                "snapshotId",
                "element",
                "uint256_1"
            ],
            [
                "_getCurrentSnapshotId()",
                "current()"
            ],
            "#Low#ERROR_MSG:ERC20Snapshot: nonexistent id"
        ]
    ],
    "GovernorWithParamsMock.votingDelay() returns(uint256)": [],
    "GovernorPreventLateQuorum.setLateQuorumVoteExtension(uint64) returns()": [
        [
            [
                "onlyGovernance"
            ],
            [
                "EQ",
                [
                    "_msgSender()",
                    "msgsender"
                ],
                [
                    "_executor()",
                    "address(this)"
                ]
            ],
            "#High#ERROR_MSG:Governor: onlyGovernance"
        ]
    ],
    "GovernorPreventLateQuorumMock.quorum(uint256) returns(uint256)": [],
    "ERC1967Upgrade._getImplementation() returns(address)": [],
    "ERC20Snapshot._beforeTokenTransfer(address,address,uint256) returns()": [],
    "GovernorWithParamsMock.votingPeriod() returns(uint256)": [],
    "GovernorPreventLateQuorumMock.proposalDeadline(uint256) returns(uint256)": [],
    "ERC20Snapshot._valueAt(uint256,ERC20Snapshot.Snapshots) returns(bool,uint256)": [
        [
            "GT",
            [
                "uint256_1",
                "snapshotId",
                "element"
            ],
            [
                "0"
            ],
            "#Low#ERROR_MSG:ERC20Snapshot: id is 0"
        ],
        [
            "LTE",
            [
                "uint256_1",
                "snapshotId",
                "element"
            ],
            [
                "_getCurrentSnapshotId()",
                "current()"
            ],
            "#Low#ERROR_MSG:ERC20Snapshot: nonexistent id"
        ]
    ],
    "GovernorWithParamsMock._getVotes(address,uint256,bytes) returns(uint256)": [],
    "GovernorPreventLateQuorumMock.proposalThreshold() returns(uint256)": [],
    "ERC1967Upgrade._changeAdmin(address) returns()": [
        [
            "NEQ",
            [
                "newAdmin",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC1967: new admin is the zero address"
        ]
    ],
    "ERC20Snapshot._updateAccountSnapshot(address) returns()": [],
    "GovernorWithParamsMock._countVote(uint256,address,uint8,uint256,bytes) returns()": [
        [
            "NOT",
            [
                "hasVoted@_proposalVotes@proposalId@account",
                "hasVoted@proposalVote@account"
            ],
            "#Medium#ERROR_MSG:GovernorVotingSimple: vote already cast"
        ]
    ],
    "GovernorPreventLateQuorumMock._castVote(uint256,address,uint8,string,bytes) returns(uint256)": [
        [
            "EQ",
            [
                "state(proposalId)"
            ],
            [
                "Active@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: vote not currently active"
        ]
    ],
    "ERC1155.constructor(string) returns()": [],
    "IGovernor.clock() returns(uint48)": [],
    "ERC20Snapshot._updateTotalSupplySnapshot() returns()": [],
    "UUPSUpgradeableLegacyMock.__setImplementation(address) returns()": [
        [
            [
                "isContract(newImplementation)"
            ],
            "#Medium#ERROR_MSG:ERC1967: new implementation is not a contract"
        ]
    ],
    "GovernorTimelockCompoundMock.supportsInterface(bytes4) returns(bool)": [],
    "ERC1967Upgrade._upgradeTo(address) returns()": [
        [
            [
                "isContract(newImplementation)"
            ],
            "#Medium#ERROR_MSG:ERC1967: new implementation is not a contract"
        ]
    ],
    "ERC20Snapshot._updateSnapshot(ERC20Snapshot.Snapshots,uint256) returns()": [],
    "Proxy._fallback() returns()": [],
    "CrossChainEnabledPolygonChild.slitherConstructorVariables() returns()": [],
    "GovernorTimelockCompoundMock.quorum(uint256) returns(uint256)": [
        [
            "LTE",
            [
                "blockNumber",
                "uint256_1",
                "timepoint",
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ]
    ],
    "UUPSUpgradeableLegacyMock._upgradeToAndCallSecureLegacyV1(address,bytes,bool) returns()": [
        [
            "EQ",
            [
                "_getImplementation()",
                "value@getAddressSlot(_IMPLEMENTATION_SLOT)",
                "oldImplementation"
            ],
            [
                "_getImplementation()",
                [
                    "_getImplementation()",
                    "value@getAddressSlot(_IMPLEMENTATION_SLOT)",
                    "oldImplementation"
                ]
            ],
            "#Medium#ERROR_MSG:ERC1967Upgrade: upgrade breaks further upgrades"
        ],
        [
            [
                "isContract(newImplementation)"
            ],
            "#Medium#ERROR_MSG:ERC1967: new implementation is not a contract"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "ERC20Snapshot._lastSnapshotId(uint256[]) returns(uint256)": [],
    "UUPSUpgradeableLegacyMock.upgradeTo(address) returns()": [
        [
            "EQ",
            [
                "_getImplementation()",
                "value@getAddressSlot(_IMPLEMENTATION_SLOT)",
                "oldImplementation"
            ],
            [
                "_getImplementation()",
                [
                    "_getImplementation()",
                    "value@getAddressSlot(_IMPLEMENTATION_SLOT)",
                    "oldImplementation"
                ]
            ],
            "#Medium#ERROR_MSG:ERC1967Upgrade: upgrade breaks further upgrades"
        ],
        [
            [
                "isContract(newImplementation)"
            ],
            "#Medium#ERROR_MSG:ERC1967: new implementation is not a contract"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "ERC1967Upgrade._setBeacon(address) returns()": [
        [
            [
                "isContract(newBeacon)"
            ],
            "#Medium#ERROR_MSG:ERC1967: new beacon is not a contract"
        ],
        [
            [
                "implementation())"
            ],
            "#Medium#ERROR_MSG:ERC1967: beacon implementation is not a contract"
        ]
    ],
    "GovernorTimelockCompoundMock.state(uint256) returns(IGovernor.ProposalState)": [],
    "UUPSUpgradeableLegacyMock.upgradeToAndCall(address,bytes) returns()": [
        [
            "EQ",
            [
                "_getImplementation()",
                "value@getAddressSlot(_IMPLEMENTATION_SLOT)",
                "oldImplementation"
            ],
            [
                "_getImplementation()",
                [
                    "_getImplementation()",
                    "value@getAddressSlot(_IMPLEMENTATION_SLOT)",
                    "oldImplementation"
                ]
            ],
            "#Medium#ERROR_MSG:ERC1967Upgrade: upgrade breaks further upgrades"
        ],
        [
            [
                "isContract(newImplementation)"
            ],
            "#Medium#ERROR_MSG:ERC1967: new implementation is not a contract"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "IGovernor.COUNTING_MODE() returns(string)": [],
    "Governor._getVotes(address,uint256,bytes) returns(uint256)": [],
    "GovernorCompMock.slitherConstructorConstantVariables() returns()": [],
    "GovernorTimelockCompoundMock.proposalThreshold() returns(uint256)": [],
    "ERC1967Upgrade._upgradeToAndCallUUPS(address,bytes,bool) returns()": [
        [
            "EQ",
            [
                "slot"
            ],
            [
                "slot",
                "_IMPLEMENTATION_SLOT",
                "bytes32"
            ],
            "#Medium#ERROR_MSG:ERC1967Upgrade: unsupported proxiableUUID"
        ],
        [
            [
                "isContract(newImplementation)"
            ],
            "#Medium#ERROR_MSG:ERC1967: new implementation is not a contract"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "ERC1155ReceiverMock.constructor(bytes4,bool,bytes4,bool) returns()": [],
    "GovernorCompatibilityBravo._encodeCalldata(string[],bytes[]) returns(bytes[])": [],
    "GovernorSettings._setProposalThreshold(uint256) returns()": [],
    "BeaconProxy._setBeacon(address,bytes) returns()": [
        [
            [
                "isContract(newBeacon)"
            ],
            "#Medium#ERROR_MSG:ERC1967: new beacon is not a contract"
        ],
        [
            [
                "implementation())"
            ],
            "#Medium#ERROR_MSG:ERC1967: beacon implementation is not a contract"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "ERC1155._burnBatch(address,uint256[],uint256[]) returns()": [
        [
            "NEQ",
            [
                "from",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC1155: burn from the zero address"
        ],
        [
            "EQ",
            [
                "length@ids"
            ],
            [
                "length@amounts"
            ],
            "#Low#ERROR_MSG:ERC1155: ids and amounts length mismatch"
        ],
        [
            "GTE",
            [
                "_balances@ids@i@from",
                "_balances@ids",
                "fromBalance",
                "_balances@id@from"
            ],
            [
                "amount",
                "amounts",
                "amounts@i"
            ],
            "#Medium#ERROR_MSG:ERC1155: burn amount exceeds balance"
        ]
    ],
    "IAccessControlDefaultAdminRules.beginDefaultAdminTransfer(address) returns()": [],
    "Counters.reset(Counters.Counter) returns()": [],
    "StorageSlotMock.getString(bytes32) returns(string)": [],
    "GovernorCountingSimple.hasVoted(uint256,address) returns(bool)": [],
    "Clones.cloneDeterministic(address,bytes32) returns(address)": [
        [
            "NEQ",
            [
                "instance"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC1167: create2 failed"
        ]
    ],
    "GovernorCompatibilityBravo._getProposalParameters(uint256) returns(address[],uint256[],bytes[],bytes32)": [],
    "Create2.deploy(uint256,bytes32,bytes) returns(address)": [
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "uint256_1",
                "amount"
            ],
            "#Medium#ERROR_MSG:Create2: insufficient balance"
        ],
        [
            "NEQ",
            [
                "length@bytecode"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:Create2: bytecode length is zero"
        ],
        [
            "NEQ",
            [
                "addr"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:Create2: Failed on deploy"
        ]
    ],
    "StorageSlotMock.getStringStorage(uint256) returns(string)": [],
    "Clones.predictDeterministicAddress(address,bytes32,address) returns(address)": [],
    "GovernorCompatibilityBravo._storeProposal(address,address[],uint256[],string[],bytes[],string) returns()": [],
    "ERC4626._tryGetAssetDecimals(IERC20) returns(bool,uint8)": [],
    "Create2.computeAddress(bytes32,bytes32) returns(address)": [],
    "StorageSlotMock.setBytes(bytes32,bytes) returns()": [],
    "Clones.predictDeterministicAddress(address,bytes32) returns(address)": [],
    "Create2.computeAddress(bytes32,bytes32,address) returns(address)": [],
    "StorageSlotMock.setBytesStorage(uint256,bytes) returns()": [],
    "SafeERC20.safeTransfer(IERC20,address,uint256) returns()": [
        [
            [
                [
                    "EQ",
                    [
                        "length@functionCall(data,SafeERC20: low-level call failed)",
                        "length@returndata"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ],
                [
                    "decode(returndata,(bool))"
                ]
            ],
            "#Medium#ERROR_MSG:SafeERC20: ERC20 operation did not succeed"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "ShortStrings.toShortString(string) returns(ShortString)": [
        [
            "LTE",
            [
                "31"
            ],
            [
                "length@bytes(str)",
                "length@bstr"
            ],
            "#Low#ERROR_MSG:StringTooLong(string)(str)"
        ]
    ],
    "StorageSlotMock.getBytes(bytes32) returns(bytes)": [],
    "SafeERC20.safeTransferFrom(IERC20,address,address,uint256) returns()": [
        [
            [
                [
                    "EQ",
                    [
                        "length@functionCall(data,SafeERC20: low-level call failed)",
                        "length@returndata"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ],
                [
                    "decode(returndata,(bool))"
                ]
            ],
            "#Medium#ERROR_MSG:SafeERC20: ERC20 operation did not succeed"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "GovernorCompatibilityBravo.getReceipt(uint256,address) returns(IGovernorCompatibilityBravo.Receipt)": [],
    "IAccessControlDefaultAdminRules.acceptDefaultAdminTransfer() returns()": [],
    "ERC1155._doSafeBatchTransferAcceptanceCheck(address,address,address,uint256[],uint256[],bytes) returns()": [
        [
            "NEQ",
            [
                "selector@onERC1155BatchReceived@IERC1155Receiver"
            ],
            [
                "response"
            ],
            "#High#ERROR_MSG:(ERC1155: ERC1155Receiver rejected tokens)"
        ]
    ],
    "StorageSlotMock.getBytesStorage(uint256) returns(bytes)": [],
    "SafeERC20.safeApprove(IERC20,address,uint256) returns()": [
        [
            [
                [
                    [
                        "EQ",
                        [
                            "uint256_1",
                            "value"
                        ],
                        [
                            "value",
                            "0"
                        ]
                    ]
                ],
                [
                    [
                        "EQ",
                        [
                            "allowance(address(this),spender)"
                        ],
                        [
                            "value",
                            "0"
                        ]
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:SafeERC20: approve from non-zero to non-zero allowance"
        ],
        [
            [
                [
                    "EQ",
                    [
                        "length@functionCall(data,SafeERC20: low-level call failed)",
                        "length@returndata"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ],
                [
                    "decode(returndata,(bool))"
                ]
            ],
            "#Medium#ERROR_MSG:SafeERC20: ERC20 operation did not succeed"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "ShortStrings.toString(ShortString) returns(string)": [
        [
            "LTE",
            [
                "31"
            ],
            [
                "result",
                "unwrap(sstr)) & 0xFF"
            ],
            "#Low#ERROR_MSG:InvalidShortString()()"
        ]
    ],
    "GovernorCompatibilityBravo.quorumVotes() returns(uint256)": [],
    "GovernorCountingSimple._quorumReached(uint256) returns(bool)": [],
    "ERC1155._asSingletonArray(uint256) returns(uint256[])": [],
    "TimelockReentrant.disableReentrancy() returns()": [],
    "SafeERC20.safeIncreaseAllowance(IERC20,address,uint256) returns()": [
        [
            [
                [
                    "EQ",
                    [
                        "length@functionCall(data,SafeERC20: low-level call failed)",
                        "length@returndata"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ],
                [
                    "decode(returndata,(bool))"
                ]
            ],
            "#Medium#ERROR_MSG:SafeERC20: ERC20 operation did not succeed"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "ShortStrings.byteLength(ShortString) returns(uint256)": [
        [
            "LTE",
            [
                "31"
            ],
            [
                "result",
                "unwrap(sstr)) & 0xFF"
            ],
            "#Low#ERROR_MSG:InvalidShortString()()"
        ]
    ],
    "GovernorCompatibilityBravo.hasVoted(uint256,address) returns(bool)": [],
    "Initializable.initializer() returns()": [
        [
            [
                [
                    [
                        "! _initializing",
                        "isTopLevelCall"
                    ],
                    [
                        "LT",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ],
                [
                    [
                        "NOT",
                        [
                            "isContract(address(this))"
                        ]
                    ],
                    [
                        "EQ",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ]
            ],
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "ERC1155Burnable.burn(address,uint256,uint256) returns()": [
        [
            [
                [
                    "EQ",
                    [
                        "from",
                        "account",
                        "address_1"
                    ],
                    [
                        "_msgSender()",
                        "operator",
                        "msgsender"
                    ]
                ],
                [
                    "isApprovedForAll(account,_msgSender())",
                    [
                        "_operatorApprovals@account@operator"
                    ]
                ]
            ],
            "#High#ERROR_MSG:ERC1155: caller is not token owner or approved"
        ],
        [
            "NEQ",
            [
                "from",
                "account",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC1155: burn from the zero address"
        ],
        [
            "GTE",
            [
                "fromBalance",
                "_balances@element",
                "_balances@id@account",
                "_balances@id@from",
                "_balances@id"
            ],
            [
                "amount",
                "element",
                "uint256_2",
                "value"
            ],
            "#Medium#ERROR_MSG:ERC1155: burn amount exceeds balance"
        ]
    ],
    "IAccessControlDefaultAdminRules.rollbackDefaultAdminDelay() returns()": [],
    "SafeERC20.safeDecreaseAllowance(IERC20,address,uint256) returns()": [
        [
            "GTE",
            [
                "oldAllowance",
                "allowance(address(this),spender)"
            ],
            [
                "uint256_1",
                "value"
            ],
            "#High#ERROR_MSG:SafeERC20: decreased allowance below zero"
        ],
        [
            [
                [
                    "EQ",
                    [
                        "length@functionCall(data,SafeERC20: low-level call failed)",
                        "length@returndata"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ],
                [
                    "decode(returndata,(bool))"
                ]
            ],
            "#Medium#ERROR_MSG:SafeERC20: ERC20 operation did not succeed"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "ShortStrings.toShortStringWithFallback(string,string) returns(ShortString)": [
        [
            "LTE",
            [
                "31"
            ],
            [
                "length@bytes(str)",
                "length@bstr"
            ],
            "#Low#ERROR_MSG:StringTooLong(string)(str)"
        ]
    ],
    "GovernorCompatibilityBravo._quorumReached(uint256) returns(bool)": [],
    "ERC1155Burnable.burnBatch(address,uint256[],uint256[]) returns()": [
        [
            [
                [
                    "EQ",
                    [
                        "from",
                        "account",
                        "address_1"
                    ],
                    [
                        "_msgSender()",
                        "operator",
                        "msgsender"
                    ]
                ],
                [
                    "isApprovedForAll(account,_msgSender())",
                    [
                        "_operatorApprovals@account@operator"
                    ]
                ]
            ],
            "#High#ERROR_MSG:ERC1155: caller is not token owner or approved"
        ],
        [
            "NEQ",
            [
                "from",
                "account",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC1155: burn from the zero address"
        ],
        [
            "EQ",
            [
                "length@ids"
            ],
            [
                "length@amounts"
            ],
            "#Low#ERROR_MSG:ERC1155: ids and amounts length mismatch"
        ],
        [
            "GTE",
            [
                "_balances@ids@i@from",
                "_balances@ids",
                "_balances@id@account",
                "_balances@id@from",
                "_balances@ids@i",
                "fromBalance",
                "_balances@ids@i@account",
                "_balances@id"
            ],
            [
                "amount",
                "amounts",
                "values@i",
                "amounts@i"
            ],
            "#Medium#ERROR_MSG:ERC1155: burn amount exceeds balance"
        ]
    ],
    "TimelockReentrant.enableRentrancy(address,bytes) returns()": [],
    "SafeERC20.forceApprove(IERC20,address,uint256) returns()": [
        [
            [
                [
                    "EQ",
                    [
                        "length@functionCall(data,SafeERC20: low-level call failed)",
                        "length@returndata"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ],
                [
                    "decode(returndata,(bool))"
                ]
            ],
            "#Medium#ERROR_MSG:SafeERC20: ERC20 operation did not succeed"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "ShortStrings.toStringWithFallback(ShortString,string) returns(string)": [
        [
            "LTE",
            [
                "31"
            ],
            [
                "result",
                "unwrap(sstr)) & 0xFF"
            ],
            "#Low#ERROR_MSG:InvalidShortString()()"
        ]
    ],
    "ERC1155Pausable._beforeTokenTransfer(address,address,address,uint256[],uint256[],bytes) returns()": [
        [
            "NOT",
            [
                "paused()",
                [
                    "_paused"
                ]
            ],
            "#Medium#ERROR_MSG:ERC1155Pausable: token transfer while paused"
        ]
    ],
    "TimelockReentrant.reenter() returns()": [
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "Initializable.onlyInitializing() returns()": [
        [
            "_initializing",
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "LibAMB.isCrossChain(address) returns(bool)": [],
    "GovernorCompatibilityBravo._countVote(uint256,address,uint8,uint256,bytes) returns()": [
        [
            "NOT",
            [
                "hasVoted@receipts@_proposalDetails@proposalId@account",
                "hasVoted@receipts@details@account",
                "hasVoted@receipt"
            ],
            "#Medium#ERROR_MSG:GovernorCompatibilityBravo: vote already cast"
        ],
        [
            "LTE",
            [
                "weight",
                "uint256_2",
                "value"
            ],
            [
                "max@type()(uint96)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 96 bits"
        ],
        [
            "EQ",
            [
                "Abstain"
            ],
            [
                "support",
                "uint8_1"
            ],
            "#Low#ERROR_MSG:(GovernorCompatibilityBravo: invalid vote type)"
        ]
    ],
    "ERC20Burnable.burn(uint256) returns()": [
        [
            "NEQ",
            [
                "from",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: burn from the zero address"
        ],
        [
            "GTE",
            [
                "_balances@from",
                "_balances@account",
                "accountBalance"
            ],
            [
                "amount",
                "uint256_1"
            ],
            "#Medium#ERROR_MSG:ERC20: burn amount exceeds balance"
        ]
    ],
    "SafeERC20.safePermit(IERC20Permit,address,address,uint256,uint256,uint8,bytes32,bytes32) returns()": [
        [
            "EQ",
            [
                "nonceAfter",
                "nonces(owner)",
                "nonceBefore"
            ],
            [
                "ADD",
                [
                    "nonceAfter",
                    "nonces(owner)",
                    "nonceBefore"
                ],
                [
                    "1"
                ]
            ],
            "#Medium#ERROR_MSG:SafeERC20: permit did not succeed"
        ]
    ],
    "ERC1155.uri(uint256) returns(string)": [],
    "UUPSUpgradeable.slitherConstructorVariables() returns()": [],
    "ERC1155Supply.totalSupply(uint256) returns(uint256)": [],
    "SafeERC20._callOptionalReturn(IERC20,bytes) returns()": [
        [
            [
                [
                    "EQ",
                    [
                        "length@functionCall(data,SafeERC20: low-level call failed)",
                        "length@returndata"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ],
                [
                    "decode(returndata,(bool))"
                ]
            ],
            "#Medium#ERROR_MSG:SafeERC20: ERC20 operation did not succeed"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "LibAMB.crossChainSender(address) returns(address)": [
        [
            "NOT",
            [
                "isCrossChain(bridge)",
                [
                    "EQ",
                    [
                        "msgsender"
                    ],
                    [
                        "address_1",
                        "bridge"
                    ]
                ]
            ],
            "#High#ERROR_MSG:NotCrossChainCall()()"
        ]
    ],
    "TimersBlockNumberImpl.getDeadline() returns(uint64)": [],
    "ERC777._move(address,address,address,uint256,bytes,bytes) returns()": [
        [
            "GTE",
            [
                "_balances@to",
                "_balances@",
                "_balances@from",
                "_balances@operator",
                "fromBalance",
                "_balances@amount"
            ],
            [
                "uint256_1",
                "amount",
                "from",
                "address_2",
                "",
                "operator",
                "address_1",
                "address_3",
                "to"
            ],
            "#Medium#ERROR_MSG:ERC777: transfer amount exceeds balance"
        ]
    ],
    "SafeERC20._callOptionalReturnBool(IERC20,bytes) returns(bool)": [],
    "ERC20Votes.delegate(address) returns()": [
        [
            "LTE",
            [
                "value",
                "newWeight"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "timestamp"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "ConstructorInitializableMock.constructor() returns()": [],
    "MyTokenTimestampBased._afterTokenTransfer(address,address,uint256) returns()": [
        [
            "LTE",
            [
                "value",
                "newWeight"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "ERC721.symbol() returns(string)": [],
    "MyTokenTimestampBased._mint(address,uint256) returns()": [
        [
            "LTE",
            [
                "totalSupply()",
                [
                    "_totalSupply"
                ]
            ],
            [
                "_maxSupply()",
                "max@type()(uint224)"
            ],
            "#Medium#ERROR_MSG:ERC20Votes: total supply risks overflowing votes"
        ],
        [
            "NEQ",
            [
                "to",
                "address_1",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: mint to the zero address"
        ],
        [
            "LTE",
            [
                "value",
                "newWeight"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "ContextMock.msgData(uint256,string) returns()": [],
    "MigratableMockV1.initialize(uint256) returns()": [
        [
            "initializer"
        ],
        [
            [
                [
                    [
                        "! _initializing",
                        "isTopLevelCall"
                    ],
                    [
                        "LT",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ],
                [
                    [
                        "NOT",
                        [
                            "isContract(address(this))"
                        ]
                    ],
                    [
                        "EQ",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ]
            ],
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "ConstructorInitializableMock.initialize() returns()": [
        [
            "initializer"
        ],
        [
            [
                [
                    [
                        "! _initializing",
                        "isTopLevelCall"
                    ],
                    [
                        "LT",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ],
                [
                    [
                        "NOT",
                        [
                            "isContract(address(this))"
                        ]
                    ],
                    [
                        "EQ",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ]
            ],
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "MyTokenTimestampBased._burn(address,uint256) returns()": [
        [
            "NEQ",
            [
                "from",
                "account",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: burn from the zero address"
        ],
        [
            "GTE",
            [
                "_balances@from",
                "_balances@account",
                "accountBalance"
            ],
            [
                "amount",
                "uint256_1",
                "delta"
            ],
            "#Medium#ERROR_MSG:ERC20: burn amount exceeds balance"
        ],
        [
            "LTE",
            [
                "value",
                "newWeight"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "AccessControlEnumerable.getRoleMember(bytes32,uint256) returns(address)": [],
    "Votes.getPastVotes(address,uint256) returns(uint256)": [
        [
            "LT",
            [
                "value",
                "uint256_1",
                "timepoint"
            ],
            [
                "clock()",
                "number)"
            ],
            "#Medium#ERROR_MSG:Votes: future lookup"
        ],
        [
            "LTE",
            [
                "value",
                "uint256_1",
                "timepoint"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "ConstructorInitializableMock.initializeOnlyInitializing() returns()": [
        [
            "onlyInitializing"
        ],
        [
            "_initializing",
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "MyTokenWrapped.constructor(IERC20) returns()": [],
    "ChildConstructorInitializableMock.constructor() returns()": [],
    "MyTokenWrapped.decimals() returns(uint8)": [],
    "ERC721Consecutive._maxBatchSize() returns(uint96)": [],
    "MyTokenWrapped._afterTokenTransfer(address,address,uint256) returns()": [
        [
            "LTE",
            [
                "value",
                "newWeight"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "ChildConstructorInitializableMock.childInitialize() returns()": [
        [
            "initializer"
        ],
        [
            [
                [
                    [
                        "! _initializing",
                        "isTopLevelCall"
                    ],
                    [
                        "LT",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ],
                [
                    [
                        "NOT",
                        [
                            "isContract(address(this))"
                        ]
                    ],
                    [
                        "EQ",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ]
            ],
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "MyTokenWrapped._mint(address,uint256) returns()": [
        [
            "LTE",
            [
                "totalSupply()",
                [
                    "_totalSupply"
                ]
            ],
            [
                "_maxSupply()",
                "max@type()(uint224)"
            ],
            "#Medium#ERROR_MSG:ERC20Votes: total supply risks overflowing votes"
        ],
        [
            "NEQ",
            [
                "address_1",
                "to",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: mint to the zero address"
        ],
        [
            "LTE",
            [
                "value",
                "newWeight"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "ReinitializerMock.getInitializedVersion() returns(uint8)": [],
    "MyTokenWrapped._burn(address,uint256) returns()": [
        [
            "NEQ",
            [
                "account",
                "address_1",
                "from"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: burn from the zero address"
        ],
        [
            "GTE",
            [
                "_balances@from",
                "_balances@account",
                "accountBalance"
            ],
            [
                "amount",
                "delta",
                "uint256_1"
            ],
            "#Medium#ERROR_MSG:ERC20: burn amount exceeds balance"
        ],
        [
            "LTE",
            [
                "value",
                "newWeight"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "GovernorCompMock.quorum(uint256) returns(uint256)": [],
    "ReinitializerMock.initialize() returns()": [
        [
            "initializer"
        ],
        [
            [
                [
                    [
                        "! _initializing",
                        "isTopLevelCall"
                    ],
                    [
                        "LT",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ],
                [
                    [
                        "NOT",
                        [
                            "isContract(address(this))"
                        ]
                    ],
                    [
                        "EQ",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ]
            ],
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ],
        [
            "onlyInitializing"
        ],
        [
            "_initializing",
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "Governor._defaultParams() returns(bytes)": [],
    "CrossChainEnabledAMBMock.slitherConstructorVariables() returns()": [],
    "GovernorCompMock.votingDelay() returns(uint256)": [],
    "ReinitializerMock.reinitialize(uint8) returns()": [
        [
            "reinitializer"
        ],
        [
            "NOT",
            [
                "_initializing",
                "bool"
            ],
            "#Low#ERROR_MSG:Initializable: contract is already initialized"
        ],
        [
            "LT",
            [
                "_initialized",
                "uint8"
            ],
            [
                "uint8_1",
                "i",
                "version"
            ],
            "#Low#ERROR_MSG:Initializable: contract is already initialized"
        ],
        [
            "onlyInitializing"
        ],
        [
            "_initializing",
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "GovernorCountingSimple._countVote(uint256,address,uint8,uint256,bytes) returns()": [
        [
            "NOT",
            [
                "hasVoted@_proposalVotes@proposalId@account",
                "hasVoted@proposalVote@account"
            ],
            "#Medium#ERROR_MSG:GovernorVotingSimple: vote already cast"
        ],
        [
            "EQ",
            [
                "Abstain"
            ],
            [
                "support",
                "uint8_1"
            ],
            "#Low#ERROR_MSG:(GovernorVotingSimple: invalid value for enum VoteType)"
        ]
    ],
    "AccessControlEnumerable._grantRole(bytes32,address) returns()": [],
    "ERC20Votes._maxSupply() returns(uint224)": [],
    "GovernorCompMock.votingPeriod() returns(uint256)": [],
    "IAccessControl.getRoleAdmin(bytes32) returns(bytes32)": [],
    "ReinitializerMock.nestedReinitialize(uint8,uint8) returns()": [
        [
            "reinitializer"
        ],
        [
            "NOT",
            [
                "_initializing",
                "bool"
            ],
            "#Low#ERROR_MSG:Initializable: contract is already initialized"
        ],
        [
            "LT",
            [
                "_initialized",
                "uint8"
            ],
            [
                "uint8_1",
                "i",
                "uint8_2",
                "j",
                "version"
            ],
            "#Low#ERROR_MSG:Initializable: contract is already initialized"
        ],
        [
            "onlyInitializing"
        ],
        [
            "_initializing",
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "AccessControlDefaultAdminRules.slitherConstructorConstantVariables() returns()": [],
    "CrossChainEnabledArbitrumL2Mock.slitherConstructorVariables() returns()": [],
    "GovernorCompatibilityBravoMock.quorum(uint256) returns(uint256)": [],
    "ReinitializerMock.chainReinitialize(uint8,uint8) returns()": [
        [
            "reinitializer"
        ],
        [
            "NOT",
            [
                "_initializing",
                "bool"
            ],
            "#Low#ERROR_MSG:Initializable: contract is already initialized"
        ],
        [
            "LT",
            [
                "_initialized",
                "uint8"
            ],
            [
                "j",
                "uint8_2",
                "uint8_1",
                "i",
                "version"
            ],
            "#Low#ERROR_MSG:Initializable: contract is already initialized"
        ],
        [
            "onlyInitializing"
        ],
        [
            "_initializing",
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "CrossChainEnabledAMB._isCrossChain() returns(bool)": [],
    "ERC4626Fees._entryFeeBasePoint() returns(uint256)": [],
    "TimelockController.hashOperation(address,uint256,bytes,bytes32,bytes32) returns(bytes32)": [],
    "Votes._push(Checkpoints.Trace224,function(uint224,uint224) returns(uint224),uint224) returns(uint224,uint224)": [
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ],
        [
            "LTE",
            [
                "_key@_unsafeAccess(self,pos - 1)",
                "_key@last"
            ],
            [
                "key"
            ],
            "#Medium#ERROR_MSG:Checkpoint: decreasing keys"
        ]
    ],
    "CrossChainEnabledAMB._crossChainSender() returns(address)": [
        [
            "onlyCrossChain"
        ],
        [
            "NOT",
            [
                "isCrossChain(bridge)",
                [
                    "EQ",
                    [
                        "msgsender"
                    ],
                    [
                        "_bridge",
                        "bridge"
                    ]
                ]
            ],
            "#High#ERROR_MSG:NotCrossChainCall()()"
        ]
    ],
    "Governor.castVoteWithReasonAndParamsBySig(uint256,uint8,string,bytes,uint8,bytes32,bytes32) returns(uint256)": [
        [
            "EQ",
            [
                "state(proposalId)"
            ],
            [
                "Active@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: vote not currently active"
        ],
        [
            "EQ",
            [
                "0"
            ],
            [
                "proposalSnapshot(proposalId)",
                "REF_1872",
                "voteStart@proposal",
                "voteStart@_proposals@proposalId",
                "snapshot"
            ],
            "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
        ],
        [
            "EQ",
            [
                "InvalidSignature@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature)"
        ],
        [
            "EQ",
            [
                "InvalidSignatureLength@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature length)"
        ],
        [
            "EQ",
            [
                "InvalidSignatureS@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature 's' value)"
        ]
    ],
    "TimelockController.hashOperationBatch(address[],uint256[],bytes[],bytes32,bytes32) returns(bytes32)": [],
    "Pausable.paused() returns(bool)": [],
    "CrossChainEnabledArbitrumL1.constructor(address) returns()": [],
    "ERC4626Fees._exitFeeBasePoint() returns(uint256)": [],
    "TimelockController.schedule(address,uint256,bytes,bytes32,bytes32,uint256) returns()": [
        [
            [
                "onlyRole",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ],
        [
            "NOT",
            [
                "isOperation(id)",
                [
                    "GT",
                    [
                        "getTimestamp(id)",
                        [
                            "_timestamps@id"
                        ]
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:TimelockController: operation already scheduled"
        ],
        [
            "GTE",
            [
                "delay",
                "uint256_2"
            ],
            [
                "getMinDelay()",
                [
                    "_minDelay"
                ]
            ],
            "#Medium#ERROR_MSG:TimelockController: insufficient delay"
        ]
    ],
    "ERC4626Fees._exitFeeRecipient() returns(address)": [],
    "TimelockController.scheduleBatch(address[],uint256[],bytes[],bytes32,bytes32,uint256) returns()": [
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@values"
            ],
            "#Medium#ERROR_MSG:TimelockController: length mismatch"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@payloads"
            ],
            "#Medium#ERROR_MSG:TimelockController: length mismatch"
        ],
        [
            [
                "onlyRole",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ],
        [
            "NOT",
            [
                "isOperation(id)",
                [
                    "GT",
                    [
                        "getTimestamp(id)",
                        [
                            "_timestamps@id"
                        ]
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:TimelockController: operation already scheduled"
        ],
        [
            "GTE",
            [
                "delay",
                "uint256_1"
            ],
            [
                "getMinDelay()",
                [
                    "_minDelay"
                ]
            ],
            "#Medium#ERROR_MSG:TimelockController: insufficient delay"
        ]
    ],
    "CrossChainEnabledArbitrumL1._isCrossChain() returns(bool)": [],
    "ERC4626Fees._feeOnRaw(uint256,uint256) returns(uint256)": [
        [
            "GT",
            [
                "denominator",
                "100000"
            ],
            [
                "prod1"
            ],
            "#Medium#ERROR_MSG:Math: mulDiv overflow"
        ]
    ],
    "ERC20Burnable.burnFrom(address,uint256) returns()": [
        [
            "NEQ",
            [
                "owner",
                "from",
                "account",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: burn from the zero address"
        ],
        [
            "GTE",
            [
                "_balances@from",
                "_balances@account",
                "_balances@owner",
                "accountBalance"
            ],
            [
                "amount",
                "uint256_1"
            ],
            "#Medium#ERROR_MSG:ERC20: burn amount exceeds balance"
        ],
        [
            "GTE",
            [
                "allowance(owner,spender)",
                "_allowances@owner@spender",
                "_allowances@account@spender",
                "_allowances@from@spender",
                "_allowances@address_1@spender",
                "allowance(owner,spender)",
                "allowance(account,spender)",
                "allowance(from,spender)",
                "allowance(address_1,spender)",
                "currentAllowance"
            ],
            [
                "amount",
                "uint256_1"
            ],
            "#High#ERROR_MSG:ERC20: insufficient allowance"
        ],
        [
            "NEQ",
            [
                "owner",
                "from",
                "account",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve from the zero address"
        ],
        [
            "NEQ",
            [
                "spender"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve to the zero address"
        ]
    ],
    "TimelockController._schedule(bytes32,uint256) returns()": [
        [
            "NOT",
            [
                "isOperation(id)",
                [
                    "GT",
                    [
                        "getTimestamp(id)",
                        [
                            "_timestamps@id"
                        ]
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:TimelockController: operation already scheduled"
        ],
        [
            "GTE",
            [
                "uint256_1",
                "delay"
            ],
            [
                "getMinDelay()",
                [
                    "_minDelay"
                ]
            ],
            "#Medium#ERROR_MSG:TimelockController: insufficient delay"
        ]
    ],
    "CrossChainEnabledArbitrumL1._crossChainSender() returns(address)": [
        [
            "onlyCrossChain"
        ],
        [
            "NEQ",
            [
                "sender",
                "l2ToL1Sender()"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:LibArbitrumL1: system messages without sender"
        ],
        [
            "NOT",
            [
                "isCrossChain(bridge)",
                [
                    "EQ",
                    [
                        "msgsender"
                    ],
                    [
                        "bridge",
                        "_bridge"
                    ]
                ]
            ],
            "#High#ERROR_MSG:NotCrossChainCall()()"
        ]
    ],
    "ERC2981._deleteDefaultRoyalty() returns()": [],
    "ERC4626Fees._feeOnTotal(uint256,uint256) returns(uint256)": [
        [
            "GT",
            [
                "denominator"
            ],
            [
                "prod1"
            ],
            "#Medium#ERROR_MSG:Math: mulDiv overflow"
        ]
    ],
    "ERC20Capped.constructor(uint256) returns()": [],
    "TimelockController.cancel(bytes32) returns()": [
        [
            [
                "isOperationPending(id)",
                [
                    "GT",
                    [
                        "getTimestamp(id)",
                        [
                            "_timestamps@id"
                        ]
                    ],
                    [
                        "_DONE_TIMESTAMP",
                        "uint256(1)",
                        "uint256"
                    ]
                ]
            ],
            "#High#ERROR_MSG:TimelockController: operation cannot be cancelled"
        ],
        [
            [
                "onlyRole",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ]
    ],
    "CrossChainEnabledArbitrumL2._isCrossChain() returns(bool)": [],
    "MyGovernor.constructor(IVotes,TimelockController) returns()": [],
    "CrossChainEnabledArbitrumL2._crossChainSender() returns(address)": [
        [
            "onlyCrossChain"
        ],
        [
            "NOT",
            [
                "isCrossChain(arbsys)",
                "wasMyCallersAddressAliased()"
            ],
            "#High#ERROR_MSG:NotCrossChainCall()()"
        ]
    ],
    "TimelockController.execute(address,uint256,bytes,bytes32,bytes32) returns()": [
        [
            "onlyRoleOrOpenRole"
        ],
        [
            [
                "isOperationReady(id)"
            ],
            "#Medium#ERROR_MSG:TimelockController: operation is not ready"
        ],
        [
            [
                [
                    "EQ",
                    [
                        "predecessor",
                        "bytes32_1",
                        "id",
                        "hashOperation(target,value,payload,predecessor,salt)",
                        "encode(target,value,data,predecessor,salt))"
                    ],
                    [
                        "bytes32(0)"
                    ]
                ],
                [
                    "isOperationDone(predecessor)",
                    [
                        "EQ",
                        [
                            "getTimestamp(id)",
                            [
                                "_timestamps@predecessor",
                                "_timestamps@id",
                                "timestamp",
                                "_timestamps@hashOperation(target,value,payload,predecessor,salt)",
                                "_timestamps@encode(target,value,data,predecessor,salt))",
                                "getTimestamp(id)"
                            ]
                        ],
                        [
                            "_DONE_TIMESTAMP",
                            "uint256(1)",
                            "uint256"
                        ]
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:TimelockController: missing dependency"
        ],
        [
            "success",
            "#Medium#ERROR_MSG:TimelockController: underlying transaction reverted"
        ]
    ],
    "ERC20Capped.cap() returns(uint256)": [],
    "MyGovernor.votingDelay() returns(uint256)": [],
    "ERC721Votes._getVotingUnits(address) returns(uint256)": [
        [
            "NEQ",
            [
                "owner",
                "account",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: address zero is not a valid owner"
        ]
    ],
    "CrossChainEnabledOptimism.constructor(address) returns()": [],
    "TimelockController.executeBatch(address[],uint256[],bytes[],bytes32,bytes32) returns()": [
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@values"
            ],
            "#Medium#ERROR_MSG:TimelockController: length mismatch"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@payloads"
            ],
            "#Medium#ERROR_MSG:TimelockController: length mismatch"
        ],
        [
            "onlyRoleOrOpenRole"
        ],
        [
            [
                "isOperationReady(id)"
            ],
            "#Medium#ERROR_MSG:TimelockController: operation is not ready"
        ],
        [
            [
                [
                    "EQ",
                    [
                        "predecessor",
                        "hashOperationBatch(targets,values,payloads,predecessor,salt)",
                        "id",
                        "encode(targets,values,payloads,predecessor,salt))",
                        "bytes32_1"
                    ],
                    [
                        "bytes32(0)"
                    ]
                ],
                [
                    "isOperationDone(predecessor)",
                    [
                        "EQ",
                        [
                            "getTimestamp(id)",
                            [
                                "_timestamps@id",
                                "_timestamps@predecessor",
                                "_timestamps@hashOperationBatch(targets,values,payloads,predecessor,salt)",
                                "_timestamps@encode(targets,values,payloads,predecessor,salt))",
                                "timestamp",
                                "getTimestamp(id)"
                            ]
                        ],
                        [
                            "_DONE_TIMESTAMP",
                            "uint256(1)",
                            "uint256"
                        ]
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:TimelockController: missing dependency"
        ],
        [
            "success",
            "#Medium#ERROR_MSG:TimelockController: underlying transaction reverted"
        ]
    ],
    "ERC20Capped._mint(address,uint256) returns()": [
        [
            "LTE",
            [
                "ADD",
                [
                    "totalSupply()"
                ],
                [
                    "amount",
                    "uint256_1"
                ]
            ],
            [
                "cap()",
                [
                    "_cap"
                ]
            ],
            "#Medium#ERROR_MSG:ERC20Capped: cap exceeded"
        ],
        [
            "NEQ",
            [
                "to",
                "address_1",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: mint to the zero address"
        ]
    ],
    "MyGovernor.votingPeriod() returns(uint256)": [],
    "TimelockController._execute(address,uint256,bytes) returns()": [
        [
            "success",
            "#Medium#ERROR_MSG:TimelockController: underlying transaction reverted"
        ]
    ],
    "ERC20FlashMint.maxFlashLoan(address) returns(uint256)": [],
    "CrossChainEnabledOptimism._isCrossChain() returns(bool)": [],
    "Governor._isValidDescriptionForProposer(address,string) returns(bool)": [],
    "MyGovernor.proposalThreshold() returns(uint256)": [],
    "ERC2981._resetTokenRoyalty(uint256) returns()": [],
    "TimelockController._beforeCall(bytes32,bytes32) returns()": [
        [
            [
                "isOperationReady(id)"
            ],
            "#Medium#ERROR_MSG:TimelockController: operation is not ready"
        ],
        [
            [
                [
                    "EQ",
                    [
                        "predecessor",
                        "bytes32_2",
                        "id",
                        "bytes32_1"
                    ],
                    [
                        "bytes32(0)"
                    ]
                ],
                [
                    "isOperationDone(predecessor)",
                    [
                        "EQ",
                        [
                            "getTimestamp(id)",
                            [
                                "_timestamps@id",
                                "timestamp",
                                "_timestamps@predecessor",
                                "getTimestamp(id)"
                            ]
                        ],
                        [
                            "_DONE_TIMESTAMP",
                            "uint256(1)",
                            "uint256"
                        ]
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:TimelockController: missing dependency"
        ]
    ],
    "GovernorVotes._getVotes(address,uint256,bytes) returns(uint256)": [],
    "CrossChainEnabledOptimism._crossChainSender() returns(address)": [
        [
            "onlyCrossChain"
        ],
        [
            "NOT",
            [
                "isCrossChain(messenger)",
                [
                    "EQ",
                    [
                        "msgsender"
                    ],
                    [
                        "_messenger",
                        "messenger"
                    ]
                ]
            ],
            "#High#ERROR_MSG:NotCrossChainCall()()"
        ]
    ],
    "MyGovernor.state(uint256) returns(IGovernor.ProposalState)": [],
    "ERC777Mock.slitherConstructorConstantVariables() returns()": [],
    "Governor._afterExecute(uint256,address[],uint256[],bytes[],bytes32) returns()": [],
    "ERC20FlashMint.flashFee(address,uint256) returns(uint256)": [
        [
            "EQ",
            [
                "token",
                "address_1",
                "uint256_1",
                "amount"
            ],
            [
                "address(this)"
            ],
            "#Low#ERROR_MSG:ERC20FlashMint: wrong token"
        ]
    ],
    "GovernorTimelockControlMock.slitherConstructorConstantVariables() returns()": [],
    "TimelockController._afterCall(bytes32) returns()": [
        [
            [
                "isOperationReady(id)"
            ],
            "#Medium#ERROR_MSG:TimelockController: operation is not ready"
        ]
    ],
    "Votes._subtract(uint224,uint224) returns(uint224)": [],
    "TimelockController.onlyRoleOrOpenRole(bytes32) returns()": [],
    "ERC20FlashMint._flashFee(address,uint256) returns(uint256)": [],
    "MyGovernor.propose(address[],uint256[],bytes[],string) returns(uint256)": [
        [
            [
                "_isValidDescriptionForProposer(proposer,description)"
            ],
            "#Medium#ERROR_MSG:Governor: proposer restricted"
        ],
        [
            "GTE",
            [
                "getVotes(proposer,currentTimepoint - 1)",
                "_getVotes(account,timepoint,_defaultParams())"
            ],
            [
                "proposalThreshold()",
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: proposer votes below proposal threshold"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@values"
            ],
            "#Medium#ERROR_MSG:Governor: invalid proposal length"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@calldatas"
            ],
            "#Medium#ERROR_MSG:Governor: invalid proposal length"
        ],
        [
            "GT",
            [
                "length@targets"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: empty proposal"
        ],
        [
            "EQ",
            [
                "voteStart@_proposals@hashProposal(targets,values,calldatas,keccak256(bytes)(bytes(description)))",
                "voteStart@_proposals@encode(targets,values,calldatas,descriptionHash)))",
                "voteStart@_proposals@proposalId"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: proposal already exists"
        ],
        [
            "LTE",
            [
                "value",
                "snapshot",
                "deadline",
                "snapshot + votingPeriod()",
                "currentTimepoint + votingDelay()"
            ],
            [
                "max@type()(uint64)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 64 bits"
        ]
    ],
    "ERC20Votes.slitherConstructorConstantVariables() returns()": [],
    "TimelockController.updateDelay(uint256) returns()": [
        [
            "EQ",
            [
                "msgsender"
            ],
            [
                "address(this)"
            ],
            "#Medium#ERROR_MSG:TimelockController: caller must be timelock"
        ]
    ],
    "NonUpgradeableMock.increment() returns()": [],
    "ERC721ConsecutiveMock._mint(address,uint256) returns()": [
        [
            [
                "isContract(address(this))"
            ],
            "#Medium#ERROR_MSG:ERC721Consecutive: can't mint during construction"
        ],
        [
            "NEQ",
            [
                "to",
                "address_1",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: mint to the zero address"
        ],
        [
            "NOT",
            [
                "_exists(tokenId)",
                [
                    "NEQ",
                    [
                        "_ownerOf(tokenId)"
                    ],
                    [
                        "address(0)"
                    ]
                ]
            ],
            "#Low#ERROR_MSG:ERC721: token already minted"
        ]
    ],
    "MyGovernor3.state(uint256) returns(IGovernor.ProposalState)": [],
    "ERC20ExcessDecimalsMock.decimals() returns(uint256)": [],
    "ERC721ConsecutiveMock._beforeTokenTransfer(address,address,uint256,uint256) returns()": [
        [
            "NOT",
            [
                "paused()",
                [
                    "_paused"
                ]
            ],
            "#High#ERROR_MSG:ERC721Pausable: token transfer while paused"
        ]
    ],
    "MyGovernor3.propose(address[],uint256[],bytes[],string) returns(uint256)": [
        [
            [
                "_isValidDescriptionForProposer(proposer,description)"
            ],
            "#High#ERROR_MSG:Governor: proposer restricted"
        ],
        [
            "GTE",
            [
                "getVotes(proposer,currentTimepoint - 1)",
                "_getVotes(account,timepoint,_defaultParams())"
            ],
            [
                "proposalThreshold()",
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: proposer votes below proposal threshold"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@values"
            ],
            "#Medium#ERROR_MSG:Governor: invalid proposal length"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@calldatas"
            ],
            "#Medium#ERROR_MSG:Governor: invalid proposal length"
        ],
        [
            "GT",
            [
                "length@targets"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: empty proposal"
        ],
        [
            "EQ",
            [
                "voteStart@_proposals@hashProposal(targets,values,calldatas,keccak256(bytes)(bytes(description)))",
                "voteStart@_proposals@encode(targets,values,calldatas,descriptionHash)))",
                "voteStart@_proposals@proposalId"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: proposal already exists"
        ],
        [
            "LTE",
            [
                "value",
                "snapshot",
                "deadline",
                "snapshot + votingPeriod()",
                "currentTimepoint + votingDelay()"
            ],
            [
                "max@type()(uint64)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 64 bits"
        ]
    ],
    "ERC721ConsecutiveMock._afterTokenTransfer(address,address,uint256,uint256) returns()": [
        [
            "LTE",
            [
                "value",
                "uint256_2",
                "batchSize",
                "amount"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ],
        [
            "LTE",
            [
                "_key@_unsafeAccess(self,pos - 1)",
                "_key@last"
            ],
            [
                "key"
            ],
            "#Medium#ERROR_MSG:Checkpoint: decreasing keys"
        ]
    ],
    "MyGovernor3.cancel(address[],uint256[],bytes[],bytes32) returns(uint256)": [
        [
            [
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "proposer@_proposalDetails@proposalId",
                        "proposer@_proposalDetails@hashProposal(targets,values,calldatas,descriptionHash)",
                        "account",
                        "proposer@_proposalDetails@encode(targets,values,calldatas,descriptionHash)))",
                        "proposer",
                        "proposer@details"
                    ]
                ],
                [
                    "LT",
                    [
                        "getVotes(proposer,clock() - 1)",
                        "_getVotes(account,timepoint,_defaultParams())"
                    ],
                    [
                        "proposalThreshold()",
                        "1000e18"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:GovernorBravo: proposer above threshold"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Canceled@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Expired@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Executed@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ]
    ],
    "ERC721ConsecutiveNoConstructorMintMock.constructor(string,string) returns()": [],
    "MyGovernor3._execute(uint256,address[],uint256[],bytes[],bytes32) returns()": [
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@values"
            ],
            "#Medium#ERROR_MSG:TimelockController: length mismatch"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@payloads"
            ],
            "#Medium#ERROR_MSG:TimelockController: length mismatch"
        ],
        [
            "onlyRoleOrOpenRole"
        ],
        [
            [
                "isOperationReady(id)"
            ],
            "#Medium#ERROR_MSG:TimelockController: operation is not ready"
        ],
        [
            [
                [
                    "EQ",
                    [
                        "predecessor",
                        "hashOperationBatch(targets,values,payloads,predecessor,salt)",
                        "0",
                        "id",
                        "encode(targets,values,payloads,predecessor,salt))"
                    ],
                    [
                        "bytes32(0)"
                    ]
                ],
                [
                    "isOperationDone(predecessor)",
                    [
                        "EQ",
                        [
                            "getTimestamp(id)",
                            [
                                "_timestamps@id",
                                "_timestamps@0",
                                "_timestamps@predecessor",
                                "_timestamps@hashOperationBatch(targets,values,payloads,predecessor,salt)",
                                "_timestamps@encode(targets,values,payloads,predecessor,salt))",
                                "timestamp",
                                "getTimestamp(id)"
                            ]
                        ],
                        [
                            "_DONE_TIMESTAMP",
                            "uint256(1)",
                            "uint256"
                        ]
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:TimelockController: missing dependency"
        ],
        [
            "success",
            "#Medium#ERROR_MSG:TimelockController: underlying transaction reverted"
        ]
    ],
    "ERC721URIStorageMock._baseURI() returns(string)": [],
    "MyGovernor3._cancel(address[],uint256[],bytes[],bytes32) returns(uint256)": [
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Canceled@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Expired@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Executed@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            [
                "isOperationPending(id)",
                [
                    "GT",
                    [
                        "getTimestamp(id)",
                        [
                            "_timestamps@id"
                        ]
                    ],
                    [
                        "_DONE_TIMESTAMP",
                        "uint256(1)",
                        "uint256"
                    ]
                ]
            ],
            "#High#ERROR_MSG:TimelockController: operation cannot be cancelled"
        ],
        [
            [
                "onlyRole",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ]
    ],
    "ERC721URIStorageMock.setBaseURI(string) returns()": [],
    "MyGovernor3._executor() returns(address)": [],
    "ERC721._approve(address,uint256) returns()": [
        [
            "NEQ",
            [
                "_ownerOf(tokenId)",
                "_owners@tokenId",
                "owner"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: invalid token ID"
        ]
    ],
    "ERC721VotesTimestampMock.clock() returns(uint48)": [
        [
            "LTE",
            [
                "value",
                "timestamp"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "MyGovernor3.supportsInterface(bytes4) returns(bool)": [],
    "ERC721VotesTimestampMock.CLOCK_MODE() returns(string)": [],
    "ERC1155Holder.onERC1155Received(address,address,uint256,uint256,bytes) returns(bytes4)": [],
    "ERC1155.setApprovalForAll(address,bool) returns()": [
        [
            "NEQ",
            [
                "owner",
                "_msgSender()",
                "msgsender"
            ],
            [
                "operator",
                "address_1"
            ],
            "#Low#ERROR_MSG:ERC1155: setting approval status for self"
        ]
    ],
    "ERC1155Holder.onERC1155BatchReceived(address,address,uint256[],uint256[],bytes) returns(bytes4)": [],
    "ERC1967Upgrade._setAdmin(address) returns()": [
        [
            "NEQ",
            [
                "newAdmin",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC1967: new admin is the zero address"
        ]
    ],
    "ERC721Royalty.supportsInterface(bytes4) returns(bool)": [],
    "ERC777.totalSupply() returns(uint256)": [],
    "ERC20PresetMinterPauser.slitherConstructorConstantVariables() returns()": [],
    "ERC721Royalty._burn(uint256) returns()": [
        [
            "NEQ",
            [
                "_ownerOf(tokenId)",
                "_owners@tokenId",
                "_owners@firstTokenId",
                "owner"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: invalid token ID"
        ]
    ],
    "MyGovernor2.slitherConstructorConstantVariables() returns()": [],
    "MinimalForwarder.constructor() returns()": [],
    "MyGovernor1.quorum(uint256) returns(uint256)": [
        [
            "LTE",
            [
                "timepoint",
                "value",
                "uint256_1",
                "blockNumber"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ]
    ],
    "MyGovernor1.state(uint256) returns(IGovernor.ProposalState)": [],
    "MinimalForwarder.getNonce(address) returns(uint256)": [],
    "ERC4626._convertToShares(uint256,Math.Rounding) returns(uint256)": [
        [
            "GT",
            [
                "denominator"
            ],
            [
                "prod1"
            ],
            "#Medium#ERROR_MSG:Math: mulDiv overflow"
        ]
    ],
    "MyGovernor1.propose(address[],uint256[],bytes[],string) returns(uint256)": [
        [
            [
                "_isValidDescriptionForProposer(proposer,description)"
            ],
            "#High#ERROR_MSG:Governor: proposer restricted"
        ],
        [
            "GTE",
            [
                "getVotes(proposer,currentTimepoint - 1)",
                "_getVotes(account,timepoint,_defaultParams())"
            ],
            [
                "proposalThreshold()",
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: proposer votes below proposal threshold"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@values"
            ],
            "#Medium#ERROR_MSG:Governor: invalid proposal length"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@calldatas"
            ],
            "#Medium#ERROR_MSG:Governor: invalid proposal length"
        ],
        [
            "GT",
            [
                "length@targets"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: empty proposal"
        ],
        [
            "EQ",
            [
                "voteStart@_proposals@hashProposal(targets,values,calldatas,keccak256(bytes)(bytes(description)))",
                "voteStart@_proposals@encode(targets,values,calldatas,descriptionHash)))",
                "voteStart@_proposals@proposalId"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: proposal already exists"
        ],
        [
            "LTE",
            [
                "value",
                "snapshot",
                "deadline",
                "snapshot + votingPeriod()",
                "currentTimepoint + votingDelay()"
            ],
            [
                "max@type()(uint64)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 64 bits"
        ]
    ],
    "MinimalForwarder.verify(MinimalForwarder.ForwardRequest,bytes) returns(bool)": [
        [
            "EQ",
            [
                "InvalidSignature@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature)"
        ],
        [
            "EQ",
            [
                "InvalidSignatureLength@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature length)"
        ],
        [
            "EQ",
            [
                "InvalidSignatureS@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature 's' value)"
        ]
    ],
    "MyGovernor1._execute(uint256,address[],uint256[],bytes[],bytes32) returns()": [
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@values"
            ],
            "#Medium#ERROR_MSG:TimelockController: length mismatch"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@payloads"
            ],
            "#Medium#ERROR_MSG:TimelockController: length mismatch"
        ],
        [
            "onlyRoleOrOpenRole"
        ],
        [
            [
                "isOperationReady(id)"
            ],
            "#Medium#ERROR_MSG:TimelockController: operation is not ready"
        ],
        [
            [
                [
                    "EQ",
                    [
                        "predecessor",
                        "hashOperationBatch(targets,values,payloads,predecessor,salt)",
                        "0",
                        "id",
                        "encode(targets,values,payloads,predecessor,salt))"
                    ],
                    [
                        "bytes32(0)"
                    ]
                ],
                [
                    "isOperationDone(predecessor)",
                    [
                        "EQ",
                        [
                            "getTimestamp(id)",
                            [
                                "_timestamps@id",
                                "_timestamps@0",
                                "_timestamps@predecessor",
                                "_timestamps@hashOperationBatch(targets,values,payloads,predecessor,salt)",
                                "_timestamps@encode(targets,values,payloads,predecessor,salt))",
                                "timestamp",
                                "getTimestamp(id)"
                            ]
                        ],
                        [
                            "_DONE_TIMESTAMP",
                            "uint256(1)",
                            "uint256"
                        ]
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:TimelockController: missing dependency"
        ],
        [
            "success",
            "#Medium#ERROR_MSG:TimelockController: underlying transaction reverted"
        ]
    ],
    "MinimalForwarder.execute(MinimalForwarder.ForwardRequest,bytes) returns(bool,bytes)": [
        [
            [
                "verify(req,signature)"
            ],
            "#Medium#ERROR_MSG:MinimalForwarder: signature does not match request"
        ],
        [
            "EQ",
            [
                "InvalidSignature@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature)"
        ],
        [
            "EQ",
            [
                "InvalidSignatureLength@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature length)"
        ],
        [
            "EQ",
            [
                "InvalidSignatureS@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature 's' value)"
        ]
    ],
    "MyGovernor1._cancel(address[],uint256[],bytes[],bytes32) returns(uint256)": [
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Canceled@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Expired@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Executed@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            [
                "isOperationPending(id)",
                [
                    "GT",
                    [
                        "getTimestamp(id)",
                        [
                            "_timestamps@id"
                        ]
                    ],
                    [
                        "_DONE_TIMESTAMP",
                        "uint256(1)",
                        "uint256"
                    ]
                ]
            ],
            "#High#ERROR_MSG:TimelockController: operation cannot be cancelled"
        ],
        [
            [
                "onlyRole",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ]
    ],
    "ContextMock.msgSender() returns()": [],
    "MyGovernor1._executor() returns(address)": [],
    "Ownable.owner() returns(address)": [],
    "ERC20FlashMint._flashFeeReceiver() returns(address)": [],
    "MyGovernor1.supportsInterface(bytes4) returns(bool)": [],
    "ContextMock.msgDataShort() returns()": [],
    "ERC1155._safeBatchTransferFrom(address,address,uint256[],uint256[],bytes) returns()": [
        [
            "EQ",
            [
                "length@ids"
            ],
            [
                "length@amounts"
            ],
            "#Low#ERROR_MSG:ERC1155: ids and amounts length mismatch"
        ],
        [
            "NEQ",
            [
                "to",
                "account",
                "address_2"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC1155: transfer to the zero address"
        ],
        [
            "GTE",
            [
                "_balances@ids@i@from",
                "_balances@id@from",
                "_balances@ids",
                "fromBalance"
            ],
            [
                "amounts",
                "amount",
                "values",
                "amounts@i"
            ],
            "#Medium#ERROR_MSG:ERC1155: insufficient balance for transfer"
        ],
        [
            "NEQ",
            [
                "selector@onERC1155BatchReceived@IERC1155Receiver"
            ],
            [
                "response"
            ],
            "#High#ERROR_MSG:ERC1155: ERC1155Receiver rejected tokens"
        ]
    ],
    "MyGovernor2.constructor(IVotes,TimelockController) returns()": [],
    "LibArbitrumL2.slitherConstructorConstantVariables() returns()": [],
    "EIP712.slitherConstructorConstantVariables() returns()": [],
    "EIP712Verifier.verify(bytes,address,address,string) returns()": [
        [
            "EQ",
            [
                "recoveredSigner",
                "recover(digest,signature)"
            ],
            [
                "signer",
                "address_1"
            ],
            "#Low#ERROR_MSG:None"
        ]
    ],
    "GovernorTimelockCompound.constructor(ICompoundTimelock) returns()": [],
    "MyGovernor2.votingDelay() returns(uint256)": [],
    "ERC1271WalletMock.constructor(address) returns()": [],
    "ERC777.operatorBurn(address,uint256,bytes,bytes) returns()": [
        [
            [
                "isOperatorFor(_msgSender(),account)",
                [
                    [
                        [
                            [
                                [
                                    "EQ",
                                    [
                                        "operator"
                                    ],
                                    [
                                        "account",
                                        "address_1",
                                        "from",
                                        "tokenHolder"
                                    ]
                                ],
                                [
                                    [
                                        [
                                            "_defaultOperators@operator"
                                        ],
                                        [
                                            "NOT",
                                            [
                                                "_revokedDefaultOperators@tokenHolder@operator"
                                            ]
                                        ]
                                    ]
                                ]
                            ]
                        ],
                        [
                            "_operators@tokenHolder@operator"
                        ]
                    ]
                ]
            ],
            "#High#ERROR_MSG:ERC777: caller is not an operator for holder"
        ],
        [
            "NEQ",
            [
                "account",
                "address_1",
                "from",
                "tokenHolder"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC777: burn from the zero address"
        ],
        [
            "GTE",
            [
                "_balances@account",
                "fromBalance",
                "_balances@tokenHolder",
                "_balances@from"
            ],
            [
                "amount",
                "uint256_1"
            ],
            "#Medium#ERROR_MSG:ERC777: burn amount exceeds balance"
        ]
    ],
    "MyGovernor2.votingPeriod() returns(uint256)": [],
    "ERC1271WalletMock.isValidSignature(bytes32,bytes) returns(bytes4)": [],
    "MyGovernor2.proposalThreshold() returns(uint256)": [],
    "TransparentUpgradeableProxy.slitherConstructorConstantVariables() returns()": [],
    "GovernorMock.slitherConstructorConstantVariables() returns()": [],
    "Votes.slitherConstructorConstantVariables() returns()": [],
    "ERC165ReturnBombMock.supportsInterface(bytes4) returns(bool)": [],
    "ERC20Permit.permit(address,address,uint256,uint256,uint8,bytes32,bytes32) returns()": [
        [
            "LTE",
            [
                "timestamp"
            ],
            [
                "uint256_2",
                "deadline"
            ],
            "#Medium#ERROR_MSG:ERC20Permit: expired deadline"
        ],
        [
            "EQ",
            [
                "recover(hash,v,r,s)",
                "signer"
            ],
            [
                "owner",
                "address_1"
            ],
            "#High#ERROR_MSG:ERC20Permit: invalid signature"
        ],
        [
            "NEQ",
            [
                "owner",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve from the zero address"
        ],
        [
            "NEQ",
            [
                "spender",
                "address_2"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve to the zero address"
        ],
        [
            "EQ",
            [
                "InvalidSignature@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature)"
        ],
        [
            "EQ",
            [
                "InvalidSignatureLength@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature length)"
        ],
        [
            "EQ",
            [
                "InvalidSignatureS@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature 's' value)"
        ]
    ],
    "ERC20Reentrant._afterTokenTransfer(address,address,uint256) returns()": [
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "ERC777.transferFrom(address,address,uint256) returns(bool)": [
        [
            "GTE",
            [
                "allowance(owner,spender)",
                "_allowances@holder@spender",
                "_allowances@holder@_msgSender()",
                "currentAllowance",
                "_allowances@holder@msgsender"
            ],
            [
                "amount",
                "uint256_1"
            ],
            "#High#ERROR_MSG:ERC777: insufficient allowance"
        ],
        [
            "NEQ",
            [
                "from",
                "to",
                "holder",
                "account",
                "address_1",
                "owner",
                "recipient",
                "address_2"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC777: transfer from the zero address"
        ],
        [
            "NEQ",
            [
                "from",
                "to",
                "holder",
                "account",
                "address_1",
                "owner",
                "recipient",
                "address_2"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC777: transfer to the zero address"
        ],
        [
            "NEQ",
            [
                "from",
                "to",
                "holder",
                "account",
                "address_1",
                "owner",
                "recipient",
                "address_2"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC777: approve from the zero address"
        ],
        [
            "NEQ",
            [
                "spender",
                "_msgSender()",
                "msgsender"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC777: approve to the zero address"
        ],
        [
            "NOT",
            [
                "isContract()"
            ],
            "#Medium#ERROR_MSG:ERC777: token recipient contract has no implementer for ERC777TokensRecipient"
        ],
        [
            "GTE",
            [
                "_balances@from",
                "_balances@to",
                "_balances@account",
                "_balances@holder",
                "_balances@owner",
                "fromBalance",
                "_balances@recipient"
            ],
            [
                "amount",
                "uint256_1"
            ],
            "#Medium#ERROR_MSG:ERC777: transfer amount exceeds balance"
        ]
    ],
    "ProxyAdmin.upgradeAndCall(ITransparentUpgradeableProxy,address,bytes) returns()": [
        [
            [
                "onlyOwner",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ]
    ],
    "AccessControlDefaultAdminRules._acceptDefaultAdminTransfer() returns()": [
        [
            "_isScheduleSet(schedule)",
            [
                "NEQ",
                [
                    "schedule"
                ],
                [
                    "0"
                ]
            ],
            "#Medium#ERROR_MSG:AccessControl: transfer delay not passed"
        ],
        [
            "_hasSchedulePassed(schedule)",
            [
                "LT",
                [
                    "schedule"
                ],
                [
                    "timestamp"
                ]
            ],
            "#Medium#ERROR_MSG:AccessControl: transfer delay not passed"
        ],
        [
            "EQ",
            [
                "defaultAdmin()",
                [
                    "_currentDefaultAdmin"
                ]
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:AccessControl: default admin already granted"
        ]
    ],
    "ERC4626Mock.constructor(address) returns()": [],
    "ERC777._mint(address,uint256,bytes,bytes) returns()": [
        [
            "NEQ",
            [
                "to",
                "account",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC777: mint to the zero address"
        ],
        [
            "NOT",
            [
                "isContract()"
            ],
            "#Medium#ERROR_MSG:ERC777: token recipient contract has no implementer for ERC777TokensRecipient"
        ]
    ],
    "TransparentUpgradeableProxy.ifAdmin() returns()": [],
    "AccessControlDefaultAdminRules.changeDefaultAdminDelay(uint48) returns()": [
        [
            [
                "onlyRole",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ],
        [
            "LTE",
            [
                "value",
                "timestamp"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "ERC4626Mock.mint(address,uint256) returns()": [
        [
            "NEQ",
            [
                "to",
                "account",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: mint to the zero address"
        ]
    ],
    "ERC777._mint(address,uint256,bytes,bytes,bool) returns()": [
        [
            "NEQ",
            [
                "to",
                "account",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC777: mint to the zero address"
        ],
        [
            "NOT",
            [
                "isContract()"
            ],
            "#Medium#ERROR_MSG:ERC777: token recipient contract has no implementer for ERC777TokensRecipient"
        ]
    ],
    "GovernorVotesComp.clock() returns(uint48)": [
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "TransparentUpgradeableProxy.constructor(address,address,bytes) returns()": [],
    "AccessControlDefaultAdminRules._changeDefaultAdminDelay(uint48) returns()": [
        [
            "LTE",
            [
                "value",
                "timestamp"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "ERC20Votes.getPastVotes(address,uint256) returns(uint256)": [
        [
            "LT",
            [
                "timepoint",
                "uint256_1"
            ],
            [
                "clock()",
                "number)"
            ],
            "#Medium#ERROR_MSG:ERC20Votes: future lookup"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "ERC4626Mock.burn(address,uint256) returns()": [
        [
            "NEQ",
            [
                "address_1",
                "account",
                "from"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: burn from the zero address"
        ],
        [
            "GTE",
            [
                "_balances@from",
                "_balances@account",
                "accountBalance"
            ],
            [
                "amount",
                "uint256_1"
            ],
            "#Medium#ERROR_MSG:ERC20: burn amount exceeds balance"
        ]
    ],
    "UUPSUpgradeable.notDelegated() returns()": [
        [
            "EQ",
            [
                "address(this)"
            ],
            [
                "address(this)",
                "__self",
                "address"
            ],
            "#Medium#ERROR_MSG:UUPSUpgradeable: must not be called through delegatecall"
        ]
    ],
    "TransparentUpgradeableProxy._fallback() returns()": [
        [
            "NEQ",
            [
                "newAdmin",
                "target",
                "newImplementation",
                "data,(address))",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC1967: new admin is the zero address"
        ],
        [
            [
                "isContract(newImplementation)"
            ],
            "#Medium#ERROR_MSG:ERC1967: new implementation is not a contract"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ],
        [
            "EQ",
            [
                "selector@implementation@ITransparentUpgradeableProxy"
            ],
            [
                "sig",
                "selector"
            ],
            "#High#ERROR_MSG:(TransparentUpgradeableProxy: admin cannot fallback to proxy target)"
        ]
    ],
    "AccessControlDefaultAdminRules.rollbackDefaultAdminDelay() returns()": [
        [
            [
                "onlyRole",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ]
    ],
    "PausableMock.constructor() returns()": [],
    "ERC777._burn(address,uint256,bytes,bytes) returns()": [
        [
            "NEQ",
            [
                "account",
                "from",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC777: burn from the zero address"
        ],
        [
            "GTE",
            [
                "fromBalance",
                "_balances@from",
                "_balances@account"
            ],
            [
                "amount",
                "uint256_1"
            ],
            "#Medium#ERROR_MSG:ERC777: burn amount exceeds balance"
        ]
    ],
    "TransparentUpgradeableProxy._dispatchAdmin() returns(bytes)": [],
    "AccessControlDefaultAdminRules._rollbackDefaultAdminDelay() returns()": [],
    "GovernorSettings.slitherConstructorConstantVariables() returns()": [],
    "TransparentUpgradeableProxy._dispatchImplementation() returns(bytes)": [],
    "AccessControlDefaultAdminRules._delayChangeWait(uint48) returns(uint48)": [],
    "GovernorVotesComp.constructor(ERC20VotesComp) returns()": [],
    "UUPSUpgradeable.upgradeTo(address) returns()": [
        [
            [
                "onlyproxy",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ],
        [
            "NEQ",
            [
                "address(this)"
            ],
            [
                "address(this)",
                "__self",
                "address"
            ],
            "#Medium#ERROR_MSG:Function must be called through delegatecall"
        ],
        [
            "EQ",
            [
                "_getImplementation()",
                [
                    "value@getAddressSlot(_IMPLEMENTATION_SLOT)"
                ]
            ],
            [
                "address(this)",
                "__self",
                "address"
            ],
            "#Medium#ERROR_MSG:Function must be called through active proxy"
        ],
        [
            "EQ",
            [
                "slot"
            ],
            [
                "slot",
                "_IMPLEMENTATION_SLOT",
                "bytes32"
            ],
            "#Medium#ERROR_MSG:ERC1967Upgrade: unsupported proxiableUUID"
        ],
        [
            [
                "isContract(newImplementation)"
            ],
            "#Medium#ERROR_MSG:ERC1967: new implementation is not a contract"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "PausableMock.normalProcess() returns()": [
        [
            "whenNotPaused"
        ]
    ],
    "ERC777._approve(address,address,uint256) returns()": [
        [
            "NEQ",
            [
                "address_1",
                "holder"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC777: approve from the zero address"
        ],
        [
            "NEQ",
            [
                "spender",
                "address_2"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC777: approve to the zero address"
        ]
    ],
    "GovernorVotesComp._getVotes(address,uint256,bytes) returns(uint256)": [
        [
            "LT",
            [
                "timepoint",
                "blockNumber",
                "uint256_1"
            ],
            [
                "clock()",
                "number)"
            ],
            "#Medium#ERROR_MSG:ERC20Votes: future lookup"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint96)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 96 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "AccessControlDefaultAdminRules._setPendingDefaultAdmin(address,uint48) returns()": [],
    "TransparentUpgradeableProxy._dispatchChangeAdmin() returns(bytes)": [
        [
            "NEQ",
            [
                "newAdmin",
                "data,(address))"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC1967: new admin is the zero address"
        ]
    ],
    "PausableMock.drasticMeasure() returns()": [
        [
            "whenPaused"
        ]
    ],
    "ERC777._callTokensToSend(address,address,address,uint256,bytes,bytes) returns()": [],
    "AccessControlDefaultAdminRules._setPendingDelay(uint48,uint48) returns()": [],
    "TransparentUpgradeableProxy._dispatchUpgradeTo() returns(bytes)": [
        [
            [
                "isContract(newImplementation)"
            ],
            "#Medium#ERROR_MSG:ERC1967: new implementation is not a contract"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "PausableMock.pause() returns()": [
        [
            "whenNotPaused"
        ]
    ],
    "ERC777._callTokensReceived(address,address,address,uint256,bytes,bytes,bool) returns()": [
        [
            "NOT",
            [
                "isContract()"
            ],
            "#Medium#ERROR_MSG:ERC777: token recipient contract has no implementer for ERC777TokensRecipient"
        ]
    ],
    "GovernorVotesComp.CLOCK_MODE() returns(string)": [
        [
            "EQ",
            [
                "clock()",
                "number)"
            ],
            [
                "value",
                "number"
            ],
            "#Medium#ERROR_MSG:ERC20Votes: broken clock mode"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "Multicall.multicall(bytes[]) returns(bytes[])": [
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "AccessControlDefaultAdminRules._isScheduleSet(uint48) returns(bool)": [],
    "ERC721Consecutive._ownerOf(uint256) returns(address)": [],
    "TransparentUpgradeableProxy._dispatchUpgradeToAndCall() returns(bytes)": [
        [
            [
                "isContract(newImplementation)"
            ],
            "#Medium#ERROR_MSG:ERC1967: new implementation is not a contract"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "PausableMock.unpause() returns()": [
        [
            "whenPaused"
        ]
    ],
    "ERC20Votes._checkpointsLookup(ERC20Votes.Checkpoint[],uint256) returns(uint256)": [],
    "ReentrancyGuard.slitherConstructorConstantVariables() returns()": [],
    "ERC777._spendAllowance(address,address,uint256) returns()": [
        [
            "GTE",
            [
                "allowance(owner,spender)",
                "currentAllowance",
                "_allowances@holder@spender"
            ],
            [
                "uint256_1",
                "amount"
            ],
            "#High#ERROR_MSG:ERC777: insufficient allowance"
        ],
        [
            "NEQ",
            [
                "holder",
                "owner",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC777: approve from the zero address"
        ],
        [
            "NEQ",
            [
                "spender",
                "address_2"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC777: approve to the zero address"
        ]
    ],
    "AccessControlDefaultAdminRules._hasSchedulePassed(uint48) returns(bool)": [],
    "GovernorCompatibilityBravo.execute(uint256) returns()": [
        [
            [
                [
                    "EQ",
                    [
                        "state(proposalId)",
                        "currentState"
                    ],
                    [
                        "Succeeded@ProposalState"
                    ]
                ],
                [
                    "EQ",
                    [
                        "state(proposalId)",
                        "currentState"
                    ],
                    [
                        "Queued@ProposalState"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Governor: proposal not successful"
        ],
        [
            "EQ",
            [
                "0"
            ],
            [
                "proposalSnapshot(proposalId)",
                "REF_1872",
                "voteStart@_proposals@proposalId",
                "voteStart@_proposals@descriptionHash",
                "snapshot",
                "voteStart@_proposals@targets",
                "voteStart@_proposals@values",
                "voteStart@_proposals@calldatas",
                "voteStart@_proposals@hashProposal(targets,values,calldatas,descriptionHash)",
                "voteStart@_proposals@",
                "voteStart@proposal",
                "voteStart@_proposals@encode(targets,values,calldatas,descriptionHash)))"
            ],
            "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
        ]
    ],
    "UUPSUpgradeable._authorizeUpgrade(address) returns()": [],
    "VotesMock.getTotalSupply() returns(uint256)": [],
    "TransparentUpgradeableProxy._admin() returns(address)": [],
    "GovernorTimelockControl.slitherConstructorConstantVariables() returns()": [],
    "ERC777._beforeTokenTransfer(address,address,address,uint256) returns()": [],
    "ERC1155._mintBatch(address,uint256[],uint256[],bytes) returns()": [
        [
            "NEQ",
            [
                "to",
                "address_1",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC1155: mint to the zero address"
        ],
        [
            "EQ",
            [
                "length@ids"
            ],
            [
                "length@amounts"
            ],
            "#Low#ERROR_MSG:ERC1155: ids and amounts length mismatch"
        ],
        [
            "NEQ",
            [
                "selector@onERC1155BatchReceived@IERC1155Receiver"
            ],
            [
                "response"
            ],
            "#High#ERROR_MSG:(ERC1155: ERC1155Receiver rejected tokens)"
        ]
    ],
    "TransparentUpgradeableProxy._requireZeroValue() returns()": [],
    "AccessControl.slitherConstructorConstantVariables() returns()": [],
    "ERC777PresetFixedSupply.constructor(string,string,address[],uint256,address) returns()": [],
    "Strings.slitherConstructorConstantVariables() returns()": [],
    "ERC721PresetMinterPauserAutoId._beforeTokenTransfer(address,address,uint256,uint256) returns()": [
        [
            "NOT",
            [
                "paused()",
                [
                    "_paused"
                ]
            ],
            "#High#ERROR_MSG:ERC721Pausable: token transfer while paused"
        ]
    ],
    "SafeCast.toUint200(uint256) returns(uint200)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint200)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 200 bits"
        ]
    ],
    "DummyImplementation.reverts() returns()": [
        [
            "false",
            "#Low#ERROR_MSG:DummyImplementation reverted"
        ]
    ],
    "ERC4626FeesMock._entryFeeBasePoint() returns(uint256)": [],
    "ERC20Votes.getPastTotalSupply(uint256) returns(uint256)": [
        [
            "LT",
            [
                "uint256_1",
                "timepoint"
            ],
            [
                "clock()",
                "number)"
            ],
            "#Low#ERROR_MSG:ERC20Votes: future lookup"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "UUPSUpgradeableLegacyMock.slitherConstructorConstantVariables() returns()": [],
    "ERC721PresetMinterPauserAutoId.supportsInterface(bytes4) returns(bool)": [],
    "DummyImplementationV2.migrate(uint256) returns()": [],
    "ERC4626FeesMock._entryFeeRecipient() returns(address)": [],
    "UUPSUpgradeable.upgradeToAndCall(address,bytes) returns()": [
        [
            [
                "onlyproxy",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ],
        [
            "NEQ",
            [
                "address(this)"
            ],
            [
                "address(this)",
                "__self",
                "address"
            ],
            "#Medium#ERROR_MSG:Function must be called through delegatecall"
        ],
        [
            "EQ",
            [
                "_getImplementation()",
                [
                    "value@getAddressSlot(_IMPLEMENTATION_SLOT)"
                ]
            ],
            [
                "address(this)",
                "__self",
                "address"
            ],
            "#Medium#ERROR_MSG:Function must be called through active proxy"
        ],
        [
            "EQ",
            [
                "_getImplementation()",
                [
                    "value@getAddressSlot(_IMPLEMENTATION_SLOT)"
                ]
            ],
            [
                "address(this)",
                "__self",
                "address"
            ],
            "#Medium#ERROR_MSG:Function must be called through active proxy"
        ],
        [
            "EQ",
            [
                "slot"
            ],
            [
                "slot",
                "_IMPLEMENTATION_SLOT",
                "0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc",
                "bytes32"
            ],
            "#Medium#ERROR_MSG:ERC1967Upgrade: unsupported proxiableUUID"
        ],
        [
            [
                "isContract(newImplementation)"
            ],
            "#Medium#ERROR_MSG:ERC1967: new implementation is not a contract"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "DummyImplementationV2.version() returns(string)": [],
    "ERC4626FeesMock._exitFeeBasePoint() returns(uint256)": [],
    "ERC2981.supportsInterface(bytes4) returns(bool)": [],
    "ERC1271MaliciousMock.isValidSignature(bytes32,bytes) returns(bytes4)": [],
    "ERC4626FeesMock._exitFeeRecipient() returns(address)": [],
    "ERC777Mock._beforeTokenTransfer(address,address,address,uint256) returns()": [],
    "ERC2981.royaltyInfo(uint256,uint256) returns(address,uint256)": [],
    "ERC165MaliciousData.supportsInterface(bytes4) returns(bool)": [],
    "ERC777SenderRecipientMock.tokensToSend(address,address,address,uint256,bytes,bytes) returns()": [],
    "ERC2981._feeDenominator() returns(uint96)": [],
    "ERC165MissingData.supportsInterface(bytes4) returns()": [],
    "ERC20VotesLegacyMock.slitherConstructorConstantVariables() returns()": [],
    "ERC2981._setDefaultRoyalty(address,uint96) returns()": [
        [
            "LTE",
            [
                "uint96_1",
                "feeNumerator"
            ],
            [
                "_feeDenominator()",
                "10000"
            ],
            "#Medium#ERROR_MSG:ERC2981: royalty fee will exceed salePrice"
        ],
        [
            "NEQ",
            [
                "receiver",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC2981: invalid receiver"
        ]
    ],
    "ERC3156FlashBorrowerMock.constructor(bool,bool) returns()": [],
    "TimelockController.slitherConstructorConstantVariables() returns()": [],
    "ERC777SenderRecipientMock.tokensReceived(address,address,address,uint256,bytes,bytes) returns()": [],
    "ERC2981._setTokenRoyalty(uint256,address,uint96) returns()": [
        [
            "LTE",
            [
                "feeNumerator",
                "uint96_1"
            ],
            [
                "_feeDenominator()",
                "10000"
            ],
            "#Medium#ERROR_MSG:ERC2981: royalty fee will exceed salePrice"
        ],
        [
            "NEQ",
            [
                "receiver",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC2981: Invalid parameters"
        ]
    ],
    "ERC3156FlashBorrowerMock.onFlashLoan(address,address,uint256,uint256,bytes) returns(bytes32)": [
        [
            "EQ",
            [
                "msgsender"
            ],
            [
                "target",
                "spender",
                "token",
                "address_2",
                "account"
            ],
            "#Low#ERROR_MSG:None"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "ERC777SenderRecipientMock.senderFor(address) returns()": [],
    "EtherReceiverMock.setAcceptEther(bool) returns()": [],
    "ERC777SenderRecipientMock.registerSender(address) returns()": [],
    "ERC1155.safeTransferFrom(address,address,uint256,uint256,bytes) returns()": [
        [
            [
                [
                    "EQ",
                    [
                        "from",
                        "address_1",
                        "account"
                    ],
                    [
                        "_msgSender()",
                        "operator",
                        "msgsender"
                    ]
                ],
                [
                    "isApprovedForAll(from,_msgSender())",
                    [
                        "_operatorApprovals@account@operator"
                    ]
                ]
            ],
            "#High#ERROR_MSG:ERC1155: caller is not token owner or approved"
        ],
        [
            "NEQ",
            [
                "to",
                "address_2",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC1155: transfer to the zero address"
        ],
        [
            "GTE",
            [
                "fromBalance",
                "_balances@id",
                "_balances@id@from",
                "_balances@element",
                "_balances@id@account"
            ],
            [
                "amount",
                "uint256_2",
                "element",
                "value"
            ],
            "#Medium#ERROR_MSG:ERC1155: insufficient balance for transfer"
        ],
        [
            "NEQ",
            [
                "selector@onERC1155Received@IERC1155Receiver"
            ],
            [
                "response"
            ],
            "#Medium#ERROR_MSG:(ERC1155: ERC1155Receiver rejected tokens)"
        ]
    ],
    "EtherReceiverMock.receive() returns()": [],
    "ERC777SenderRecipientMock.recipientFor(address) returns()": [],
    "ConditionalEscrow.withdraw(address) returns()": [
        [
            [
                "withdrawalAllowed(payee)",
                [
                    "_allowed@payee"
                ]
            ],
            "#Medium#ERROR_MSG:ConditionalEscrow: payee is not allowed to withdraw"
        ],
        [
            [
                "onlyOwner",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "_deposits@payee",
                "payment",
                "amount",
                "_deposits@recipient"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance"
        ],
        [
            "success",
            "#Medium#ERROR_MSG:Address: unable to send value, recipient may have reverted"
        ]
    ],
    "Math.log2(uint256) returns(uint256)": [],
    "EnumerableMap.at(EnumerableMap.AddressToUintMap,uint256) returns(address,uint256)": [],
    "AccessControlCrossChain._checkRole(bytes32) returns()": [
        [
            "EQ",
            [
                "Strings.toHexString(uint256,uint256).value"
            ],
            [
                "0"
            ],
            "#Meidum#ERROR_MSG:Strings: hex length insufficient"
        ],
        [
            "NOT",
            [
                "hasRole(role,account)",
                [
                    "REF_605",
                    "members@_roles@role@account"
                ]
            ],
            "#High#ERROR_MSG:(string(abi.encodePacked(AccessControl: account ,Strings.toHexString(account), is missing role ,Strings.toHexString(uint256(role),32))))"
        ]
    ],
    "EnumerableSet.contains(EnumerableSet.UintSet,uint256) returns(bool)": [],
    "SafeCast.toUint8(uint256) returns(uint8)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint8)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 8 bits"
        ]
    ],
    "ECDSA.recover(bytes32,bytes) returns(address)": [
        [
            "EQ",
            [
                "InvalidSignature@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature)"
        ],
        [
            "EQ",
            [
                "InvalidSignatureLength@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature length)"
        ],
        [
            "EQ",
            [
                "InvalidSignatureS@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature 's' value)"
        ]
    ],
    "ERC777.constructor(string,string,address[]) returns()": [],
    "Math.log2(uint256,Math.Rounding) returns(uint256)": [],
    "EnumerableMap.tryGet(EnumerableMap.AddressToUintMap,address) returns(bool,uint256)": [],
    "EnumerableSet.length(EnumerableSet.UintSet) returns(uint256)": [],
    "SafeCast.toUint256(int256) returns(uint256)": [
        [
            "GTE",
            [
                "int256_1",
                "value"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:SafeCast: value must be positive"
        ]
    ],
    "Votes.getPastTotalSupply(uint256) returns(uint256)": [
        [
            "LT",
            [
                "value",
                "uint256_1",
                "timepoint"
            ],
            [
                "clock()",
                "timestamp)"
            ],
            "#Medium#ERROR_MSG:Votes: future lookup"
        ],
        [
            "LTE",
            [
                "value",
                "uint256_1",
                "timepoint"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "ECDSA.tryRecover(bytes32,bytes32,bytes32) returns(address,ECDSA.RecoverError)": [],
    "EnumerableMap.get(EnumerableMap.AddressToUintMap,address) returns(uint256)": [
        [
            [
                [
                    "NEQ",
                    [
                        "value",
                        "_values@map",
                        "_values@map@value",
                        "_values@map@key"
                    ],
                    [
                        "0"
                    ]
                ],
                [
                    "contains(map,key)",
                    "contains(key)"
                ]
            ],
            "#Medium#ERROR_MSG:EnumerableMap: nonexistent key"
        ]
    ],
    "Math.log10(uint256) returns(uint256)": [],
    "EnumerableSet.at(EnumerableSet.UintSet,uint256) returns(uint256)": [],
    "SafeCast.toInt248(int256) returns(int248)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "int256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 248 bits"
        ]
    ],
    "AccessControlDefaultAdminRules.constructor(uint48,address) returns()": [
        [
            "NEQ",
            [
                "account",
                "address_1",
                "initialDefaultAdmin"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:AccessControl: 0 default admin"
        ]
    ],
    "ECDSA.recover(bytes32,bytes32,bytes32) returns(address)": [
        [
            "EQ",
            [
                "InvalidSignature@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature)"
        ],
        [
            "EQ",
            [
                "InvalidSignatureLength@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature length)"
        ],
        [
            "EQ",
            [
                "InvalidSignatureS@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature 's' value)"
        ]
    ],
    "EnumerableMap.get(EnumerableMap.AddressToUintMap,address,string) returns(uint256)": [
        [
            [
                [
                    "NEQ",
                    [
                        "_values@map",
                        "_values@map@value",
                        "value",
                        "_values@map@key"
                    ],
                    [
                        "0"
                    ]
                ],
                [
                    "contains(map,key)",
                    "contains(key)"
                ]
            ],
            "#Low#ERROR_MSG:errorMessage"
        ]
    ],
    "Math.log10(uint256,Math.Rounding) returns(uint256)": [],
    "Escrow.withdraw(address) returns()": [
        [
            [
                "onlyOwner",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "_deposits@recipient",
                "payment",
                "_deposits@payee",
                "amount"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance"
        ],
        [
            "success",
            "#Low#ERROR_MSG:Address: unable to send value, recipient may have reverted"
        ]
    ],
    "EnumerableSet.values(EnumerableSet.UintSet) returns(uint256[])": [],
    "SafeCast.toInt240(int256) returns(int240)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "value",
                "int256_1"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 240 bits"
        ]
    ],
    "Votes.delegates(address) returns(address)": [],
    "EnumerableMap.keys(EnumerableMap.AddressToUintMap) returns(address[])": [],
    "ERC721PresetMinterPauserAutoId.slitherConstructorConstantVariables() returns()": [],
    "ECDSA.tryRecover(bytes32,uint8,bytes32,bytes32) returns(address,ECDSA.RecoverError)": [],
    "Math.log256(uint256) returns(uint256)": [],
    "SafeCast.toInt232(int256) returns(int232)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "int256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 232 bits"
        ]
    ],
    "EnumerableMap.set(EnumerableMap.Bytes32ToUintMap,bytes32,uint256) returns(bool)": [],
    "ECDSA.recover(bytes32,uint8,bytes32,bytes32) returns(address)": [
        [
            "EQ",
            [
                "InvalidSignature@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature)"
        ],
        [
            "EQ",
            [
                "InvalidSignatureLength@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature length)"
        ],
        [
            "EQ",
            [
                "InvalidSignatureS@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature 's' value)"
        ]
    ],
    "Math.log256(uint256,Math.Rounding) returns(uint256)": [],
    "SafeCast.toInt224(int256) returns(int224)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "int256_1",
                "value"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ]
    ],
    "Votes.delegateBySig(address,uint256,uint256,uint8,bytes32,bytes32) returns()": [
        [
            "LTE",
            [
                "timestamp"
            ],
            [
                "uint256_2",
                "expiry"
            ],
            "#Medium#ERROR_MSG:Votes: signature expired"
        ],
        [
            "EQ",
            [
                "uint256_1",
                "nonce"
            ],
            [
                "_useNonce(signer)"
            ],
            "#Medium#ERROR_MSG:Votes: invalid nonce"
        ],
        [
            "LTE",
            [
                "value",
                "amount"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ],
        [
            "LTE",
            [
                "_key@_unsafeAccess(self,pos - 1)",
                "_key@last"
            ],
            [
                "key"
            ],
            "#Medium#ERROR_MSG:Checkpoint: decreasing keys"
        ],
        [
            "EQ",
            [
                "InvalidSignature@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature)"
        ],
        [
            "EQ",
            [
                "InvalidSignatureLength@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature length)"
        ],
        [
            "EQ",
            [
                "InvalidSignatureS@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature 's' value)"
        ]
    ],
    "EnumerableMap.remove(EnumerableMap.Bytes32ToUintMap,bytes32) returns(bool)": [],
    "ECDSA.toEthSignedMessageHash(bytes32) returns(bytes32)": [],
    "SafeCast.toUint248(uint256) returns(uint248)": [
        [
            "LTE",
            [
                "value",
                "uint256_1"
            ],
            [
                "max@type()(uint248)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 248 bits"
        ]
    ],
    "AccessControlDefaultAdminRules.supportsInterface(bytes4) returns(bool)": [],
    "SafeCast.toInt216(int256) returns(int216)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "int256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 216 bits"
        ]
    ],
    "EnumerableMap.contains(EnumerableMap.Bytes32ToUintMap,bytes32) returns(bool)": [],
    "ECDSA.toEthSignedMessageHash(bytes) returns(bytes32)": [],
    "SafeCast.toUint240(uint256) returns(uint240)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint240)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 240 bits"
        ]
    ],
    "SafeCast.toInt208(int256) returns(int208)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "value",
                "int256_1"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 208 bits"
        ]
    ],
    "AccessControlDefaultAdminRules.owner() returns(address)": [],
    "EnumerableMap.length(EnumerableMap.Bytes32ToUintMap) returns(uint256)": [],
    "ERC777.symbol() returns(string)": [],
    "ECDSA.toTypedDataHash(bytes32,bytes32) returns(bytes32)": [],
    "SafeCast.toUint232(uint256) returns(uint232)": [
        [
            "LTE",
            [
                "value",
                "uint256_1"
            ],
            [
                "max@type()(uint232)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 232 bits"
        ]
    ],
    "SafeCast.toInt200(int256) returns(int200)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "int256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 200 bits"
        ]
    ],
    "AccessControlDefaultAdminRules.grantRole(bytes32,address) returns()": [
        [
            "NEQ",
            [
                "role",
                "bytes32_1"
            ],
            [
                "DEFAULT_ADMIN_ROLE",
                "0x00",
                "bytes32"
            ],
            "#Medium#ERROR_MSG:AccessControl: can't directly grant default admin role"
        ],
        [
            [
                "onlyRole",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ]
    ],
    "EnumerableMap.at(EnumerableMap.Bytes32ToUintMap,uint256) returns(bytes32,uint256)": [],
    "ECDSA.toDataWithIntendedValidatorHash(address,bytes) returns(bytes32)": [],
    "AccessControlDefaultAdminRules.revokeRole(bytes32,address) returns()": [
        [
            "NEQ",
            [
                "role",
                "bytes32_1"
            ],
            [
                "DEFAULT_ADMIN_ROLE",
                "0x00",
                "bytes32"
            ],
            "#Medium#ERROR_MSG:AccessControl: can't directly revoke default admin role"
        ],
        [
            [
                "onlyRole",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ]
    ],
    "SafeCast.toUint224(uint256) returns(uint224)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ]
    ],
    "SafeCast.toInt192(int256) returns(int192)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "int256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 192 bits"
        ]
    ],
    "GovernorVoteMocks.slitherConstructorConstantVariables() returns()": [],
    "ERC777.granularity() returns(uint256)": [],
    "UUPSUpgradeableMock.slitherConstructorConstantVariables() returns()": [],
    "MerkleProof.verify(bytes32[],bytes32,bytes32) returns(bool)": [],
    "AccessControlDefaultAdminRules.renounceRole(bytes32,address) returns()": [
        [
            "EQ",
            [
                "newDefaultAdmin"
            ],
            [
                "address(0)"
            ],
            "#High#ERROR_MSG:AccessControl: only can renounce in two delayed steps"
        ],
        [
            "_isScheduleSet(schedule)",
            [
                "NEQ",
                [
                    "schedule"
                ],
                [
                    "0"
                ]
            ],
            "#High#ERROR_MSG:AccessControl: only can renounce in two delayed steps"
        ],
        [
            "_hasSchedulePassed(schedule)",
            [
                "LT",
                [
                    "schedule"
                ],
                [
                    "timestamp"
                ]
            ],
            "#High#ERROR_MSG:AccessControl: only can renounce in two delayed steps"
        ],
        [
            "EQ",
            [
                "account",
                "address_1"
            ],
            [
                "_msgSender()",
                "msgsender"
            ],
            "#High#ERROR_MSG:AccessControl: can only renounce roles for self"
        ]
    ],
    "SafeCast.toUint216(uint256) returns(uint216)": [
        [
            "LTE",
            [
                "value",
                "uint256_1"
            ],
            [
                "max@type()(uint216)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 216 bits"
        ]
    ],
    "SafeCast.toInt184(int256) returns(int184)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "int256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 184 bits"
        ]
    ],
    "EnumerableMap.get(EnumerableMap.Bytes32ToUintMap,bytes32) returns(uint256)": [
        [
            [
                [
                    "NEQ",
                    [
                        "value",
                        "_values@map",
                        "_values@map@key",
                        "_values@map@value"
                    ],
                    [
                        "0"
                    ]
                ],
                [
                    "contains(map,key)",
                    "contains(key)"
                ]
            ],
            "#Medium#ERROR_MSG:EnumerableMap: nonexistent key"
        ]
    ],
    "MerkleProof.verifyCalldata(bytes32[],bytes32,bytes32) returns(bool)": [],
    "SafeCast.toUint208(uint256) returns(uint208)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint208)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 208 bits"
        ]
    ],
    "SafeCast.toInt176(int256) returns(int176)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "int256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 176 bits"
        ]
    ],
    "AccessControlDefaultAdminRules._grantRole(bytes32,address) returns()": [
        [
            "EQ",
            [
                "defaultAdmin()",
                [
                    "_currentDefaultAdmin"
                ]
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:AccessControl: default admin already granted"
        ]
    ],
    "ERC721Enumerable._addTokenToAllTokensEnumeration(uint256) returns()": [],
    "Implementation4.getValue() returns(uint256)": [],
    "SafeMath.tryMul(uint256,uint256) returns(bool,uint256)": [],
    "ERC721Enumerable._removeTokenFromOwnerEnumeration(address,uint256) returns()": [
        [
            "NEQ",
            [
                "owner",
                "address_1",
                "from"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: address zero is not a valid owner"
        ]
    ],
    "Implementation4.fallback() returns()": [],
    "SafeMath.tryDiv(uint256,uint256) returns(bool,uint256)": [],
    "ERC721Enumerable._removeTokenFromAllTokensEnumeration(uint256) returns()": [],
    "SafeMath.tryMod(uint256,uint256) returns(bool,uint256)": [],
    "ERC4626._convertToAssets(uint256,Math.Rounding) returns(uint256)": [
        [
            "GT",
            [
                "denominator"
            ],
            [
                "prod1"
            ],
            "#Medium#ERROR_MSG:Math: mulDiv overflow"
        ]
    ],
    "ERC721Pausable._beforeTokenTransfer(address,address,uint256,uint256) returns()": [
        [
            "NOT",
            [
                "paused()",
                [
                    "_paused"
                ]
            ],
            "#High#ERROR_MSG:ERC721Pausable: token transfer while paused"
        ]
    ],
    "MigratableMockV2.migrate(uint256,uint256) returns()": [
        [
            "NOT",
            [
                "_migratedV2",
                "bool"
            ],
            "#Low#ERROR_MSG:None"
        ]
    ],
    "SafeMath.add(uint256,uint256) returns(uint256)": [],
    "ERC721URIStorage.supportsInterface(bytes4) returns(bool)": [],
    "EnumerableMap.set(EnumerableMap.Bytes32ToBytes32Map,bytes32,bytes32) returns(bool)": [],
    "SafeMath.sub(uint256,uint256) returns(uint256)": [],
    "EnumerableMap.remove(EnumerableMap.Bytes32ToBytes32Map,bytes32) returns(bool)": [],
    "SafeMath.mul(uint256,uint256) returns(uint256)": [],
    "MigratableMockV3.migrate() returns()": [
        [
            "NOT",
            [
                "_migratedV3",
                "bool"
            ],
            "#Low#ERROR_MSG:None"
        ]
    ],
    "ERC721URIStorage._setTokenURI(uint256,string) returns()": [
        [
            [
                "_exists(tokenId)",
                [
                    "NEQ",
                    [
                        "_ownerOf(tokenId)",
                        [
                            "_owners@tokenId"
                        ]
                    ],
                    [
                        "address(0)"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:ERC721URIStorage: URI set of nonexistent token"
        ]
    ],
    "EnumerableMap.contains(EnumerableMap.Bytes32ToBytes32Map,bytes32) returns(bool)": [],
    "SafeMath.div(uint256,uint256) returns(uint256)": [],
    "CrossChainEnabledPolygonChildMock.constructor(address) returns()": [],
    "EnumerableMap.length(EnumerableMap.Bytes32ToBytes32Map) returns(uint256)": [],
    "SafeMath.mod(uint256,uint256) returns(uint256)": [],
    "UUPSUpgradeableMock._authorizeUpgrade(address) returns()": [],
    "ERC721Votes._afterTokenTransfer(address,address,uint256,uint256) returns()": [
        [
            "LTE",
            [
                "value",
                "batchSize",
                "amount",
                "uint256_2"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ],
        [
            "LTE",
            [
                "_key@_unsafeAccess(self,pos - 1)",
                "_key@last"
            ],
            [
                "key"
            ],
            "#Medium#ERROR_MSG:Checkpoint: decreasing keys"
        ]
    ],
    "SafeMath.sub(uint256,uint256,string) returns(uint256)": [
        [
            "LTE",
            [
                "uint256_2",
                "b"
            ],
            [
                "uint256_1",
                "a"
            ],
            "#Low#ERROR_MSG:errorMessage"
        ]
    ],
    "EnumerableMap.at(EnumerableMap.Bytes32ToBytes32Map,uint256) returns(bytes32,bytes32)": [],
    "GovernorCompatibilityBravoMock.slitherConstructorConstantVariables() returns()": [],
    "UUPSUpgradeableUnsafeMock.upgradeTo(address) returns()": [
        [
            [
                "isContract(newImplementation)"
            ],
            "#Medium#ERROR_MSG:ERC1967: new implementation is not a contract"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "EnumerableMap.tryGet(EnumerableMap.Bytes32ToBytes32Map,bytes32) returns(bool,bytes32)": [],
    "ERC4626._withdraw(address,address,address,uint256,uint256) returns()": [
        [
            "NEQ",
            [
                "owner",
                "from",
                "account",
                "address_3"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: burn from the zero address"
        ],
        [
            "GTE",
            [
                "_balances@from",
                "_balances@account",
                "_balances@owner",
                "accountBalance"
            ],
            [
                "amount",
                "uint256_2",
                "shares"
            ],
            "#Medium#ERROR_MSG:ERC20: burn amount exceeds balance"
        ],
        [
            "GTE",
            [
                "allowance(owner,spender)",
                "_allowances@owner@spender",
                "_allowances@owner@caller",
                "currentAllowance"
            ],
            [
                "amount",
                "uint256_2",
                "shares"
            ],
            "#High#ERROR_MSG:ERC20: insufficient allowance"
        ],
        [
            "NEQ",
            [
                "owner",
                "from",
                "account",
                "address_3"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve from the zero address"
        ],
        [
            "NEQ",
            [
                "spender",
                "caller",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve to the zero address"
        ],
        [
            [
                [
                    "EQ",
                    [
                        "length@functionCall(data,SafeERC20: low-level call failed)",
                        "length@returndata"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ],
                [
                    "decode(returndata,(bool))"
                ]
            ],
            "#Medium#ERROR_MSG:SafeERC20: ERC20 operation did not succeed"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "SafeMath.div(uint256,uint256,string) returns(uint256)": [
        [
            "GT",
            [
                "uint256_2",
                "b"
            ],
            [
                "0"
            ],
            "#Low#ERROR_MSG:errorMessage"
        ]
    ],
    "UUPSUpgradeableUnsafeMock.upgradeToAndCall(address,bytes) returns()": [
        [
            [
                "isContract(newImplementation)"
            ],
            "#Medium#ERROR_MSG:ERC1967: new implementation is not a contract"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "ERC721Wrapper.constructor(IERC721) returns()": [],
    "EnumerableMap.get(EnumerableMap.Bytes32ToBytes32Map,bytes32) returns(bytes32)": [
        [
            [
                [
                    "NEQ",
                    [
                        "value",
                        "_values@map",
                        "_values@map@value",
                        "_values@map@key"
                    ],
                    [
                        "0"
                    ]
                ],
                [
                    "contains(map,key)",
                    "contains(key)"
                ]
            ],
            "#Medium#ERROR_MSG:EnumerableMap: nonexistent key"
        ]
    ],
    "GovernorVotesComp.slitherConstructorConstantVariables() returns()": [],
    "SafeMath.mod(uint256,uint256,string) returns(uint256)": [
        [
            "GT",
            [
                "uint256_2",
                "b"
            ],
            [
                "0"
            ],
            "#Low#ERROR_MSG:errorMessage"
        ]
    ],
    "ERC721ReceiverMock.constructor(bytes4,ERC721ReceiverMock.Error) returns()": [],
    "CompTimelock.executeTransaction(address,uint256,string,bytes,uint256) returns(bytes)": [
        [
            "EQ",
            [
                "msgsender"
            ],
            [
                "admin",
                "address"
            ],
            "#High#ERROR_MSG:Timelock::executeTransaction: Call must come from admin."
        ],
        [
            "queuedTransactions@encode(target,value,signature,data,eta))",
            "queuedTransactions@txHash",
            "#Medium#ERROR_MSG:Timelock::executeTransaction: Transaction hasn't been queued."
        ],
        [
            "GTE",
            [
                "getBlockTimestamp()",
                "timestamp"
            ],
            [
                "uint256_2",
                "eta"
            ],
            "#Medium#ERROR_MSG:Timelock::executeTransaction: Transaction hasn't surpassed time lock."
        ],
        [
            "LTE",
            [
                "getBlockTimestamp()",
                "timestamp"
            ],
            [
                "ADD",
                [
                    "uint256_2",
                    "eta"
                ],
                [
                    "1209600",
                    "GRACE_PERIOD",
                    "uint256"
                ]
            ],
            "#Medium#ERROR_MSG:Timelock::executeTransaction: Transaction is stale."
        ],
        [
            "success",
            "#Low#ERROR_MSG:Timelock::executeTransaction: Transaction execution reverted."
        ]
    ],
    "Pausable.constructor() returns()": [],
    "IAccessControl.grantRole(bytes32,address) returns()": [],
    "IGovernorCompatibilityBravo.propose(address[],uint256[],string[],bytes[],string) returns(uint256)": [],
    "CompTimelock.getBlockTimestamp() returns(uint256)": [],
    "ERC4626.mint(uint256,address) returns(uint256)": [
        [
            "LTE",
            [
                "shares",
                "amount",
                "assets",
                "Up)",
                "uint256_1",
                "previewMint(shares)",
                "x",
                "value"
            ],
            [
                "maxMint(receiver)",
                "max@type()(uint256)"
            ],
            "#Medium#ERROR_MSG:ERC4626: mint more than max"
        ],
        [
            "NEQ",
            [
                "receiver",
                "to",
                "account",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: mint to the zero address"
        ],
        [
            [
                [
                    "EQ",
                    [
                        "length@functionCall(data,SafeERC20: low-level call failed)",
                        "length@returndata"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ],
                [
                    "decode(returndata,(bool))"
                ]
            ],
            "#Medium#ERROR_MSG:SafeERC20: ERC20 operation did not succeed"
        ],
        [
            "GT",
            [
                "denominator",
                "100000"
            ],
            [
                "prod1"
            ],
            "#Medium#ERROR_MSG:Math: mulDiv overflow"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "BaseRelayMock.relayAs(address,bytes,address) returns()": [
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "BridgeAMBMock.messageSender() returns(address)": [],
    "GovernorTimelockCompound._cancel(address[],uint256[],bytes[],bytes32) returns(uint256)": [
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Canceled@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Expired@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Executed@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "EQ",
            [
                "0"
            ],
            [
                "proposalSnapshot(proposalId)",
                "REF_1872",
                "voteStart@_proposals@_cancel(targets,values,calldatas,descriptionHash)",
                "voteStart@_proposals@encode(targets,values,calldatas,descriptionHash)))",
                "voteStart@_proposals@hashProposal(targets,values,calldatas,descriptionHash)",
                "voteStart@_proposals@proposalId",
                "snapshot",
                "voteStart@proposal"
            ],
            "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
        ]
    ],
    "BridgeArbitrumL1Mock.activeOutbox() returns(address)": [],
    "Pausable._requireNotPaused() returns()": [],
    "BridgeArbitrumL1Mock.currentSender() returns(address)": [],
    "TokenTimelock.constructor(IERC20,address,uint256) returns()": [],
    "BridgeArbitrumL1Outbox.l2ToL1Sender() returns(address)": [],
    "ERC20PresetFixedSupply.constructor(string,string,uint256,address) returns()": [],
    "TokenTimelock.token() returns(IERC20)": [],
    "BridgeArbitrumL2Mock.wasMyCallersAddressAliased() returns(bool)": [],
    "TokenTimelock.beneficiary() returns(address)": [],
    "BridgeArbitrumL2Mock.myCallersAddressWithoutAliasing() returns(address)": [],
    "PullPayment.withdrawPayments(address) returns()": [
        [
            [
                "onlyOwner",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "_deposits@payee",
                "payment",
                "amount",
                "_deposits@recipient"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance"
        ],
        [
            "success",
            "#Low#ERROR_MSG:Address: unable to send value, recipient may have reverted"
        ]
    ],
    "GovernorTimelockCompound.__acceptAdmin() returns()": [],
    "TokenTimelock.releaseTime() returns(uint256)": [],
    "Checkpoints.upperLookup(Checkpoints.Trace224,uint32) returns(uint224)": [],
    "VestingWallet.releasable(address) returns(uint256)": [],
    "ERC20VotesLegacyMock.numCheckpoints(address) returns(uint32)": [
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ]
    ],
    "Checkpoints.upperLookupRecent(Checkpoints.Trace224,uint32) returns(uint224)": [],
    "VestingWallet.release() returns()": [
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "timestamp))@_released",
                "balance + released(),timestamp)@_released",
                "amount",
                "releasable()",
                "timestamp))@released()",
                "balance + released(),timestamp)@released()"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance"
        ],
        [
            "success",
            "#Low#ERROR_MSG:Address: unable to send value, recipient may have reverted"
        ]
    ],
    "ERC20VotesLegacyMock.delegates(address) returns(address)": [],
    "Checkpoints.latest(Checkpoints.Trace224) returns(uint224)": [],
    "VestingWallet.release(address) returns()": [
        [
            [
                [
                    "EQ",
                    [
                        "length@functionCall(data,SafeERC20: low-level call failed)",
                        "length@returndata"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ],
                [
                    "decode(returndata,(bool))"
                ]
            ],
            "#Medium#ERROR_MSG:SafeERC20: ERC20 operation did not succeed"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "ERC20VotesLegacyMock.getVotes(address) returns(uint256)": [],
    "Checkpoints.latestCheckpoint(Checkpoints.Trace224) returns(bool,uint32,uint224)": [],
    "StorageSlot.getAddressSlot(bytes32) returns(StorageSlot.AddressSlot)": [],
    "VestingWallet.vestedAmount(uint64) returns(uint256)": [],
    "ERC20VotesLegacyMock.getPastVotes(address,uint256) returns(uint256)": [
        [
            "LT",
            [
                "blockNumber",
                "uint256_1"
            ],
            [
                "number"
            ],
            "#Low#ERROR_MSG:ERC20Votes: block not yet mined"
        ]
    ],
    "Checkpoints.length(Checkpoints.Trace224) returns(uint256)": [],
    "StorageSlot.getBooleanSlot(bytes32) returns(StorageSlot.BooleanSlot)": [],
    "VestingWallet.vestedAmount(address,uint64) returns(uint256)": [],
    "ERC20VotesLegacyMock.getPastTotalSupply(uint256) returns(uint256)": [
        [
            "LT",
            [
                "uint256_1",
                "blockNumber"
            ],
            [
                "number"
            ],
            "#Low#ERROR_MSG:ERC20Votes: block not yet mined"
        ]
    ],
    "Checkpoints._insert(Checkpoints.Checkpoint224[],uint32,uint224) returns(uint224,uint224)": [
        [
            "LTE",
            [
                "_key@_unsafeAccess(self,pos - 1)",
                "_key@last"
            ],
            [
                "uint32_1",
                "key"
            ],
            "#Medium#ERROR_MSG:Checkpoint: decreasing keys"
        ]
    ],
    "StorageSlot.getBytes32Slot(bytes32) returns(StorageSlot.Bytes32Slot)": [],
    "VestingWallet._vestingSchedule(uint256,uint64) returns(uint256)": [],
    "BridgeArbitrumL1Outbox.slitherConstructorVariables() returns()": [],
    "ERC20VotesLegacyMock._checkpointsLookup(ERC20VotesLegacyMock.Checkpoint[],uint256) returns(uint256)": [],
    "CrossChainEnabled._isCrossChain() returns(bool)": [],
    "Checkpoints._upperBinaryLookup(Checkpoints.Checkpoint224[],uint32,uint256,uint256) returns(uint256)": [],
    "ERC20VotesLegacyMock.delegate(address) returns()": [
        [
            "LTE",
            [
                "value",
                "newWeight"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ]
    ],
    "StorageSlot.getUint256Slot(bytes32) returns(StorageSlot.Uint256Slot)": [],
    "Checkpoints._lowerBinaryLookup(Checkpoints.Checkpoint224[],uint32,uint256,uint256) returns(uint256)": [],
    "ERC20VotesLegacyMock.delegateBySig(address,uint256,uint256,uint8,bytes32,bytes32) returns()": [
        [
            "LTE",
            [
                "timestamp"
            ],
            [
                "uint256_2",
                "expiry"
            ],
            "#Medium#ERROR_MSG:ERC20Votes: signature expired"
        ],
        [
            "EQ",
            [
                "nonce",
                "uint256_1"
            ],
            [
                "_useNonce(signer)"
            ],
            "#Medium#ERROR_MSG:ERC20Votes: invalid nonce"
        ],
        [
            "LTE",
            [
                "value",
                "newWeight"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ]
    ],
    "StorageSlot.getStringSlot(bytes32) returns(StorageSlot.StringSlot)": [],
    "Checkpoints._unsafeAccess(Checkpoints.Checkpoint224[],uint256) returns(Checkpoints.Checkpoint224)": [],
    "ERC20VotesLegacyMock._maxSupply() returns(uint224)": [],
    "StorageSlot.getStringSlot(string) returns(StorageSlot.StringSlot)": [],
    "Checkpoints.push(Checkpoints.Trace160,uint96,uint160) returns(uint160,uint160)": [
        [
            "LTE",
            [
                "_key@_unsafeAccess(self,pos - 1)",
                "_key@last"
            ],
            [
                "uint96_1",
                "key"
            ],
            "#Medium#ERROR_MSG:Checkpoint: decreasing keys"
        ]
    ],
    "ERC777.approve(address,uint256) returns(bool)": [
        [
            "NEQ",
            [
                "_msgSender()",
                "msgsender",
                "holder"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC777: approve from the zero address"
        ],
        [
            "NEQ",
            [
                "spender",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC777: approve to the zero address"
        ]
    ],
    "AccessControl.onlyRole(bytes32) returns()": [],
    "ERC20VotesLegacyMock._mint(address,uint256) returns()": [
        [
            "LTE",
            [
                "totalSupply()",
                [
                    "_totalSupply"
                ]
            ],
            [
                "_maxSupply()",
                "max@type()(uint224)"
            ],
            "#Medium#ERROR_MSG:ERC20Votes: total supply risks overflowing votes"
        ],
        [
            "NEQ",
            [
                "to",
                "account",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: mint to the zero address"
        ],
        [
            "LTE",
            [
                "value",
                "newWeight"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ]
    ],
    "Checkpoints.lowerLookup(Checkpoints.Trace160,uint96) returns(uint160)": [],
    "StorageSlot.getBytesSlot(bytes32) returns(StorageSlot.BytesSlot)": [],
    "ERC20VotesLegacyMock._burn(address,uint256) returns()": [
        [
            "NEQ",
            [
                "from",
                "account",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: burn from the zero address"
        ],
        [
            "GTE",
            [
                "_balances@from",
                "_balances@account",
                "accountBalance"
            ],
            [
                "delta",
                "amount",
                "uint256_1"
            ],
            "#Medium#ERROR_MSG:ERC20: burn amount exceeds balance"
        ],
        [
            "LTE",
            [
                "value",
                "newWeight"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ]
    ],
    "GovernorCompatibilityBravo.propose(address[],uint256[],bytes[],string) returns(uint256)": [
        [
            [
                "_isValidDescriptionForProposer(proposer,description)"
            ],
            "#High#ERROR_MSG:Governor: proposer restricted"
        ],
        [
            "GTE",
            [
                "getVotes(proposer,currentTimepoint - 1)",
                "_getVotes(account,timepoint,_defaultParams())"
            ],
            [
                "proposalThreshold()",
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: proposer votes below proposal threshold"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@values"
            ],
            "#Medium#ERROR_MSG:Governor: invalid proposal length"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@calldatas"
            ],
            "#Medium#ERROR_MSG:Governor: invalid proposal length"
        ],
        [
            "GT",
            [
                "length@targets"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: empty proposal"
        ],
        [
            "EQ",
            [
                "voteStart@_proposals@hashProposal(targets,values,calldatas,keccak256(bytes)(bytes(description)))",
                "voteStart@_proposals@encode(targets,values,calldatas,descriptionHash)))",
                "voteStart@_proposals@proposalId"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: proposal already exists"
        ],
        [
            "LTE",
            [
                "value",
                "snapshot",
                "deadline",
                "snapshot + votingPeriod()",
                "currentTimepoint + votingDelay()"
            ],
            [
                "max@type()(uint64)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 64 bits"
        ]
    ],
    "Checkpoints.upperLookup(Checkpoints.Trace160,uint96) returns(uint160)": [],
    "StorageSlot.getBytesSlot(bytes) returns(StorageSlot.BytesSlot)": [],
    "AccessControl.supportsInterface(bytes4) returns(bool)": [],
    "AccessControlCrossChainMock.slitherConstructorConstantVariables() returns()": [],
    "ERC20VotesComp._maxSupply() returns(uint224)": [],
    "Address.isContract(address) returns(bool)": [],
    "ERC20Wrapper.constructor(IERC20) returns()": [],
    "Proxy.fallback() returns()": [],
    "Address.sendValue(address,uint256) returns()": [
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "uint256_1",
                "amount"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance"
        ],
        [
            "success",
            "#Low#ERROR_MSG:Address: unable to send value, recipient may have reverted"
        ]
    ],
    "ERC20Wrapper.decimals() returns(uint8)": [],
    "Address.functionCall(address,bytes) returns(bytes)": [
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "ERC20Wrapper.underlying() returns(IERC20)": [],
    "Address.functionCall(address,bytes,string) returns(bytes)": [
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "Proxy._beforeFallback() returns()": [],
    "Address.functionCallWithValue(address,bytes,uint256) returns(bytes)": [
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "uint256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "ERC20Wrapper.withdrawTo(address,uint256) returns(bool)": [
        [
            "NEQ",
            [
                "from",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: burn from the zero address"
        ],
        [
            "GTE",
            [
                "_balances@from",
                "_balances@account",
                "accountBalance"
            ],
            [
                "amount",
                "uint256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:ERC20: burn amount exceeds balance"
        ],
        [
            [
                [
                    "EQ",
                    [
                        "length@functionCall(data,SafeERC20: low-level call failed)",
                        "length@returndata"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ],
                [
                    "decode(returndata,(bool))"
                ]
            ],
            "#Medium#ERROR_MSG:SafeERC20: ERC20 operation did not succeed"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "Address.functionCallWithValue(address,bytes,uint256,string) returns(bytes)": [
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "uint256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "Address.functionStaticCall(address,bytes) returns(bytes)": [
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "ERC4626.constructor(IERC20) returns()": [],
    "Address.functionStaticCall(address,bytes,string) returns(bytes)": [
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "ERC721Burnable.burn(uint256) returns()": [
        [
            [
                "_isApprovedOrOwner(_msgSender(),tokenId)",
                "_isApprovedOrOwner(msgsender,tokenId)",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "spender"
                    ],
                    [
                        "ownerOf(tokenId)",
                        "owner"
                    ]
                ],
                "isApprovedForAll(_msgSender(),tokenId)",
                "isApprovedForAll(msgsender,tokenId)",
                "_operatorApprovals@_msgSender()@tokenId",
                "_operatorApprovals@msgsender@tokenId",
                [
                    "EQ",
                    "getApproved(tokenId)",
                    [
                        "_msgSender()",
                        "msgsender"
                    ]
                ]
            ],
            "#High#ERROR_MSG:ERC721: caller is not token owner or approved"
        ],
        [
            "NEQ",
            [
                "_ownerOf(tokenId)",
                "_owners@tokenId",
                "_owners@firstTokenId",
                "owner"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: invalid token ID"
        ]
    ],
    "Address.functionDelegateCall(address,bytes) returns(bytes)": [
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "ERC777.slitherConstructorConstantVariables() returns()": [],
    "Address.functionDelegateCall(address,bytes,string) returns(bytes)": [
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "ERC4626.decimals() returns(uint8)": [],
    "Address.verifyCallResultFromTarget(address,bool,bytes,string) returns(bytes)": [
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "ERC1155URIStorage.slitherConstructorVariables() returns()": [],
    "Bytes32ArraysMock.unsafeAccess(uint256) returns(bytes32)": [],
    "CallReceiverMock.mockFunction() returns(string)": [],
    "CallReceiverMock.mockFunctionEmptyReturn() returns()": [],
    "GovernorTimelockCompound.supportsInterface(bytes4) returns(bool)": [],
    "CallReceiverMock.mockFunctionWithArgs(uint256,uint256) returns(string)": [],
    "GovernorTimelockCompound.state(uint256) returns(IGovernor.ProposalState)": [
        [
            "EQ",
            [
                "0"
            ],
            [
                "proposalSnapshot(proposalId)",
                "REF_2545",
                "voteStart@_proposals@proposalId",
                "snapshot",
                "voteStart@proposal"
            ],
            "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
        ]
    ],
    "CallReceiverMock.mockFunctionNonPayable() returns(string)": [],
    "CallReceiverMock.mockStaticFunction() returns(string)": [],
    "GovernorTimelockCompound.proposalEta(uint256) returns(uint256)": [],
    "CallReceiverMock.mockFunctionRevertsNoReason() returns()": [],
    "CallReceiverMock.mockFunctionRevertsReason() returns()": [],
    "GovernorTimelockCompound._execute(uint256,address[],uint256[],bytes[],bytes32) returns()": [
        [
            "GT",
            [
                "proposalEta(proposalId)",
                "eta"
            ],
            [
                "0"
            ],
            "#Low#ERROR_MSG:GovernorTimelockCompound: proposal not yet queued"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "amount"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance"
        ],
        [
            "success",
            "#Low#ERROR_MSG:Address: unable to send value, recipient may have reverted"
        ]
    ],
    "CallReceiverMock.mockFunctionThrows() returns()": [
        [
            "false",
            "#Low#ERROR_MSG:None"
        ]
    ],
    "Receiver.slitherConstructorVariables() returns()": [],
    "CallReceiverMock.mockFunctionOutOfGas() returns()": [],
    "Base64.slitherConstructorConstantVariables() returns()": [],
    "Checkpoints.getAtProbablyRecentBlock(Checkpoints.History,uint256) returns(uint256)": [
        [
            "LT",
            [
                "blockNumber",
                "uint256_1",
                "value"
            ],
            [
                "number"
            ],
            "#Medium#ERROR_MSG:Checkpoints: block not yet mined"
        ],
        [
            "LTE",
            [
                "value",
                "blockNumber",
                "uint256_1"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ]
    ],
    "CallReceiverMock.mockFunctionWritesStorage(bytes32,bytes32) returns(string)": [],
    "PaymentSplitter.receive() returns()": [],
    "PullPaymentMock.constructor() returns()": [],
    "PaymentSplitter.totalShares() returns(uint256)": [],
    "PullPaymentMock.callTransfer(address,uint256) returns()": [
        [
            [
                "onlyOwner",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ]
    ],
    "PaymentSplitter.totalReleased() returns(uint256)": [],
    "ReentrancyAttack.callSender(bytes4) returns()": [
        [
            "success",
            "#Medium#ERROR_MSG:ReentrancyAttack: failed call"
        ]
    ],
    "PaymentSplitter.totalReleased(IERC20) returns(uint256)": [],
    "ReentrancyMock.constructor() returns()": [],
    "PaymentSplitter.shares(address) returns(uint256)": [],
    "ReentrancyMock.callback() returns()": [
        [
            "nonReentrant"
        ]
    ],
    "PaymentSplitter.released(address) returns(uint256)": [],
    "ReentrancyMock.countLocalRecursive(uint256) returns()": [
        [
            "nonReentrant"
        ]
    ],
    "ERC1155PresetMinterPauser.slitherConstructorConstantVariables() returns()": [],
    "PaymentSplitter.released(IERC20,address) returns(uint256)": [],
    "ReentrancyMock.countThisRecursive(uint256) returns()": [
        [
            "success",
            "#Medium#ERROR_MSG:ReentrancyMock: failed call"
        ],
        [
            "nonReentrant"
        ]
    ],
    "PaymentSplitter.payee(uint256) returns(address)": [],
    "ERC777.send(address,uint256,bytes) returns()": [
        [
            "NEQ",
            [
                "to",
                "account",
                "from",
                "address_1",
                "recipient"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC777: transfer from the zero address"
        ],
        [
            "NEQ",
            [
                "to",
                "account",
                "from",
                "address_1",
                "recipient"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC777: transfer to the zero address"
        ],
        [
            "NOT",
            [
                "isContract()"
            ],
            "#Medium#ERROR_MSG:ERC777: token recipient contract has no implementer for ERC777TokensRecipient"
        ],
        [
            "GTE",
            [
                "_balances@to",
                "_balances@from",
                "_balances@recipient",
                "fromBalance",
                "_balances@account"
            ],
            [
                "amount",
                "uint256_1"
            ],
            "#Medium#ERROR_MSG:ERC777: transfer amount exceeds balance"
        ]
    ],
    "ReentrancyMock.countAndCall(ReentrancyAttack) returns()": [
        [
            "nonReentrant"
        ],
        [
            "success",
            "#Medium#ERROR_MSG:ReentrancyAttack: failed call"
        ]
    ],
    "PaymentSplitter.releasable(address) returns(uint256)": [],
    "ReentrancyMock._count() returns()": [],
    "PaymentSplitter.releasable(IERC20,address) returns(uint256)": [],
    "ReentrancyMock.guardedCheckEntered() returns()": [
        [
            [
                "_reentrancyGuardEntered()",
                [
                    "EQ",
                    [
                        "_status",
                        "uint256"
                    ],
                    [
                        "2",
                        "_ENTERED",
                        "uint256"
                    ]
                ]
            ],
            "#Low#ERROR_MSG:None"
        ],
        [
            "nonReentrant"
        ]
    ],
    "PaymentSplitter.release(address) returns()": [
        [
            "GT",
            [
                "_shares@account"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:PaymentSplitter: account has no shares"
        ],
        [
            "NEQ",
            [
                "releasable(account)",
                "payment",
                "amount"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:PaymentSplitter: account is not due payment"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "releasable(account)",
                "payment",
                "amount"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance"
        ],
        [
            "success",
            "#Low#ERROR_MSG:Address: unable to send value, recipient may have reverted"
        ]
    ],
    "ERC20Votes.delegateBySig(address,uint256,uint256,uint8,bytes32,bytes32) returns()": [
        [
            "LTE",
            [
                "value",
                "timestamp"
            ],
            [
                "uint256_2",
                "expiry"
            ],
            "#Medium#ERROR_MSG:ERC20Votes: signature expired"
        ],
        [
            "EQ",
            [
                "uint256_1",
                "nonce"
            ],
            [
                "_useNonce(signer)"
            ],
            "#Medium#ERROR_MSG:ERC20Votes: invalid nonce"
        ],
        [
            "LTE",
            [
                "value",
                "newWeight"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "timestamp"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ],
        [
            "EQ",
            [
                "InvalidSignature@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature)"
        ],
        [
            "EQ",
            [
                "InvalidSignatureLength@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature length)"
        ],
        [
            "EQ",
            [
                "InvalidSignatureS@RecoverError"
            ],
            [
                "error"
            ],
            "#Medium#ERROR_MSG:(ECDSA: invalid signature 's' value)"
        ]
    ],
    "GovernorVotes.slitherConstructorConstantVariables() returns()": [],
    "ReentrancyMock.unguardedCheckNotEntered() returns()": [
        [
            "NOT",
            [
                "_reentrancyGuardEntered()",
                [
                    "EQ",
                    [
                        "_status",
                        "uint256"
                    ],
                    [
                        "2",
                        "_ENTERED",
                        "uint256"
                    ]
                ]
            ],
            "#Low#ERROR_MSG:None"
        ]
    ],
    "PaymentSplitter.release(IERC20,address) returns()": [
        [
            "GT",
            [
                "_shares@account"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:PaymentSplitter: account has no shares"
        ],
        [
            "NEQ",
            [
                "releasable(token,account)",
                "value",
                "payment"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:PaymentSplitter: account is not due payment"
        ],
        [
            [
                [
                    "EQ",
                    [
                        "length@functionCall(data,SafeERC20: low-level call failed)",
                        "length@returndata"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ],
                [
                    "decode(returndata,(bool))"
                ]
            ],
            "#Medium#ERROR_MSG:SafeERC20: ERC20 operation did not succeed"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "UUPSUpgradeable.onlyProxy() returns()": [
        [
            "NEQ",
            [
                "address(this)"
            ],
            [
                "address(this)",
                "__self",
                "address"
            ],
            "#Medium#ERROR_MSG:Function must be called through delegatecall"
        ],
        [
            "EQ",
            [
                "_getImplementation()",
                [
                    "value@getAddressSlot(_IMPLEMENTATION_SLOT)"
                ]
            ],
            [
                "address(this)",
                "__self",
                "address"
            ],
            "#Medium#ERROR_MSG:Function must be called through active proxy"
        ]
    ],
    "ERC4626Fees.previewMint(uint256) returns(uint256)": [
        [
            "GT",
            [
                "denominator",
                "100000"
            ],
            [
                "prod1"
            ],
            "#Medium#ERROR_MSG:Math: mulDiv overflow"
        ]
    ],
    "ERC1155ReceiverMock.onERC1155Received(address,address,uint256,uint256,bytes) returns(bytes4)": [
        [
            "NOT",
            [
                "_recReverts",
                "bool"
            ],
            "#Medium#ERROR_MSG:ERC1155ReceiverMock: reverting on receive"
        ]
    ],
    "ERC1155ReceiverMock.onERC1155BatchReceived(address,address,uint256[],uint256[],bytes) returns(bytes4)": [
        [
            "NOT",
            [
                "_batReverts",
                "bool"
            ],
            "#Medium#ERROR_MSG:ERC1155ReceiverMock: reverting on batch receive"
        ]
    ],
    "UUPSUpgradeable.proxiableUUID() returns(bytes32)": [
        [
            "notDelegated"
        ],
        [
            "EQ",
            [
                "address(this)"
            ],
            [
                "address(this)",
                "__self",
                "address"
            ],
            "#Medium#ERROR_MSG:UUPSUpgradeable: must not be called through delegatecall"
        ]
    ],
    "ERC20DecimalsMock.constructor(uint8) returns()": [],
    "ERC20DecimalsMock.decimals() returns(uint8)": [],
    "ERC20FlashMintMock.setFlashFee(uint256) returns()": [],
    "ERC4626Fees.previewRedeem(uint256) returns(uint256)": [
        [
            "GT",
            [
                "denominator"
            ],
            [
                "prod1"
            ],
            "#Medium#ERROR_MSG:Math: mulDiv overflow"
        ]
    ],
    "DisableOld.constructor() returns()": [],
    "PullPayment.constructor() returns()": [],
    "ERC20FlashMintMock._flashFee(address,uint256) returns(uint256)": [],
    "ERC20FlashMintMock.setFlashFeeReceiver(address) returns()": [],
    "PullPayment.payments(address) returns(uint256)": [],
    "ERC20FlashMintMock._flashFeeReceiver() returns(address)": [],
    "EnumerableSet._length(EnumerableSet.Set) returns(uint256)": [],
    "GovernorTimelockCompoundMock._execute(uint256,address[],uint256[],bytes[],bytes32) returns()": [
        [
            "GT",
            [
                "proposalEta(proposalId)",
                "eta",
                "_proposalTimelocks@proposalId"
            ],
            [
                "0"
            ],
            "#Low#ERROR_MSG:GovernorTimelockCompound: proposal not yet queued"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "amount"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance"
        ],
        [
            "success",
            "#Low#ERROR_MSG:Address: unable to send value, recipient may have reverted"
        ]
    ],
    "TimersBlockNumberImpl.setDeadline(uint64) returns()": [],
    "GovernorTimelockCompoundMock._cancel(address[],uint256[],bytes[],bytes32) returns(uint256)": [
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Canceled@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Expired@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Executed@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ]
    ],
    "TimersBlockNumberImpl.reset() returns()": [],
    "GovernorTimelockCompoundMock._executor() returns(address)": [],
    "TimersBlockNumberImpl.isUnset() returns(bool)": [],
    "ERC20Snapshot._snapshot() returns(uint256)": [],
    "GovernorTimelockControlMock.supportsInterface(bytes4) returns(bool)": [],
    "TimersBlockNumberImpl.isStarted() returns(bool)": [],
    "GovernorTimelockControlMock.quorum(uint256) returns(uint256)": [
        [
            "LTE",
            [
                "timepoint",
                "value",
                "blockNumber",
                "uint256_1"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ]
    ],
    "TimersBlockNumberImpl.isPending() returns(bool)": [],
    "GovernorPreventLateQuorum.constructor(uint64) returns()": [],
    "TimersBlockNumberImpl.isExpired() returns(bool)": [],
    "GovernorTimelockControlMock.state(uint256) returns(IGovernor.ProposalState)": [],
    "TimersTimestampImpl.getDeadline() returns(uint64)": [],
    "GovernorTimelockControlMock.proposalThreshold() returns(uint256)": [],
    "GovernorPreventLateQuorum._castVote(uint256,address,uint8,string,bytes) returns(uint256)": [
        [
            "EQ",
            [
                "state(proposalId)"
            ],
            [
                "Active@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: vote not currently active"
        ],
        [
            "EQ",
            [
                "0"
            ],
            [
                "proposalSnapshot(proposalId)",
                "REF_1872",
                "voteStart@_proposals@proposalId",
                "voteStart@proposal",
                "snapshot"
            ],
            "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
        ]
    ],
    "GovernorTimelockControlMock._execute(uint256,address[],uint256[],bytes[],bytes32) returns()": [
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@values"
            ],
            "#Medium#ERROR_MSG:TimelockController: length mismatch"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@payloads"
            ],
            "#Medium#ERROR_MSG:TimelockController: length mismatch"
        ],
        [
            "onlyRoleOrOpenRole"
        ],
        [
            [
                "isOperationReady(id)"
            ],
            "#Medium#ERROR_MSG:TimelockController: operation is not ready"
        ],
        [
            [
                [
                    "EQ",
                    [
                        "predecessor",
                        "hashOperationBatch(targets,values,payloads,predecessor,salt)",
                        "0",
                        "id",
                        "encode(targets,values,payloads,predecessor,salt))"
                    ],
                    [
                        "bytes32(0)"
                    ]
                ],
                [
                    "isOperationDone(predecessor)",
                    [
                        "EQ",
                        [
                            "getTimestamp(id)",
                            [
                                "_timestamps@id",
                                "_timestamps@0",
                                "_timestamps@predecessor",
                                "_timestamps@hashOperationBatch(targets,values,payloads,predecessor,salt)",
                                "_timestamps@encode(targets,values,payloads,predecessor,salt))",
                                "timestamp",
                                "getTimestamp(id)"
                            ]
                        ],
                        [
                            "_DONE_TIMESTAMP",
                            "uint256(1)",
                            "uint256"
                        ]
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:TimelockController: missing dependency"
        ],
        [
            "success",
            "#Medium#ERROR_MSG:TimelockController: underlying transaction reverted"
        ]
    ],
    "TimersTimestampImpl.setDeadline(uint64) returns()": [],
    "BeaconProxy.slitherConstructorConstantVariables() returns()": [],
    "GovernorPreventLateQuorum.proposalDeadline(uint256) returns(uint256)": [],
    "GovernorTimelockControlMock._cancel(address[],uint256[],bytes[],bytes32) returns(uint256)": [
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Canceled@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Expired@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Executed@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            [
                "isOperationPending(id)",
                [
                    "GT",
                    [
                        "getTimestamp(id)",
                        [
                            "_timestamps@id"
                        ]
                    ],
                    [
                        "_DONE_TIMESTAMP",
                        "uint256(1)",
                        "uint256"
                    ]
                ]
            ],
            "#High#ERROR_MSG:TimelockController: operation cannot be cancelled"
        ],
        [
            [
                "onlyRole",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ]
    ],
    "TimersTimestampImpl.reset() returns()": [],
    "GovernorTimelockControlMock._executor() returns(address)": [],
    "TimersTimestampImpl.isUnset() returns(bool)": [],
    "MyGovernor.slitherConstructorConstantVariables() returns()": [],
    "GovernorPreventLateQuorum.lateQuorumVoteExtension() returns(uint64)": [],
    "GovernorTimelockControlMock.nonGovernanceFunction() returns()": [],
    "TimersTimestampImpl.isStarted() returns(bool)": [],
    "GovernorVoteMocks.quorum(uint256) returns(uint256)": [],
    "TimersTimestampImpl.isPending() returns(bool)": [],
    "ReinitializerMock.disableInitializers() returns()": [
        [
            "NOT",
            [
                "_initializing",
                "bool"
            ],
            "#Low#ERROR_MSG:Initializable: contract is initializing"
        ]
    ],
    "TimelockController.onERC721Received(address,address,uint256,bytes) returns(bytes4)": [],
    "SafeCast.toUint192(uint256) returns(uint192)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint192)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 192 bits"
        ]
    ],
    "ReinitializerMock.doStuff() returns()": [
        [
            "onlyInitializing"
        ],
        [
            "_initializing",
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "ERC1155._mint(address,uint256,uint256,bytes) returns()": [
        [
            "NEQ",
            [
                "to",
                "account",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC1155: mint to the zero address"
        ],
        [
            "NEQ",
            [
                "selector@onERC1155Received@IERC1155Receiver"
            ],
            [
                "response"
            ],
            "#High#ERROR_MSG:ERC1155: ERC1155Receiver rejected tokens"
        ]
    ],
    "TimelockController.onERC1155Received(address,address,uint256,uint256,bytes) returns(bytes4)": [],
    "SafeCast.toUint184(uint256) returns(uint184)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint184)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 184 bits"
        ]
    ],
    "TimelockController.onERC1155BatchReceived(address,address,uint256[],uint256[],bytes) returns(bytes4)": [],
    "Ownable.onlyOwner() returns()": [],
    "SafeCast.toUint176(uint256) returns(uint176)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint176)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 176 bits"
        ]
    ],
    "ERC1155.balanceOfBatch(address[],uint256[]) returns(uint256[])": [
        [
            "EQ",
            [
                "length@accounts"
            ],
            [
                "length@ids"
            ],
            "#Medium#ERROR_MSG:ERC1155: accounts and ids length mismatch"
        ],
        [
            "NEQ",
            [
                "account"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC1155: address zero is not a valid owner"
        ]
    ],
    "SafeCast.toUint168(uint256) returns(uint168)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint168)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 168 bits"
        ]
    ],
    "DisableBad2.constructor() returns()": [],
    "SafeCast.toUint160(uint256) returns(uint160)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint160)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 160 bits"
        ]
    ],
    "SafeCast.toUint152(uint256) returns(uint152)": [
        [
            "LTE",
            [
                "value",
                "uint256_1"
            ],
            [
                "max@type()(uint152)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 152 bits"
        ]
    ],
    "EnumerableSet.remove(EnumerableSet.Bytes32Set,bytes32) returns(bool)": [],
    "SafeCast.toUint144(uint256) returns(uint144)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint144)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 144 bits"
        ]
    ],
    "ERC1155._burn(address,uint256,uint256) returns()": [
        [
            "NEQ",
            [
                "from",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC1155: burn from the zero address"
        ],
        [
            "GTE",
            [
                "fromBalance",
                "_balances@element",
                "_balances@id@from"
            ],
            [
                "amount",
                "uint256_2",
                "element"
            ],
            "#Medium#ERROR_MSG:ERC1155: burn amount exceeds balance"
        ]
    ],
    "SafeCast.toUint136(uint256) returns(uint136)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint136)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 136 bits"
        ]
    ],
    "ERC1967Upgrade.slitherConstructorConstantVariables() returns()": [],
    "SampleMother.initialize(uint256) returns()": [
        [
            "initializer"
        ],
        [
            [
                [
                    [
                        "! _initializing",
                        "isTopLevelCall"
                    ],
                    [
                        "LT",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ],
                [
                    [
                        "NOT",
                        [
                            "isContract(address(this))"
                        ]
                    ],
                    [
                        "EQ",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ]
            ],
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ],
        [
            "onlyInitializing"
        ],
        [
            "_initializing",
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "SafeCast.toUint128(uint256) returns(uint128)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint128)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 128 bits"
        ]
    ],
    "SafeCast.toInt96(int256) returns(int96)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "int256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 96 bits"
        ]
    ],
    "GovernorVotesQuorumFraction.slitherConstructorConstantVariables() returns()": [],
    "SafeCast.toUint120(uint256) returns(uint120)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint120)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 120 bits"
        ]
    ],
    "Ownable2Step.pendingOwner() returns(address)": [],
    "GovernorCompatibilityBravo.cancel(address[],uint256[],bytes[],bytes32) returns(uint256)": [
        [
            [
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "proposer@_proposalDetails@encode(targets,values,calldatas,descriptionHash)))",
                        "account",
                        "proposer@_proposalDetails@hashProposal(targets,values,calldatas,descriptionHash)",
                        "proposer",
                        "proposer@_proposalDetails@proposalId"
                    ]
                ],
                [
                    "LT",
                    [
                        "getVotes(proposer,clock() - 1)",
                        "_getVotes(account,timepoint,_defaultParams())"
                    ],
                    [
                        "proposalThreshold()",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:GovernorBravo: proposer above threshold"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Canceled@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Expired@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Executed@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "EQ",
            [
                "0"
            ],
            [
                "proposalSnapshot(proposalId)",
                "REF_1872",
                "voteStart@_proposals@encode(targets,values,calldatas,descriptionHash)))",
                "voteStart@_proposals@proposalId",
                "snapshot",
                "voteStart@_proposals@hashProposal(targets,values,calldatas,descriptionHash)",
                "voteStart@proposal"
            ],
            "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
        ]
    ],
    "SafeCast.toUint112(uint256) returns(uint112)": [
        [
            "LTE",
            [
                "uint256_1",
                "value"
            ],
            [
                "max@type()(uint112)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 112 bits"
        ]
    ],
    "SampleMother.__SampleMother_init(uint256) returns()": [
        [
            "onlyInitializing"
        ],
        [
            "_initializing",
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "ERC1155.isApprovedForAll(address,address) returns(bool)": [],
    "EnumerableMap.get(EnumerableMap.Bytes32ToBytes32Map,bytes32,string) returns(bytes32)": [
        [
            [
                [
                    "NEQ",
                    [
                        "_values@map",
                        "_values@map@value",
                        "value",
                        "_values@map@key"
                    ],
                    [
                        "0"
                    ]
                ],
                [
                    "contains(map,key)",
                    "contains(key)"
                ]
            ],
            "#Low#ERROR_MSG:errorMessage"
        ]
    ],
    "ERC2771ContextMock.constructor(address) returns()": [],
    "MerkleProof.processProof(bytes32[],bytes32) returns(bytes32)": [],
    "EnumerableMap.keys(EnumerableMap.Bytes32ToBytes32Map) returns(bytes32[])": [],
    "ERC2771ContextMock._msgSender() returns(address)": [],
    "MerkleProof.processProofCalldata(bytes32[],bytes32) returns(bytes32)": [],
    "ERC20FlashMint.flashLoan(IERC3156FlashBorrower,address,uint256,bytes) returns(bool)": [
        [
            "LTE",
            [
                "amount",
                "fee",
                "flashFee(token,amount)",
                "uint256_1"
            ],
            [
                "maxFlashLoan(token)"
            ],
            "#High#ERROR_MSG:ERC20FlashMint: amount exceeds maxFlashLoan"
        ],
        [
            "EQ",
            [
                "onFlashLoan(msgsender,token,amount,fee,data)"
            ],
            [
                "onFlashLoan)",
                "_RETURN_VALUE",
                "bytes32"
            ],
            "#High#ERROR_MSG:ERC20FlashMint: invalid return value"
        ],
        [
            "GTE",
            [
                "allowance(owner,spender)",
                "_allowances@owner@spender",
                "currentAllowance"
            ],
            [
                "amount"
            ],
            "#High#ERROR_MSG:ERC20: insufficient allowance"
        ],
        [
            "NEQ",
            [
                "to",
                "account",
                "flashFeeReceiver",
                "_flashFeeReceiver()",
                "address(0)"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: mint to the zero address"
        ],
        [
            "NEQ",
            [
                "from",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: burn from the zero address"
        ],
        [
            "GTE",
            [
                "_balances@from",
                "fromBalance",
                "_balances@account",
                "accountBalance"
            ],
            [
                "amount",
                "fee",
                "flashFee(token,amount)",
                "uint256_1"
            ],
            "#Medium#ERROR_MSG:ERC20: burn amount exceeds balance"
        ],
        [
            "EQ",
            [
                "token",
                "address_1"
            ],
            [
                "address(this)"
            ],
            "#Low#ERROR_MSG:ERC20FlashMint: wrong token"
        ],
        [
            "NEQ",
            [
                "from",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: transfer to the zero address"
        ],
        [
            "NEQ",
            [
                "to",
                "account",
                "flashFeeReceiver",
                "_flashFeeReceiver()",
                "address(0)"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: transfer to the zero address"
        ],
        [
            "GTE",
            [
                "_balances@from",
                "fromBalance",
                "_balances@account",
                "accountBalance"
            ],
            [
                "amount",
                "fee",
                "flashFee(token,amount)",
                "uint256_1"
            ],
            "#Medium#ERROR_MSG:ERC20: transfer amount exceeds balance"
        ],
        [
            "NEQ",
            [
                "owner"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve from the zero address"
        ],
        [
            "NEQ",
            [
                "spender"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: approve to the zero address"
        ]
    ],
    "EnumerableMap.set(EnumerableMap.UintToUintMap,uint256,uint256) returns(bool)": [],
    "ERC2771ContextMock._msgData() returns(bytes)": [],
    "ERC20Pausable._beforeTokenTransfer(address,address,uint256) returns()": [
        [
            "NOT",
            [
                "paused()",
                [
                    "_paused"
                ]
            ],
            "#Medium#ERROR_MSG:ERC20Pausable: token transfer while paused"
        ]
    ],
    "MerkleProof.multiProofVerify(bytes32[],bool[],bytes32,bytes32[]) returns(bool)": [
        [
            "EQ",
            [
                "SUB",
                [
                    "ADD",
                    [
                        "leavesLen",
                        "length@leaves"
                    ],
                    [
                        "proofLen",
                        "length@proof"
                    ]
                ],
                [
                    "1"
                ]
            ],
            [
                "length@proofFlags",
                "totalHashes"
            ],
            "#Medium#ERROR_MSG:MerkleProof: invalid multiproof"
        ],
        [
            "EQ",
            [
                "proofPos"
            ],
            [
                "proofLen",
                "length@proof"
            ],
            "#Medium#ERROR_MSG:MerkleProof: invalid multiproof"
        ]
    ],
    "EnumerableMap.remove(EnumerableMap.UintToUintMap,uint256) returns(bool)": [],
    "InitializableMock.isInitializing() returns(bool)": [],
    "MerkleProof.multiProofVerifyCalldata(bytes32[],bool[],bytes32,bytes32[]) returns(bool)": [
        [
            "EQ",
            [
                "SUB",
                [
                    "ADD",
                    [
                        "length@leaves",
                        "leavesLen"
                    ],
                    [
                        "proofLen",
                        "length@proof"
                    ]
                ],
                [
                    "1"
                ]
            ],
            [
                "length@proofFlags",
                "totalHashes"
            ],
            "#Medium#ERROR_MSG:MerkleProof: invalid multiproof"
        ],
        [
            "EQ",
            [
                "proofPos"
            ],
            [
                "proofLen",
                "length@proof"
            ],
            "#Medium#ERROR_MSG:MerkleProof: invalid multiproof"
        ]
    ],
    "EnumerableMap.contains(EnumerableMap.UintToUintMap,uint256) returns(bool)": [],
    "MerkleProof.processMultiProof(bytes32[],bool[],bytes32[]) returns(bytes32)": [
        [
            "EQ",
            [
                "SUB",
                [
                    "ADD",
                    [
                        "leavesLen",
                        "length@leaves"
                    ],
                    [
                        "proofLen",
                        "length@proof"
                    ]
                ],
                [
                    "1"
                ]
            ],
            [
                "length@proofFlags",
                "totalHashes"
            ],
            "#Medium#ERROR_MSG:MerkleProof: invalid multiproof"
        ],
        [
            "EQ",
            [
                "proofPos"
            ],
            [
                "proofLen",
                "length@proof"
            ],
            "#Medium#ERROR_MSG:MerkleProof: invalid multiproof"
        ]
    ],
    "EnumerableMap.length(EnumerableMap.UintToUintMap) returns(uint256)": [],
    "MerkleProof.processMultiProofCalldata(bytes32[],bool[],bytes32[]) returns(bytes32)": [
        [
            "EQ",
            [
                "SUB",
                [
                    "ADD",
                    [
                        "length@leaves",
                        "leavesLen"
                    ],
                    [
                        "proofLen",
                        "length@proof"
                    ]
                ],
                [
                    "1"
                ]
            ],
            [
                "totalHashes",
                "length@proofFlags"
            ],
            "#Medium#ERROR_MSG:MerkleProof: invalid multiproof"
        ],
        [
            "EQ",
            [
                "proofPos"
            ],
            [
                "proofLen",
                "length@proof"
            ],
            "#Medium#ERROR_MSG:MerkleProof: invalid multiproof"
        ]
    ],
    "InitializableMock.initialize() returns()": [
        [
            "initializer"
        ],
        [
            [
                [
                    [
                        "! _initializing",
                        "isTopLevelCall"
                    ],
                    [
                        "LT",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ],
                [
                    [
                        "NOT",
                        [
                            "isContract(address(this))"
                        ]
                    ],
                    [
                        "EQ",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ]
            ],
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "EnumerableMap.at(EnumerableMap.UintToUintMap,uint256) returns(uint256,uint256)": [],
    "MerkleProof._hashPair(bytes32,bytes32) returns(bytes32)": [],
    "InitializableMock.initializeOnlyInitializing() returns()": [
        [
            "onlyInitializing"
        ],
        [
            "_initializing",
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "EnumerableMap.tryGet(EnumerableMap.UintToUintMap,uint256) returns(bool,uint256)": [],
    "MerkleProof._efficientHash(bytes32,bytes32) returns(bytes32)": [],
    "InitializableMock.initializerNested() returns()": [
        [
            "initializer"
        ],
        [
            [
                [
                    [
                        "! _initializing",
                        "isTopLevelCall"
                    ],
                    [
                        "LT",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ],
                [
                    [
                        "NOT",
                        [
                            "isContract(address(this))"
                        ]
                    ],
                    [
                        "EQ",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ]
            ],
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "SafeCast.toInt80(int256) returns(int80)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "int256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 80 bits"
        ]
    ],
    "EnumerableMap.get(EnumerableMap.UintToUintMap,uint256) returns(uint256)": [
        [
            [
                [
                    "NEQ",
                    [
                        "value",
                        "_values@map",
                        "_values@map@value",
                        "_values@map@key"
                    ],
                    [
                        "0"
                    ]
                ],
                [
                    "contains(map,key)",
                    "contains(key)"
                ]
            ],
            "#Medium#ERROR_MSG:EnumerableMap: nonexistent key"
        ]
    ],
    "CrossChainEnabledOptimismMock.slitherConstructorVariables() returns()": [],
    "SignatureChecker.isValidSignatureNow(address,bytes32,bytes) returns(bool)": [],
    "InitializableMock.onlyInitializingNested() returns()": [
        [
            "initializer"
        ],
        [
            [
                [
                    [
                        "! _initializing",
                        "isTopLevelCall"
                    ],
                    [
                        "LT",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ],
                [
                    [
                        "NOT",
                        [
                            "isContract(address(this))"
                        ]
                    ],
                    [
                        "EQ",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ]
            ],
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ],
        [
            "onlyInitializing"
        ],
        [
            "_initializing",
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "BeaconProxy.constructor(address,bytes) returns()": [],
    "EnumerableMap.get(EnumerableMap.UintToUintMap,uint256,string) returns(uint256)": [
        [
            [
                [
                    "NEQ",
                    [
                        "_values@map",
                        "_values@map@value",
                        "value",
                        "_values@map@key"
                    ],
                    [
                        "0"
                    ]
                ],
                [
                    "contains(map,key)",
                    "contains(key)"
                ]
            ],
            "#Low#ERROR_MSG:errorMessage"
        ]
    ],
    "MyGovernor3.slitherConstructorConstantVariables() returns()": [],
    "SignatureChecker.isValidERC1271SignatureNow(address,bytes32,bytes) returns(bool)": [],
    "GovernorTimelockCompound.slitherConstructorConstantVariables() returns()": [],
    "InitializableMock.initializeWithX(uint256) returns()": [
        [
            "initializer"
        ],
        [
            [
                [
                    [
                        "! _initializing",
                        "isTopLevelCall"
                    ],
                    [
                        "LT",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ],
                [
                    [
                        "NOT",
                        [
                            "isContract(address(this))"
                        ]
                    ],
                    [
                        "EQ",
                        [
                            "_initialized",
                            "uint8"
                        ],
                        [
                            "1"
                        ]
                    ]
                ]
            ],
            "#High#ERROR_MSG:Initializable: contract is not initializing"
        ]
    ],
    "BeaconProxy._beacon() returns(address)": [],
    "EnumerableMap.keys(EnumerableMap.UintToUintMap) returns(uint256[])": [],
    "ERC165Checker.supportsERC165(address) returns(bool)": [],
    "ERC3156FlashBorrowerMock.slitherConstructorConstantVariables() returns()": [],
    "InitializableMock.nonInitializable(uint256) returns()": [],
    "BeaconProxy._implementation() returns(address)": [],
    "EnumerableMap.set(EnumerableMap.UintToAddressMap,uint256,address) returns(bool)": [],
    "GovernorPreventLateQuorum.slitherConstructorConstantVariables() returns()": [],
    "InitializableMock.fail() returns()": [
        [
            "false",
            "#Low#ERROR_MSG:InitializableMock forced failure"
        ]
    ],
    "ERC165Checker.supportsInterface(address,bytes4) returns(bool)": [],
    "MyGovernor2.quorum(uint256) returns(uint256)": [
        [
            "LTE",
            [
                "timepoint",
                "value",
                "uint256_1",
                "blockNumber"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ]
    ],
    "EnumerableMap.get(EnumerableMap.Bytes32ToUintMap,bytes32,string) returns(uint256)": [
        [
            [
                [
                    "NEQ",
                    [
                        "_values@map",
                        "_values@map@value",
                        "value",
                        "_values@map@key"
                    ],
                    [
                        "0"
                    ]
                ],
                [
                    "contains(map,key)",
                    "contains(key)"
                ]
            ],
            "#Low#ERROR_MSG:errorMessage"
        ]
    ],
    "ERC1155Supply.exists(uint256) returns(bool)": [],
    "SafeCast.toInt168(int256) returns(int168)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "int256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 168 bits"
        ]
    ],
    "MyGovernor.cancel(address[],uint256[],bytes[],bytes32) returns(uint256)": [
        [
            [
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "proposer@_proposalDetails@proposalId",
                        "proposer@_proposalDetails@hashProposal(targets,values,calldatas,descriptionHash)",
                        "account",
                        "proposer@_proposalDetails@encode(targets,values,calldatas,descriptionHash)))",
                        "proposer",
                        "proposer@details"
                    ]
                ],
                [
                    "LT",
                    [
                        "getVotes(proposer,clock() - 1)",
                        "_getVotes(account,timepoint,_defaultParams())"
                    ],
                    [
                        "proposalThreshold()",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:GovernorBravo: proposer above threshold"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Canceled@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Expired@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Executed@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ]
    ],
    "MulticallTest.checkReturnValues(ERC20MulticallMock,address[],uint256[]) returns()": [
        [
            [
                "decode(results[i_scope_0],(bool))"
            ],
            "#Low#ERROR_MSG:None"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "GovernorCompatibilityBravoMock.supportsInterface(bytes4) returns(bool)": [],
    "EnumerableMap.keys(EnumerableMap.Bytes32ToUintMap) returns(bytes32[])": [],
    "MyGovernor2.state(uint256) returns(IGovernor.ProposalState)": [],
    "ERC1155Supply._beforeTokenTransfer(address,address,address,uint256[],uint256[],bytes) returns()": [
        [
            "GTE",
            [
                "supply",
                "_totalSupply@ids@i_scope_0",
                "_totalSupply@ids",
                "_totalSupply@id"
            ],
            [
                "amount",
                "amounts",
                "amounts@i_scope_0"
            ],
            "#Medium#ERROR_MSG:ERC1155: burn amount exceeds totalSupply"
        ]
    ],
    "SafeCast.toInt160(int256) returns(int160)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "value",
                "int256_1"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 160 bits"
        ]
    ],
    "MyGovernor._execute(uint256,address[],uint256[],bytes[],bytes32) returns()": [
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@values"
            ],
            "#Medium#ERROR_MSG:TimelockController: length mismatch"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@payloads"
            ],
            "#Medium#ERROR_MSG:TimelockController: length mismatch"
        ],
        [
            "onlyRoleOrOpenRole"
        ],
        [
            [
                "isOperationReady(id)"
            ],
            "#Medium#ERROR_MSG:TimelockController: operation is not ready"
        ],
        [
            [
                [
                    "EQ",
                    [
                        "predecessor",
                        "hashOperationBatch(targets,values,payloads,predecessor,salt)",
                        "0",
                        "id",
                        "encode(targets,values,payloads,predecessor,salt))"
                    ],
                    [
                        "bytes32(0)"
                    ]
                ],
                [
                    "isOperationDone(predecessor)",
                    [
                        "EQ",
                        [
                            "getTimestamp(id)",
                            [
                                "_timestamps@id",
                                "_timestamps@0",
                                "_timestamps@predecessor",
                                "_timestamps@hashOperationBatch(targets,values,payloads,predecessor,salt)",
                                "_timestamps@encode(targets,values,payloads,predecessor,salt))",
                                "timestamp",
                                "getTimestamp(id)"
                            ]
                        ],
                        [
                            "_DONE_TIMESTAMP",
                            "uint256(1)",
                            "uint256"
                        ]
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:TimelockController: missing dependency"
        ],
        [
            "success",
            "#Medium#ERROR_MSG:TimelockController: underlying transaction reverted"
        ]
    ],
    "StorageSlotMock.setBoolean(bytes32,bool) returns()": [],
    "GovernorCompatibilityBravoMock.state(uint256) returns(IGovernor.ProposalState)": [],
    "Strings.toString(uint256) returns(string)": [],
    "MyGovernor2.propose(address[],uint256[],bytes[],string) returns(uint256)": [
        [
            [
                "_isValidDescriptionForProposer(proposer,description)"
            ],
            "#High#ERROR_MSG:Governor: proposer restricted"
        ],
        [
            "GTE",
            [
                "getVotes(proposer,currentTimepoint - 1)",
                "_getVotes(account,timepoint,_defaultParams())"
            ],
            [
                "proposalThreshold()",
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: proposer votes below proposal threshold"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@values"
            ],
            "#Medium#ERROR_MSG:Governor: invalid proposal length"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@calldatas"
            ],
            "#Medium#ERROR_MSG:Governor: invalid proposal length"
        ],
        [
            "GT",
            [
                "length@targets"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: empty proposal"
        ],
        [
            "EQ",
            [
                "voteStart@_proposals@hashProposal(targets,values,calldatas,keccak256(bytes)(bytes(description)))",
                "voteStart@_proposals@encode(targets,values,calldatas,descriptionHash)))",
                "voteStart@_proposals@proposalId"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: proposal already exists"
        ],
        [
            "LTE",
            [
                "value",
                "snapshot",
                "deadline",
                "snapshot + votingPeriod()",
                "currentTimepoint + votingDelay()"
            ],
            [
                "max@type()(uint64)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 64 bits"
        ]
    ],
    "ERC1155URIStorage.uri(uint256) returns(string)": [],
    "Strings.toString(int256) returns(string)": [],
    "SafeCast.toInt152(int256) returns(int152)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "int256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 152 bits"
        ]
    ],
    "MyGovernor._cancel(address[],uint256[],bytes[],bytes32) returns(uint256)": [
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Canceled@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Expired@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Executed@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            [
                "isOperationPending(id)",
                [
                    "GT",
                    [
                        "getTimestamp(id)",
                        [
                            "_timestamps@id"
                        ]
                    ],
                    [
                        "_DONE_TIMESTAMP",
                        "uint256(1)",
                        "uint256"
                    ]
                ]
            ],
            "#High#ERROR_MSG:TimelockController: operation cannot be cancelled"
        ],
        [
            [
                "onlyRole",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ]
    ],
    "GovernorCompatibilityBravoMock.proposalEta(uint256) returns(uint256)": [],
    "MyGovernor2._execute(uint256,address[],uint256[],bytes[],bytes32) returns()": [
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@values"
            ],
            "#Medium#ERROR_MSG:TimelockController: length mismatch"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@payloads"
            ],
            "#Medium#ERROR_MSG:TimelockController: length mismatch"
        ],
        [
            "onlyRoleOrOpenRole"
        ],
        [
            [
                "isOperationReady(id)"
            ],
            "#Medium#ERROR_MSG:TimelockController: operation is not ready"
        ],
        [
            [
                [
                    "EQ",
                    [
                        "predecessor",
                        "hashOperationBatch(targets,values,payloads,predecessor,salt)",
                        "0",
                        "id",
                        "encode(targets,values,payloads,predecessor,salt))"
                    ],
                    [
                        "bytes32(0)"
                    ]
                ],
                [
                    "isOperationDone(predecessor)",
                    [
                        "EQ",
                        [
                            "getTimestamp(id)",
                            [
                                "_timestamps@id",
                                "_timestamps@0",
                                "_timestamps@predecessor",
                                "_timestamps@hashOperationBatch(targets,values,payloads,predecessor,salt)",
                                "_timestamps@encode(targets,values,payloads,predecessor,salt))",
                                "timestamp",
                                "getTimestamp(id)"
                            ]
                        ],
                        [
                            "_DONE_TIMESTAMP",
                            "uint256(1)",
                            "uint256"
                        ]
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:TimelockController: missing dependency"
        ],
        [
            "success",
            "#Medium#ERROR_MSG:TimelockController: underlying transaction reverted"
        ]
    ],
    "Strings.toHexString(uint256) returns(string)": [
        [
            "EQ",
            [
                "Strings.toHexString(uint256,uint256).value",
                "value",
                "uint256_1"
            ],
            [
                "0"
            ],
            "#Meidum#ERROR_MSG:Strings: hex length insufficient"
        ]
    ],
    "SafeCast.toInt144(int256) returns(int144)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "value",
                "int256_1"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 144 bits"
        ]
    ],
    "StorageSlotMock.setAddress(bytes32,address) returns()": [],
    "MyGovernor._executor() returns(address)": [],
    "GovernorCompatibilityBravoMock.proposalThreshold() returns(uint256)": [],
    "MyGovernor2._cancel(address[],uint256[],bytes[],bytes32) returns(uint256)": [
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Canceled@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Expired@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Executed@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            [
                "isOperationPending(id)",
                [
                    "GT",
                    [
                        "getTimestamp(id)",
                        [
                            "_timestamps@id"
                        ]
                    ],
                    [
                        "_DONE_TIMESTAMP",
                        "uint256(1)",
                        "uint256"
                    ]
                ]
            ],
            "#High#ERROR_MSG:TimelockController: operation cannot be cancelled"
        ],
        [
            [
                "onlyRole",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ]
    ],
    "EnumerableSet._add(EnumerableSet.Set,bytes32) returns(bool)": [],
    "ERC1155URIStorage._setURI(uint256,string) returns()": [],
    "SafeCast.toInt136(int256) returns(int136)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "int256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 136 bits"
        ]
    ],
    "StorageSlotMock.setBytes32(bytes32,bytes32) returns()": [],
    "MyGovernor.supportsInterface(bytes4) returns(bool)": [],
    "Strings.toHexString(uint256,uint256) returns(string)": [
        [
            "EQ",
            [
                "uint256_1",
                "Strings.toHexString(uint256,uint256).value"
            ],
            [
                "0"
            ],
            "#Meidum#ERROR_MSG:Strings: hex length insufficient"
        ]
    ],
    "GovernorCompatibilityBravoMock.propose(address[],uint256[],bytes[],string) returns(uint256)": [
        [
            [
                "_isValidDescriptionForProposer(proposer,description)"
            ],
            "#High#ERROR_MSG:Governor: proposer restricted"
        ],
        [
            "GTE",
            [
                "getVotes(proposer,currentTimepoint - 1)",
                "_getVotes(account,timepoint,_defaultParams())"
            ],
            [
                "proposalThreshold()",
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: proposer votes below proposal threshold"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@values"
            ],
            "#Medium#ERROR_MSG:Governor: invalid proposal length"
        ],
        [
            "EQ",
            [
                "length@targets"
            ],
            [
                "length@calldatas"
            ],
            "#Medium#ERROR_MSG:Governor: invalid proposal length"
        ],
        [
            "GT",
            [
                "length@targets"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: empty proposal"
        ],
        [
            "EQ",
            [
                "voteStart@_proposals@hashProposal(targets,values,calldatas,keccak256(bytes)(bytes(description)))",
                "voteStart@_proposals@encode(targets,values,calldatas,descriptionHash)))",
                "voteStart@_proposals@proposalId"
            ],
            [
                "0"
            ],
            "#Medium#ERROR_MSG:Governor: proposal already exists"
        ],
        [
            "LTE",
            [
                "value",
                "snapshot",
                "deadline",
                "snapshot + votingPeriod()",
                "currentTimepoint + votingDelay()"
            ],
            [
                "max@type()(uint64)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 64 bits"
        ]
    ],
    "MyGovernor2._executor() returns(address)": [],
    "EnumerableSet._remove(EnumerableSet.Set,bytes32) returns(bool)": [],
    "VotesMock.delegate(address,address) returns()": [
        [
            "LTE",
            [
                "value",
                "amount"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ],
        [
            "LTE",
            [
                "_key@_unsafeAccess(self,pos - 1)",
                "_key@last"
            ],
            [
                "key"
            ],
            "#Medium#ERROR_MSG:Checkpoint: decreasing keys"
        ]
    ],
    "ERC1155URIStorage._setBaseURI(string) returns()": [],
    "StorageSlotMock.setUint256(bytes32,uint256) returns()": [],
    "MyToken.constructor() returns()": [],
    "Strings.toHexString(address) returns(string)": [
        [
            "EQ",
            [
                "Strings.toHexString(uint256,uint256).value"
            ],
            [
                "0"
            ],
            "#Meidum#ERROR_MSG:Strings: hex length insufficient"
        ]
    ],
    "SafeCast.toInt128(int256) returns(int128)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "int256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 128 bits"
        ]
    ],
    "GovernorCompatibilityBravoMock.queue(address[],uint256[],bytes[],bytes32) returns(uint256)": [
        [
            "EQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Succeeded@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not successful"
        ],
        [
            "NOT",
            [
                "encode(targets[i],values[i],,calldatas[i],eta)))"
            ],
            "#Low#ERROR_MSG:GovernorTimelockCompound: identical proposal action already queued"
        ],
        [
            "LTE",
            [
                "eta",
                "value",
                "delay()"
            ],
            [
                "max@type()(uint64)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 64 bits"
        ]
    ],
    "MyGovernor2.supportsInterface(bytes4) returns(bool)": [],
    "EnumerableSet._contains(EnumerableSet.Set,bytes32) returns(bool)": [],
    "ERC1155PresetMinterPauser.constructor(string) returns()": [],
    "SafeCast.toInt120(int256) returns(int120)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "int256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 120 bits"
        ]
    ],
    "StorageSlotMock.getBoolean(bytes32) returns(bool)": [],
    "Strings.equal(string,string) returns(bool)": [],
    "MyToken._afterTokenTransfer(address,address,uint256) returns()": [
        [
            "LTE",
            [
                "value",
                "newWeight"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "GovernorCompatibilityBravoMock.execute(address[],uint256[],bytes[],bytes32) returns(uint256)": [
        [
            [
                [
                    "EQ",
                    [
                        "state(proposalId)",
                        "currentState"
                    ],
                    [
                        "Succeeded@ProposalState"
                    ]
                ],
                [
                    "EQ",
                    [
                        "state(proposalId)",
                        "currentState"
                    ],
                    [
                        "Queued@ProposalState"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Governor: proposal not successful"
        ]
    ],
    "MyGovernor3.constructor(IVotes,TimelockController) returns()": [],
    "StorageSlotMock.getAddress(bytes32) returns(address)": [],
    "SafeCast.toInt112(int256) returns(int112)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "int256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 112 bits"
        ]
    ],
    "MyToken._mint(address,uint256) returns()": [
        [
            "LTE",
            [
                "totalSupply()",
                [
                    "_totalSupply"
                ]
            ],
            [
                "_maxSupply()",
                "max@type()(uint224)"
            ],
            "#Medium#ERROR_MSG:ERC20Votes: total supply risks overflowing votes"
        ],
        [
            "NEQ",
            [
                "to",
                "account",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: mint to the zero address"
        ],
        [
            "LTE",
            [
                "value",
                "newWeight"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "GovernorCompatibilityBravoMock.cancel(address[],uint256[],bytes[],bytes32) returns(uint256)": [
        [
            [
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "proposer@_proposalDetails@_cancel(targets,values,calldatas,descriptionHash)",
                        "proposer@_proposalDetails@proposalId",
                        "account",
                        "proposer@_proposalDetails@hashProposal(targets,values,calldatas,descriptionHash)",
                        "proposer@_proposalDetails@encode(targets,values,calldatas,descriptionHash)))",
                        "proposer",
                        "proposer@details"
                    ]
                ],
                [
                    "LT",
                    [
                        "getVotes(proposer,clock() - 1)",
                        "_getVotes(account,timepoint,_defaultParams())"
                    ],
                    [
                        "proposalThreshold()"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:GovernorBravo: proposer above threshold"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Canceled@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Expired@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Executed@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ]
    ],
    "MyGovernor3.votingDelay() returns(uint256)": [],
    "EnumerableSet._at(EnumerableSet.Set,uint256) returns(bytes32)": [],
    "ERC1155PresetMinterPauser.mint(address,uint256,uint256,bytes) returns()": [
        [
            [
                "hasRole(MINTER_ROLE,_msgSender())",
                [
                    "members@_roles@role@account"
                ],
                "onlyRole",
                [
                    "EQ",
                    [
                        "msgsender",
                        "_msgSender()"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth",
                        "gov"
                    ]
                ]
            ],
            "#High#ERROR_MSG:ERC1155PresetMinterPauser: must have minter role to mint"
        ],
        [
            "NEQ",
            [
                "to",
                "address_1",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC1155: mint to the zero address"
        ],
        [
            "NEQ",
            [
                "selector@onERC1155Received@IERC1155Receiver"
            ],
            [
                "response"
            ],
            "#High#ERROR_MSG:(ERC1155: ERC1155Receiver rejected tokens)"
        ]
    ],
    "StorageSlotMock.getBytes32(bytes32) returns(bytes32)": [],
    "MyToken._burn(address,uint256) returns()": [
        [
            "NEQ",
            [
                "from",
                "account",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC20: burn from the zero address"
        ],
        [
            "GTE",
            [
                "_balances@from",
                "_balances@account",
                "accountBalance"
            ],
            [
                "amount",
                "delta",
                "uint256_1"
            ],
            "#Medium#ERROR_MSG:ERC20: burn amount exceeds balance"
        ],
        [
            "LTE",
            [
                "value",
                "newWeight"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "Timers.getDeadline(Timers.Timestamp) returns(uint64)": [],
    "SafeCast.toInt104(int256) returns(int104)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "int256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 104 bits"
        ]
    ],
    "GovernorCompatibilityBravoMock._execute(uint256,address[],uint256[],bytes[],bytes32) returns()": [
        [
            "GT",
            [
                "proposalEta(proposalId)",
                "eta"
            ],
            [
                "0"
            ],
            "#Low#ERROR_MSG:GovernorTimelockCompound: proposal not yet queued"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "amount"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance"
        ],
        [
            "success",
            "#Low#ERROR_MSG:Address: unable to send value, recipient may have reverted"
        ]
    ],
    "MyGovernor3.votingPeriod() returns(uint256)": [],
    "EnumerableSet._values(EnumerableSet.Set) returns(bytes32[])": [],
    "StorageSlotMock.getUint256(bytes32) returns(uint256)": [],
    "MyTokenTimestampBased.constructor() returns()": [],
    "ERC1155PresetMinterPauser.mintBatch(address,uint256[],uint256[],bytes) returns()": [
        [
            [
                "hasRole(MINTER_ROLE,_msgSender())",
                [
                    "members@_roles@role@account"
                ],
                "onlyRole",
                [
                    "EQ",
                    [
                        "msgsender",
                        "_msgSender()"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth",
                        "gov"
                    ]
                ]
            ],
            "#High#ERROR_MSG:ERC1155PresetMinterPauser: must have minter role to mint"
        ],
        [
            "NEQ",
            [
                "to",
                "address_1",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC1155: mint to the zero address"
        ],
        [
            "EQ",
            [
                "length@ids"
            ],
            [
                "length@amounts"
            ],
            "#Low#ERROR_MSG:ERC1155: ids and amounts length mismatch"
        ],
        [
            "NEQ",
            [
                "selector@onERC1155BatchReceived@IERC1155Receiver"
            ],
            [
                "response"
            ],
            "#Medium#ERROR_MSG:(ERC1155: ERC1155Receiver rejected tokens)"
        ]
    ],
    "Timers.setDeadline(Timers.Timestamp,uint64) returns()": [],
    "VotesMock._mint(address,uint256) returns()": [
        [
            "LTE",
            [
                "value",
                "amount",
                "1"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ],
        [
            "LTE",
            [
                "_key@_unsafeAccess(self,pos - 1)",
                "_key@last"
            ],
            [
                "key"
            ],
            "#Medium#ERROR_MSG:Checkpoint: decreasing keys"
        ]
    ],
    "GovernorCompatibilityBravoMock._cancel(address[],uint256[],bytes[],bytes32) returns(uint256)": [
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Canceled@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Expired@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ],
        [
            "NEQ",
            [
                "state(proposalId)",
                "currentState"
            ],
            [
                "Executed@ProposalState"
            ],
            "#Medium#ERROR_MSG:Governor: proposal not active"
        ]
    ],
    "MyGovernor3.proposalThreshold() returns(uint256)": [],
    "EnumerableSet.add(EnumerableSet.Bytes32Set,bytes32) returns(bool)": [],
    "SafeCast.toInt88(int256) returns(int88)": [
        [
            "EQ",
            [
                "downcasted"
            ],
            [
                "int256_1",
                "value"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 88 bits"
        ]
    ],
    "StorageSlotMock.setString(bytes32,string) returns()": [],
    "CrossChainEnabledPolygonChildMock.slitherConstructorVariables() returns()": [],
    "MyTokenTimestampBased.clock() returns(uint48)": [],
    "MyGovernor1.slitherConstructorConstantVariables() returns()": [],
    "ERC1155PresetMinterPauser.pause() returns()": [
        [
            [
                "hasRole(PAUSER_ROLE,_msgSender())",
                [
                    "members@_roles@role@account"
                ],
                "onlyRole",
                [
                    "EQ",
                    [
                        "msgsender",
                        "_msgSender()"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth",
                        "gov"
                    ]
                ]
            ],
            "#High#ERROR_MSG:ERC1155PresetMinterPauser: must have pauser role to pause"
        ],
        [
            "whenNotPaused"
        ]
    ],
    "Timers.reset(Timers.Timestamp) returns()": [],
    "GovernorCompatibilityBravoMock._executor() returns(address)": [],
    "MyGovernor3.quorum(uint256) returns(uint256)": [
        [
            "LTE",
            [
                "timepoint",
                "value",
                "uint256_1",
                "blockNumber"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ]
    ],
    "StorageSlotMock.setStringStorage(uint256,string) returns()": [],
    "MyTokenTimestampBased.CLOCK_MODE() returns(string)": [],
    "ERC1155PresetMinterPauser.unpause() returns()": [
        [
            [
                "hasRole(PAUSER_ROLE,_msgSender())",
                [
                    "members@_roles@role@account"
                ],
                "onlyrole",
                [
                    "EQ",
                    [
                        "msgsender",
                        "_msgSender()"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth",
                        "gov"
                    ]
                ]
            ],
            "#High#ERROR_MSG:ERC1155PresetMinterPauser: must have pauser role to unpause"
        ],
        [
            "whenPaused"
        ]
    ],
    "Timers.isUnset(Timers.Timestamp) returns(bool)": [],
    "RefundEscrow.constructor(address) returns()": [],
    "VotesMock._getVotingUnits(address) returns(uint256)": [],
    "ConditionalEscrowMock.setAllowed(address,bool) returns()": [],
    "ERC2771Context.isTrustedForwarder(address) returns(bool)": [],
    "RefundEscrow.state() returns(RefundEscrow.State)": [],
    "ConditionalEscrowMock.withdrawalAllowed(address) returns(bool)": [],
    "VotesMock._burn(uint256) returns()": [
        [
            "LTE",
            [
                "value",
                "amount",
                "1"
            ],
            [
                "max@type()(uint224)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 224 bits"
        ],
        [
            "LTE",
            [
                "value"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ],
        [
            "LTE",
            [
                "value",
                "number"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ],
        [
            "LTE",
            [
                "_key@_unsafeAccess(self,pos - 1)",
                "_key@last"
            ],
            [
                "key"
            ],
            "#Medium#ERROR_MSG:Checkpoint: decreasing keys"
        ]
    ],
    "TimelockController.constructor(uint256,address[],address[],address) returns()": [],
    "RefundEscrow.beneficiary() returns(address)": [],
    "ERC721ConsecutiveEnumerableMock.constructor(string,string,address[],uint96[]) returns()": [],
    "CompTimelock.slitherConstructorConstantVariables() returns()": [],
    "VotesTimestampMock.clock() returns(uint48)": [],
    "TimelockController.receive() returns()": [],
    "RefundEscrow.deposit(address) returns()": [
        [
            "EQ",
            [
                "state()",
                [
                    "_state"
                ]
            ],
            [
                "Active@State"
            ],
            "#Medium#ERROR_MSG:RefundEscrow: can only deposit while active"
        ],
        [
            [
                "onlyOwner",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ]
    ],
    "ERC721ConsecutiveEnumerableMock.supportsInterface(bytes4) returns(bool)": [],
    "Governor.onlyGovernance() returns()": [
        [
            "EQ",
            [
                "_msgSender()",
                "msgsender"
            ],
            [
                "_executor()",
                "address(this)"
            ],
            "#High#ERROR_MSG:Governor: onlyGovernance"
        ]
    ],
    "VotesTimestampMock.CLOCK_MODE() returns(string)": [],
    "TimelockController.supportsInterface(bytes4) returns(bool)": [],
    "RefundEscrow.close() returns()": [
        [
            "EQ",
            [
                "state()",
                [
                    "_state"
                ]
            ],
            [
                "Active@State"
            ],
            "#Medium#ERROR_MSG:RefundEscrow: can only close while active"
        ],
        [
            [
                "onlyOwner",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ]
    ],
    "ERC721ConsecutiveEnumerableMock._ownerOf(uint256) returns(address)": [],
    "ERC2771Context._msgData() returns(bytes)": [],
    "ERC4626Fees.previewDeposit(uint256) returns(uint256)": [
        [
            "GT",
            [
                "denominator"
            ],
            [
                "prod1"
            ],
            "#Medium#ERROR_MSG:Math: mulDiv overflow"
        ]
    ],
    "TimelockController.isOperation(bytes32) returns(bool)": [],
    "RefundEscrow.enableRefunds() returns()": [
        [
            "EQ",
            [
                "state()",
                [
                    "_state"
                ]
            ],
            [
                "Active@State"
            ],
            "#Medium#ERROR_MSG:RefundEscrow: can only enable refunds while active"
        ],
        [
            [
                "onlyOwner",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ]
    ],
    "ERC721ConsecutiveEnumerableMock._mint(address,uint256) returns()": [
        [
            [
                "isContract(address(this))"
            ],
            "#Medium#ERROR_MSG:ERC721Consecutive: can't mint during construction"
        ],
        [
            "NEQ",
            [
                "to",
                "address_1",
                "from",
                "owner"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: mint to the zero address"
        ],
        [
            "NOT",
            [
                "_exists(tokenId)",
                [
                    "NEQ",
                    [
                        "_ownerOf(tokenId)"
                    ],
                    [
                        "address(0)"
                    ]
                ]
            ],
            "#Low#ERROR_MSG:ERC721: token already minted"
        ]
    ],
    "TimelockController.isOperationPending(bytes32) returns(bool)": [],
    "ERC721ConsecutiveEnumerableMock._beforeTokenTransfer(address,address,uint256,uint256) returns()": [
        [
            "NEQ",
            [
                "to",
                "address_1",
                "from",
                "owner",
                "address_2"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC721: address zero is not a valid owner"
        ]
    ],
    "RefundEscrow.beneficiaryWithdraw() returns()": [
        [
            "EQ",
            [
                "state()",
                [
                    "_state"
                ]
            ],
            [
                "Closed@State"
            ],
            "#Medium#ERROR_MSG:RefundEscrow: beneficiary can only withdraw while closed"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "amount"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance"
        ],
        [
            "success",
            "#Low#ERROR_MSG:Address: unable to send value, recipient may have reverted"
        ]
    ],
    "ERC4626Fees.previewWithdraw(uint256) returns(uint256)": [
        [
            "GT",
            [
                "denominator",
                "100000"
            ],
            [
                "prod1"
            ],
            "#Medium#ERROR_MSG:Math: mulDiv overflow"
        ]
    ],
    "TimelockController.isOperationReady(bytes32) returns(bool)": [],
    "IAccessControlEnumerable.getRoleMember(bytes32,uint256) returns(address)": [],
    "ERC721ConsecutiveEnumerableMock._afterTokenTransfer(address,address,uint256,uint256) returns()": [
        [
            "EQ",
            [
                "batchSize",
                "uint256_2"
            ],
            [
                "1"
            ],
            "#Low#ERROR_MSG:ERC721Consecutive: batch burn not supported"
        ]
    ],
    "RefundEscrow.withdrawalAllowed(address) returns(bool)": [],
    "TimelockController.isOperationDone(bytes32) returns(bool)": [],
    "ERC721ConsecutiveMock.constructor(string,string,address[],address[],uint96[]) returns()": [],
    "ERC4626Fees._deposit(address,address,uint256,uint256) returns()": [
        [
            "NEQ",
            [
                "receiver",
                "address_2",
                "to",
                "account"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC20: mint to the zero address"
        ],
        [
            [
                [
                    "EQ",
                    [
                        "length@functionCall(data,SafeERC20: low-level call failed)",
                        "length@returndata"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ],
                [
                    "decode(returndata,(bool))"
                ]
            ],
            "#Medium#ERROR_MSG:SafeERC20: ERC20 operation did not succeed"
        ],
        [
            "GT",
            [
                "denominator"
            ],
            [
                "prod1"
            ],
            "#Medium#ERROR_MSG:Math: mulDiv overflow"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "TimelockController.getTimestamp(bytes32) returns(uint256)": [],
    "CrossChainEnabledAMB.constructor(address) returns()": [],
    "ERC721ConsecutiveMock._ownerOf(uint256) returns(address)": [],
    "TimelockController.getMinDelay() returns(uint256)": [],
    "SignedMath.max(int256,int256) returns(int256)": [],
    "ERC777SenderRecipientMock.registerRecipient(address) returns()": [],
    "SignedMath.min(int256,int256) returns(int256)": [],
    "ERC777SenderRecipientMock.setShouldRevertSend(bool) returns()": [],
    "SignedMath.average(int256,int256) returns(int256)": [],
    "ERC777SenderRecipientMock.setShouldRevertReceive(bool) returns()": [],
    "UUPSUpgradeable.slitherConstructorConstantVariables() returns()": [],
    "IAccessControlDefaultAdminRules.defaultAdmin() returns(address)": [],
    "ERC777SenderRecipientMock.send(IERC777,address,uint256,bytes) returns()": [],
    "SignedMath.abs(int256) returns(uint256)": [],
    "ERC777SenderRecipientMock.burn(IERC777,uint256,bytes) returns()": [],
    "SignedSafeMath.mul(int256,int256) returns(int256)": [],
    "ERC20VotesTimestampMock.clock() returns(uint48)": [
        [
            "LTE",
            [
                "value",
                "timestamp"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "SignedSafeMath.div(int256,int256) returns(int256)": [],
    "ERC20VotesTimestampMock.CLOCK_MODE() returns(string)": [],
    "SignedSafeMath.sub(int256,int256) returns(int256)": [],
    "IAccessControlDefaultAdminRules.defaultAdminDelay() returns(uint48)": [],
    "ERC20VotesCompTimestampMock.clock() returns(uint48)": [
        [
            "LTE",
            [
                "value",
                "timestamp"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "SignedSafeMath.add(int256,int256) returns(int256)": [],
    "ERC20VotesCompTimestampMock.CLOCK_MODE() returns(string)": [],
    "BitMaps.get(BitMaps.BitMap,uint256) returns(bool)": [],
    "MyGovernor1.constructor(IVotes,TimelockController) returns()": [],
    "CrossChainEnabledArbitrumL1Mock.slitherConstructorVariables() returns()": [],
    "BitMaps.setTo(BitMaps.BitMap,uint256,bool) returns()": [],
    "MyGovernor1.votingDelay() returns(uint256)": [],
    "BitMaps.set(BitMaps.BitMap,uint256) returns()": [],
    "MyGovernor1.votingPeriod() returns(uint256)": [],
    "ERC777.balanceOf(address) returns(uint256)": [],
    "Pausable.whenNotPaused() returns()": [],
    "AccessControlDefaultAdminRules._revokeRole(bytes32,address) returns()": [],
    "Checkpoints.upperLookupRecent(Checkpoints.Trace160,uint96) returns(uint160)": [],
    "AccessControlDefaultAdminRules._setRoleAdmin(bytes32,bytes32) returns()": [
        [
            "NEQ",
            [
                "role",
                "bytes32_1"
            ],
            [
                "DEFAULT_ADMIN_ROLE",
                "0x00",
                "bytes32"
            ],
            "#Medium#ERROR_MSG:AccessControl: can't violate default admin rules"
        ]
    ],
    "Checkpoints.latest(Checkpoints.Trace160) returns(uint160)": [],
    "ERC777.transfer(address,uint256) returns(bool)": [
        [
            "NEQ",
            [
                "to",
                "account",
                "from",
                "recipient",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC777: transfer from the zero address"
        ],
        [
            "NEQ",
            [
                "to",
                "account",
                "from",
                "recipient",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC777: transfer to the zero address"
        ],
        [
            "NOT",
            [
                "isContract()"
            ],
            "#Medium#ERROR_MSG:ERC777: token recipient contract has no implementer for ERC777TokensRecipient"
        ],
        [
            "GTE",
            [
                "_balances@recipient",
                "_balances@to",
                "_balances@from",
                "fromBalance",
                "_balances@account"
            ],
            [
                "amount",
                "uint256_1"
            ],
            "#Medium#ERROR_MSG:ERC777: transfer amount exceeds balance"
        ]
    ],
    "Checkpoints.latestCheckpoint(Checkpoints.Trace160) returns(bool,uint96,uint160)": [],
    "AccessControlDefaultAdminRules.defaultAdmin() returns(address)": [],
    "Checkpoints.length(Checkpoints.Trace160) returns(uint256)": [],
    "AccessControlDefaultAdminRules.pendingDefaultAdmin() returns(address,uint48)": [],
    "ERC777.isOperatorFor(address,address) returns(bool)": [],
    "ERC777SenderRecipientMock.slitherConstructorVariables() returns()": [],
    "Checkpoints._insert(Checkpoints.Checkpoint160[],uint96,uint160) returns(uint160,uint160)": [
        [
            "LTE",
            [
                "_key@_unsafeAccess(self,pos - 1)",
                "_key@last"
            ],
            [
                "uint96_1",
                "key"
            ],
            "#Medium#ERROR_MSG:Checkpoint: decreasing keys"
        ]
    ],
    "AccessControlDefaultAdminRules.defaultAdminDelay() returns(uint48)": [],
    "ERC165Storage.supportsInterface(bytes4) returns(bool)": [],
    "Checkpoints._upperBinaryLookup(Checkpoints.Checkpoint160[],uint96,uint256,uint256) returns(uint256)": [],
    "AccessControlDefaultAdminRules.pendingDefaultAdminDelay() returns(uint48,uint48)": [],
    "ERC777.revokeOperator(address) returns()": [
        [
            "NEQ",
            [
                "operator",
                "address_1"
            ],
            [
                "_msgSender()",
                "msgsender"
            ],
            "#Low#ERROR_MSG:ERC777: revoking self as operator"
        ]
    ],
    "ERC777SenderRecipientMock.slitherConstructorConstantVariables() returns()": [],
    "Checkpoints._lowerBinaryLookup(Checkpoints.Checkpoint160[],uint96,uint256,uint256) returns(uint256)": [],
    "AccessControlDefaultAdminRules.defaultAdminDelayIncreaseWait() returns(uint48)": [],
    "ERC165Storage._registerInterface(bytes4) returns()": [
        [
            "NEQ",
            [
                "interfaceId",
                "bytes4_1"
            ],
            [
                "0xffffffff"
            ],
            "#Low#ERROR_MSG:ERC165: invalid interface id"
        ]
    ],
    "ERC2771Context.constructor(address) returns()": [],
    "Checkpoints._unsafeAccess(Checkpoints.Checkpoint160[],uint256) returns(Checkpoints.Checkpoint160)": [],
    "AccessControlDefaultAdminRules.beginDefaultAdminTransfer(address) returns()": [
        [
            [
                "onlyRole",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ],
        [
            "LTE",
            [
                "value",
                "timestamp"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "ERC1820Implementer.canImplementInterfaceForAddress(bytes32,address) returns(bytes32)": [],
    "ERC777.operatorSend(address,address,uint256,bytes,bytes) returns()": [
        [
            [
                "isOperatorFor(_msgSender(),sender)",
                [
                    [
                        [
                            [
                                [
                                    "EQ",
                                    [
                                        "operator"
                                    ],
                                    [
                                        "from",
                                        "to",
                                        "tokenHolder",
                                        "account",
                                        "recipient",
                                        "address_2",
                                        "sender",
                                        "address_1"
                                    ]
                                ],
                                [
                                    [
                                        [
                                            "_defaultOperators@operator"
                                        ],
                                        [
                                            "NOT",
                                            [
                                                "_revokedDefaultOperators@tokenHolder@operator"
                                            ]
                                        ]
                                    ]
                                ]
                            ]
                        ],
                        [
                            "_operators@tokenHolder@operator"
                        ]
                    ]
                ]
            ],
            "#High#ERROR_MSG:ERC777: caller is not an operator for holder"
        ],
        [
            "NEQ",
            [
                "from",
                "to",
                "tokenHolder",
                "account",
                "recipient",
                "address_2",
                "sender",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Low#ERROR_MSG:ERC777: transfer from the zero address"
        ],
        [
            "NEQ",
            [
                "from",
                "to",
                "tokenHolder",
                "account",
                "recipient",
                "address_2",
                "sender",
                "address_1"
            ],
            [
                "address(0)"
            ],
            "#Medium#ERROR_MSG:ERC777: transfer to the zero address"
        ],
        [
            "NOT",
            [
                "isContract()"
            ],
            "#High#ERROR_MSG:ERC777: token recipient contract has no implementer for ERC777TokensRecipient"
        ],
        [
            "GTE",
            [
                "_balances@from",
                "_balances@to",
                "_balances@account",
                "_balances@tokenHolder",
                "_balances@recipient",
                "_balances@sender",
                "fromBalance"
            ],
            [
                "amount",
                "uint256_1"
            ],
            "#Medium#ERROR_MSG:ERC777: transfer amount exceeds balance"
        ]
    ],
    "AccessControlDefaultAdminRules._beginDefaultAdminTransfer(address) returns()": [
        [
            "LTE",
            [
                "value",
                "timestamp"
            ],
            [
                "max@type()(uint48)"
            ],
            "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
        ]
    ],
    "Counters.current(Counters.Counter) returns(uint256)": [],
    "ERC2771Context._msgSender() returns(address)": [],
    "AccessControlDefaultAdminRules.cancelDefaultAdminTransfer() returns()": [
        [
            [
                "onlyRole",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ]
    ],
    "ERC777.allowance(address,address) returns(uint256)": [],
    "Counters.increment(Counters.Counter) returns()": [],
    "GovernorTimelockCompoundMock.slitherConstructorConstantVariables() returns()": [],
    "AccessControlDefaultAdminRules._cancelDefaultAdminTransfer() returns()": [],
    "Counters.decrement(Counters.Counter) returns()": [
        [
            "GT",
            [
                "value",
                "_value@counter"
            ],
            [
                "0"
            ],
            "#Low#ERROR_MSG:Counter: decrement overflow"
        ]
    ],
    "AccessControlDefaultAdminRules.acceptDefaultAdminTransfer() returns()": [
        [
            "EQ",
            [
                "_msgSender()",
                "msgsender"
            ],
            [
                "newDefaultAdmin"
            ],
            "#Medium#ERROR_MSG:AccessControl: pending admin must accept"
        ],
        [
            "_isScheduleSet(schedule)",
            [
                "NEQ",
                [
                    "schedule"
                ],
                [
                    "0"
                ]
            ],
            "#Medium#EERROR_MSG:AccessControl: transfer delay not passed"
        ],
        [
            "_hasSchedulePassed(schedule)",
            [
                "LT",
                [
                    "schedule"
                ],
                [
                    "timestamp"
                ]
            ],
            "#Medium#EERROR_MSG:AccessControl: transfer delay not passed"
        ],
        [
            "EQ",
            [
                "defaultAdmin()",
                [
                    "_currentDefaultAdmin"
                ]
            ],
            [
                "address(0)"
            ],
            "#Low#EERROR_MSG:AccessControl: default admin already granted"
        ]
    ],
    "Address.verifyCallResult(bool,bytes,string) returns(bytes)": [
    ],
    "TokenTimelock.release() returns()": [
        [
            "GTE",
            [
                "timestamp"
            ],
            [
                "releaseTime()",
                [
                    "_releaseTime"
                ]
            ],
            "#Medium#ERROR_MSG:TokenTimelock: current time is before release time"
        ],
        [
            "GT",
            [
                "amount",
                "balanceOf(address(this))",
                "value"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:TokenTimelock: no tokens to release"
        ],
        [
            [
                [
                    "EQ",
                    [
                        "length@functionCall(data,SafeERC20: low-level call failed)",
                        "length@returndata"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ],
                [
                    "decode(returndata,(bool))"
                ]
            ],
            "#Medium#ERROR_MSG:SafeERC20: ERC20 operation did not succeed"
        ],
        [
            "GTE",
            [
                "balance@address(this)"
            ],
            [
                "value",
                "0"
            ],
            "#Medium#ERROR_MSG:Address: insufficient balance for call"
        ],
        [
            [
                "isContract(target)",
                [
                    "GT",
                    [
                        "length@code@account"
                    ],
                    [
                        "value",
                        "0"
                    ]
                ]
            ],
            "#Medium#ERROR_MSG:Address: call to non-contract"
        ]
    ],
    "Address._revert(bytes,string) returns()": [
    ],
    "BridgeArbitrumL1Mock.slitherConstructorVariables() returns()": [],
    "Arrays.findUpperBound(uint256[],uint256) returns(uint256)": [],
    "ERC721Holder.onERC721Received(address,address,uint256,bytes) returns(bytes4)": [],
    "Arrays.unsafeAccess(address[],uint256) returns(StorageSlot.AddressSlot)": [],
    "Arrays.unsafeAccess(bytes32[],uint256) returns(StorageSlot.Bytes32Slot)": [],
    "Arrays.unsafeAccess(uint256[],uint256) returns(StorageSlot.Uint256Slot)": [],
    "Base64.encode(bytes) returns(string)": [],
    "UUPSUpgradeableUnsafeMock.slitherConstructorConstantVariables() returns()": [],
    "AccessControlEnumerable.slitherConstructorConstantVariables() returns()": [],
    "Checkpoints.getAtBlock(Checkpoints.History,uint256) returns(uint256)": [
        [
            "LT",
            [
                "value",
                "uint256_1",
                "blockNumber"
            ],
            [
                "number"
            ],
            "#Medium#ERROR_MSG:Checkpoints: block not yet mined"
        ],
        [
            "LTE",
            [
                "value",
                "uint256_1",
                "blockNumber"
            ],
            [
                "max@type()(uint32)"
            ],
            "#Low#ERROR_MSG:SafeCast: value doesn't fit in 32 bits"
        ]
    ]
}
call_req={
    "ERC721._safeMint(address,uint256) returns()": {
        "ERC721Wrapper.depositFor(address,uint256[]) returns(bool)": [],
        "ERC721Wrapper.onERC721Received(address,address,uint256,bytes) returns(bytes4)": [
            [
                "EQ",
                [
                    "address(underlying())"
                ],
                [
                    "_msgSender()",
                    "msg.sender"
                ],
                "#High#ERROR_MSG:ERC721Wrapper: caller is not underlying"
            ]
        ],
        "ERC721.safeMint(address,uint256,bytes) returns()": [
            [
                [
                    [
                        "EQ",
                        [
                            "msgsender",
                            "msg.sender",
                            "_msgSender()"
                        ],
                        [
                            "owner",
                            "admin",
                            "ownerof(tokenId)",
                            "_owner@tokenId"
                        ]
                    ],
                    "OnlyRole",
                    [
                        "hasRole(role,account)"
                    ]
                ],
                "#High#ERROR_MSG:ERC721: Not allowed mint"
            ]
        ]
    },
    "ERC20._transfer(address,address,uint256) returns()": {
        "ERC20.transfer(address,uint256) returns(bool)": [
            [
                "MsgSender",
                [
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ],
        "ERC20.transferFrom(address,address,uint256) returns(bool)": [
            [
                "GTE",
                [
                    "allowance(owner,spender)",
                    "_allowances@owner@spender",
                    "_allowances@owner@_msgSender()",
                    "currentAllowance",
                    "_allowances@owner@msgsender"
                ],
                [
                    "amount",
                    "uint256_1"
                ],
                "#High#ERROR_MSG:ERC20: insufficient allowance"
            ],
            [
                "NEQ",
                [
                    "owner",
                    "address_1",
                    "from"
                ],
                [
                    "address(0)"
                ],
                "#Medium#ERROR_MSG:ERC20: approve from the zero address"
            ],
            [
                "NEQ",
                [
                    "spender",
                    "_msgSender()",
                    "msgsender"
                ],
                [
                    "address(0)"
                ],
                "#Medium#ERROR_MSG:ERC20: approve to the zero address"
            ]
        ],
        "ERC20FlashMint.flashLoan(IERC3156FlashBorrower,address,uint256,bytes) returns(bool)": [
            [
                "EQ",
                [
                    "receiver.onFlashLoan(msg.sender,token,amount,fee,data)"
                ],
                [
                    "_RETURN_VALUE",
                    "bytes32"
                ],
                "#High#ERROR_MSG:ERC20FlashMint: invalid return value"
            ],
            [
                "NEQ",
                [
                    "from",
                    "account",
                    "address_1"
                ],
                [
                    "address(0)"
                ],
                "#Low#ERROR_MSG:ERC20: burn from the zero address"
            ],
            [
                "GTE",
                [
                    "_balances@from",
                    "fromBalance",
                    "_balances@account",
                    "accountBalance"
                ],
                [
                    "amount",
                    "fee",
                    "flashFee(token,amount)",
                    "uint256_1"
                ],
                "#Medium#ERROR_MSG:ERC20: burn amount exceeds balance"
            ]
        ]
    },
    "Initializable._isInitializing() returns(bool)": {
        "InitializableMock.isInitializing() returns(bool)": []
    },
    "ERC20VotesLegacyMock._delegate(address,address) returns()": {
        "ERC20VotesLegacyMock.delegate(address) returns()": [
            [
                "MsgSender",
                [
                    "_msgSender()",
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ],
        "ERC20VotesLegacyMock.delegateBySig(address,uint256,uint256,uint8,bytes32,bytes32) returns()": [
            [
                "EQ",
                [
                    "nonce"
                ],
                [
                    "_useNonce(signer)"
                ],
                "#Medium#ERROR_MSG:ERC20Votes: invalid nonce"
            ]
        ]
    },
    "ERC20._burn(address,uint256) returns()": {
        "ERC20Mock.burn(address,uint256) returns()": [],
        "ERC4626Mock.burn(address,uint256) returns()": [],
        "ERC20FlashMint.flashLoan(IERC3156FlashBorrower,address,uint256,bytes) returns(bool)": [
            [
                "EQ",
                [
                    "receiver.onFlashLoan(msg.sender,token,amount,fee,data)"
                ],
                [
                    "_RETURN_VALUE",
                    "bytes32"
                ],
                "#High#ERROR_MSG:ERC20FlashMint: invalid return value"
            ],
            [
                "GTE",
                [
                    "allowance(owner,spender)",
                    "_allowances@owner@spender",
                    "currentAllowance"
                ],
                [
                    "amount"
                ],
                "#High#ERROR_MSG:ERC20: insufficient allowance"
            ],
            [
                "NEQ",
                [
                    "owner"
                ],
                [
                    "address(0)"
                ],
                "#Medium#ERROR_MSG:ERC20: approve from the zero address"
            ],
            [
                "NEQ",
                [
                    "spender"
                ],
                [
                    "address(0)"
                ],
                "#Medium#ERROR_MSG:ERC20: approve to the zero address"
            ]
        ],
        "ERC20Burnable.burn(uint256) returns()": [
            [
                "MsgSender",
                [
                    "_msgSender()",
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ],
        "ERC20Wrapper.withdrawTo(address,uint256) returns(bool)": [
            [
                "MsgSender",
                [
                    "_msgSender()",
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ],
        "ERC20Burnable.burnFrom(address,uint256) returns()": [
            [
                "GTE",
                [
                    "allowance(owner,spender)",
                    "_allowances@owner@spender",
                    "_allowances@account@spender",
                    "_allowances@from@spender",
                    "_allowances@address_1@spender",
                    "allowance(owner,spender)",
                    "allowance(account,spender)",
                    "allowance(from,spender)",
                    "allowance(address_1,spender)",
                    "currentAllowance"
                ],
                [
                    "amount",
                    "uint256_1"
                ],
                "#High#ERROR_MSG:ERC20: insufficient allowance"
            ],
            [
                "NEQ",
                [
                    "owner",
                    "from",
                    "account",
                    "address_1"
                ],
                [
                    "address(0)"
                ],
                "#Medium#ERROR_MSG:ERC20: approve from the zero address"
            ],
            [
                "NEQ",
                [
                    "spender"
                ],
                [
                    "address(0)"
                ],
                "#Medium#ERROR_MSG:ERC20: approve to the zero address"
            ]
        ]
    },
    "Pausable._pause() returns()": {
        "PausableMock.pause() returns()": [],
        "ERC1155PresetMinterPauser.pause() returns()": [
            [
                [
                    "hasRole(PAUSE_ROLE,_msgSender())",
                    [
                        "members@_roles@role@account"
                    ],
                    "OnlyRole",
                    [
                        "EQ",
                        [
                            "msgsender",
                            "_msgSender()"
                        ],
                        [
                            "owner",
                            "admin",
                            "auth",
                            "gov"
                        ]
                    ]
                ],
                "#High#ERROR_MSG:ERC1155PresetMinterPauser: must have pauser role to pause"
            ]
        ],
        "ERC20PresetMinterPauser.pause() returns()": [
            [
                [
                    "hasRole(PAUSE_ROLE,_msgSender())",
                    [
                        "members@_roles@role@account"
                    ],
                    "OnlyRole",
                    [
                        "EQ",
                        [
                            "msgsender",
                            "_msgSender()"
                        ],
                        [
                            "owner",
                            "admin",
                            "auth",
                            "gov"
                        ]
                    ]
                ],
                "#High#ERROR_MSG:ERC20PresetMinterPauser: must have pauser role to pause"
            ]
        ],
        "ERC721PresetMinterPauserAutoId.pause() returns()": [
            [
                [
                    "hasRole(PAUSE_ROLE,_msgSender())",
                    [
                        "members@_roles@role@account"
                    ],
                    "OnlyRole",
                    [
                        "EQ",
                        [
                            "msgsender",
                            "_msgSender()"
                        ],
                        [
                            "owner",
                            "admin",
                            "auth",
                            "gov"
                        ]
                    ]
                ],
                "#High#ERROR_MSG:ERC721PresetMinterPauserAutoId: must have pauser role to pause"
            ]
        ]
    },
    "PullPayment._asyncTransfer(address,uint256) returns()": {
        "PullPaymentMock.callTransfer(address,uint256) returns()": []
    },
    "Governor._castVote(uint256,address,uint8,string) returns(uint256)": {
        "Governor.castVote(uint256,uint8) returns(uint256)": [
            [
                "MsgSender",
                [
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ],
        "Governor.castVoteWithReason(uint256,uint8,string) returns(uint256)": [
            [
                "MsgSender",
                [
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ],
        "Governor.castVoteBySig(uint256,uint8,uint8,bytes32,bytes32) returns(uint256)": [
            [
                "EQ",
                [
                    "InvalidSignature@RecoverError"
                ],
                [
                    "error"
                ],
                "#Medium#ERROR_MSG:(ECDSA: invalid signature)"
            ],
            [
                "EQ",
                [
                    "InvalidSignatureLength@RecoverError"
                ],
                [
                    "error"
                ],
                "#Medium#ERROR_MSG:(ECDSA: invalid signature length)"
            ],
            [
                "EQ",
                [
                    "InvalidSignatureS@RecoverError"
                ],
                [
                    "error"
                ],
                "#Medium#ERROR_MSG:(ECDSA: invalid signature 's' value)"
            ]
        ]
    },
    "Pausable._unpause() returns()": {
        "PausableMock.unpause() returns()": [],
        "ERC1155PresetMinterPauser.unpause() returns()": [
            [
                [
                    "hasRole(PAUSE_ROLE,_msgSender())",
                    [
                        "members@_roles@role@account"
                    ],
                    "OnlyRole",
                    [
                        "EQ",
                        [
                            "msgsender",
                            "_msgSender()"
                        ],
                        [
                            "owner",
                            "admin",
                            "auth",
                            "gov"
                        ]
                    ]
                ],
                "#High#ERROR_MSG:ERC1155PresetMinterPauser: must have pauser role to unpause"
            ]
        ],
        "ERC20PresetMinterPauser.unpause() returns()": [
            [
                [
                    "hasRole(PAUSE_ROLE,_msgSender())",
                    [
                        "members@_roles@role@account"
                    ],
                    "OnlyRole",
                    [
                        "EQ",
                        [
                            "msgsender",
                            "_msgSender()"
                        ],
                        [
                            "owner",
                            "admin",
                            "auth",
                            "gov"
                        ]
                    ]
                ],
                "#High#ERROR_MSG:ERC20PresetMinterPauser: must have pauser role to unpause"
            ]
        ],
        "ERC721PresetMinterPauserAutoId.unpause() returns()": [
            [
                [
                    "hasRole(PAUSE_ROLE,_msgSender())",
                    [
                        "members@_roles@role@account"
                    ],
                    "OnlyRole",
                    [
                        "EQ",
                        [
                            "msgsender",
                            "_msgSender()"
                        ],
                        [
                            "owner",
                            "admin",
                            "auth",
                            "gov"
                        ]
                    ]
                ],
                "#High#ERROR_MSG:ERC721PresetMinterPauserAutoId: must have pauser role to unpause"
            ]
        ]
    },
    "ERC20._approve(address,address,uint256) returns()": {
        "ERC20.approve(address,uint256) returns(bool)": [
            [
                "MsgSender",
                [
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ],
        "ERC20.increaseAllowance(address,uint256) returns(bool)": [
            [
                "MsgSender",
                [
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ],
        "ERC20.decreaseAllowance(address,uint256) returns(bool)": [
            [
                "GTE",
                [
                    "allowance(owner,spender)",
                    "_allowances@owner@spender",
                    "currentAllowance",
                    "currentAllowance"
                ],
                [
                    "subtractedValue"
                ],
                "#High#ERROR_MSG:ERC20: decreased allowance below zero"
            ],
            [
                "MsgSender",
                [
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ],
        "ERC20Permit.permit(address,address,uint256,uint256,uint8,bytes32,bytes32) returns()": [
            [
                "EQ",
                [
                    "recover(hash,v,r,s)",
                    "signer"
                ],
                [
                    "owner"
                ],
                "#High#ERROR_MSG:ERC20Permit: invalid signature"
            ],
            [
                "EQ",
                [
                    "InvalidSignature@RecoverError"
                ],
                [
                    "error"
                ],
                "#Medium#ERROR_MSG:(ECDSA: invalid signature)"
            ],
            [
                "EQ",
                [
                    "InvalidSignatureLength@RecoverError"
                ],
                [
                    "error"
                ],
                "#Medium#ERROR_MSG:(ECDSA: invalid signature length)"
            ],
            [
                "EQ",
                [
                    "InvalidSignatureS@RecoverError"
                ],
                [
                    "error"
                ],
                "#Medium#ERROR_MSG:(ECDSA: invalid signature 's' value)"
            ]
        ]
    },
    "ERC721._mint(address,uint256) returns()": {
        "ERC721PresetMinterPauserAutoId.mint(address) returns()": [],
        "ERC721.mint(address,uint256,bytes) returns()": [
            [
                [
                    [
                        "EQ",
                        [
                            "msgsender",
                            "msg.sender",
                            "_msgSender()"
                        ],
                        [
                            "owner",
                            "admin",
                            "auth",
                            "gov",
                            "ownerof(tokenId)",
                            "_owner@tokenId"
                        ]
                    ],
                    "OnlyRole",
                    [
                        "hasRole(role,account)"
                    ]
                ],
                "#High#ERROR_MSG:ERC721: Not allowed mint"
            ]
        ]
    },
    "ERC20._spendAllowance(address,address,uint256) returns()": {
        "ERC20.transferFrom(address,address,uint256) returns(bool)": [
            [
                "MsgSender",
                [
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ],
        "ERC20Burnable.burnFrom(address,uint256) returns()": [
            [
                "MsgSender",
                [
                    "_msgSender()",
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ],
        "ERC20FlashMint.flashLoan(IERC3156FlashBorrower,address,uint256,bytes) returns(bool)": [
            [
                "EQ",
                [
                    "receiver.onFlashLoan(msg.sender,token,amount,fee,data)"
                ],
                [
                    "_RETURN_VALUE",
                    "bytes32"
                ],
                "#High#ERROR_MSG:ERC20FlashMint: invalid return value"
            ]
        ]
    },
    "Governor._quorumReached(uint256) returns(bool)": {
        "Governor.state(uint256) returns(IGovernor.ProposalState)": [
            [
                "EQ",
                [
                    "0"
                ],
                [
                    "proposalSnapshot(proposalId)",
                    "REF_1872",
                    "voteStart@Governor._proposals@Governor.proposalSnapshot(uint256).proposalId",
                    "Governor.state(uint256).snapshot",
                    "Governor.state(uint256).snapshot"
                ],
                "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
            ]
        ]
    },
    "ERC721._requireMinted(uint256) returns()": {
        "ERC721.tokenURI(uint256) returns(string)": [],
        "ERC721.getApproved(uint256) returns(address)": [],
        "ERC721URIStorage.tokenURI(uint256) returns(string)": []
    },
    "Votes._useNonce(address) returns(uint256)": {
        "Votes.delegateBySig(address,uint256,uint256,uint8,bytes32,bytes32) returns()": [
            [
                "EQ",
                [
                    "InvalidSignature@RecoverError"
                ],
                [
                    "error"
                ],
                "#Medium#ERROR_MSG:(ECDSA: invalid signature)"
            ],
            [
                "EQ",
                [
                    "InvalidSignatureLength@RecoverError"
                ],
                [
                    "error"
                ],
                "#Medium#ERROR_MSG:(ECDSA: invalid signature length)"
            ],
            [
                "EQ",
                [
                    "InvalidSignatureS@RecoverError"
                ],
                [
                    "error"
                ],
                "#Medium#ERROR_MSG:(ECDSA: invalid signature 's' value)"
            ]
        ]
    },
    "Governor._execute(uint256,address[],uint256[],bytes[],bytes32) returns()": {
        "Governor.execute(address[],uint256[],bytes[],bytes32) returns(uint256)": [
            [
                [
                    [
                        "EQ",
                        [
                            "state(proposalId)",
                            "currentState"
                        ],
                        [
                            "Succeeded@ProposalState"
                        ]
                    ],
                    [
                        "EQ",
                        [
                            "state(proposalId)",
                            "currentState"
                        ],
                        [
                            "Queued@ProposalState"
                        ]
                    ]
                ],
                "#Medium#ERROR_MSG:Governor: proposal not successful"
            ],
            [
                "EQ",
                [
                    "0"
                ],
                [
                    "proposalSnapshot(proposalId)",
                    "REF_1872",
                    "voteStart@_proposals@proposalId",
                    "snapshot",
                    "voteStart@_proposals@targets",
                    "voteStart@_proposals@calldatas",
                    "voteStart@_proposals@descriptionHash",
                    "voteStart@_proposals@hashProposal(targets,values,calldatas,descriptionHash)",
                    "voteStart@_proposals@",
                    "voteStart@_proposals@values",
                    "voteStart@proposal",
                    "voteStart@_proposals@encode(targets,values,calldatas,descriptionHash)))"
                ],
                "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
            ]
        ]
    },
    "ERC721._safeTransfer(address,address,uint256,bytes) returns()": {
        "ERC721.safeTransferFrom(address,address,uint256,bytes) returns()": [
            [
                [
                    "_isApprovedOrOwner(_msgSender(),tokenId)",
                    "_isApprovedOrOwner(msgsender,tokenId)",
                    [
                        "EQ",
                        [
                            "_msgSender()",
                            "spender"
                        ],
                        [
                            "ownerOf(tokenId)",
                            "owner"
                        ]
                    ],
                    "isApprovedForAll(_msgSender(),tokenId)",
                    "isApprovedForAll(msgsender,tokenId)",
                    "_operatorApprovals@_msgSender()@tokenId",
                    "_operatorApprovals@msgsender@tokenId",
                    [
                        "EQ",
                        "getApproved(tokenId)",
                        [
                            "_msgSender()",
                            "msgsender"
                        ]
                    ]
                ],
                "#High#ERROR_MSG:ERC721: caller is not token owner or approved"
            ],
            [
                "NEQ",
                [
                    "_ownerOf(tokenId)",
                    "_owners@tokenId",
                    "_owners@firstTokenId",
                    "owner"
                ],
                [
                    "address(0)"
                ],
                "#Low#ERROR_MSG:ERC721: invalid token ID"
            ]
        ]
    },
    "ERC1967Upgrade._upgradeToAndCall(address,bytes,bool) returns()": {
        "UUPSUpgradeableUnsafeMock.upgradeTo(address) returns()": [],
        "UUPSUpgradeableUnsafeMock.upgradeToAndCall(address,bytes) returns()": []
    },
    "ERC20._mint(address,uint256) returns()": {
        "ERC20.mint(address,uint256) returns()": [
            [
                "EQ",
                [
                    "msgsender",
                    "msg.sender",
                    "_msgSender()"
                ],
                [
                    "owner",
                    "admin",
                    "auth",
                    "gov"
                ],
                "#High#ERROR_MSG:ERC20: must have minter role to mint"
            ]
        ],
        "ERC20Mock.mint(address,uint256) returns()": [],
        "ERC4626Mock.mint(address,uint256) returns()": [],
        "ERC20FlashMint.flashLoan(IERC3156FlashBorrower,address,uint256,bytes) returns(bool)": [
            [
                "LTE",
                [
                    "amount"
                ],
                [
                    "maxFlashLoan(token)"
                ],
                "#Medium#ERROR_MSG:ERC20FlashMint: amount exceeds maxFlashLoan"
            ],
            [
                "EQ",
                [
                    "token"
                ],
                [
                    "address(this)"
                ],
                "#Low#ERROR_MSG:ERC20FlashMint: wrong token"
            ],
            [
                "EQ",
                [
                    "receiver@onFlashLoan(msg.sender, token, amount, fee, data)"
                ],
                [
                    "_RETURN_VALUE"
                ],
                "#Medium#ERROR_MSG:ERC20FlashMint: wrong token"
            ]
        ],
        "ERC20Wrapper.depositFor(address,uint256) returns(bool)": [
            [
                [
                    [
                        "EQ",
                        [
                            "length@functionCall(data,SafeERC20: low-level call failed)",
                            "length@returndata"
                        ],
                        [
                            "value",
                            "0"
                        ]
                    ],
                    [
                        "decode(returndata,(bool))"
                    ]
                ],
                "#Medium#ERROR_MSG:SafeERC20: ERC20 operation did not succeed"
            ],
            [
                "GTE",
                [
                    "balance@address(this)"
                ],
                [
                    "value",
                    "0"
                ],
                "#Medium#ERROR_MSG:Address: insufficient balance for call"
            ],
            [
                [
                    "isContract(target)",
                    [
                        "GT",
                        [
                            "length@code@account"
                        ],
                        [
                            "value",
                            "0"
                        ]
                    ]
                ],
                "#Medium#ERROR_MSG:Address: call to non-contract"
            ]
        ],
        "ERC20PresetMinterPauser.mint(address,uint256) returns()": [
            [
                [
                    "hasRole(MINTER_ROLE,_msgSender())",
                    [
                        "members@_roles@role@account"
                    ],
                    "OnlyRole",
                    [
                        "EQ",
                        [
                            "msgsender",
                            "_msgSender()"
                        ],
                        [
                            "owner",
                            "admin",
                            "auth",
                            "gov"
                        ]
                    ]
                ],
                "#High#ERROR_MSG:ERC20PresetMinterPauser: must have minter role to mint"
            ]
        ]
    },
    "Governor._cancel(address[],uint256[],bytes[],bytes32) returns(uint256)": {
        "Governor.cancel(address[],uint256[],bytes[],bytes32) returns(uint256)": [
            [
                "EQ",
                [
                    "_msgSender()",
                    "msg.sender"
                ],
                [
                    "proposer@_proposals@hashProposal(targets,values,calldatas,descriptionHash)",
                    "proposer@_proposals@uint256(keccak256(bytes)(abi.encode(targets,values,calldatas,descriptionHash)))",
                    "proposer@_proposals@proposalId",
                    "proposer@_proposals@proposalId"
                ],
                "#High#ERROR_MSG:Governor: only proposer can cancel"
            ],
            [
                "EQ",
                [
                    "0"
                ],
                [
                    "proposalSnapshot(proposalId)",
                    "REF_1872",
                    "voteStart@_proposals@hashProposal(targets,values,calldatas,descriptionHash)",
                    "voteStart@_proposals@encode(targets,values,calldatas,descriptionHash)))",
                    "voteStart@_proposals@proposalId",
                    "snapshot",
                    "voteStart@proposal"
                ],
                "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
            ]
        ],
        "GovernorCompatibilityBravo.cancel(address[],uint256[],bytes[],bytes32) returns(uint256)": [
            [
                [
                    [
                        "EQ",
                        [
                            "_msgSender()",
                            "msg.sender"
                        ],
                        [
                            "proposer@_proposalDetails@hashProposal(targets,values,calldatas,descriptionHash)",
                            "proposer@_proposalDetails@uint256(keccak256(bytes)(abi.encode(targets,values,calldatas,descriptionHash)))",
                            "proposer@_proposalDetails@proposalId",
                            "proposer",
                            "proposer"
                        ]
                    ],
                    [
                        "LT",
                        [
                            "getVotes(proposer,clock() - 1)",
                            "_getVotes(account,timepoint,_defaultParams())"
                        ],
                        [
                            "proposalThreshold()",
                            "0"
                        ]
                    ]
                ],
                "#Medium#ERROR_MSG:GovernorBravo: proposer above threshold"
            ]
        ]
    },
    "AccessControl._revokeRole(bytes32,address) returns()": {
        "AccessControl.revokeRole(bytes32,address) returns()": [],
        "AccessControl.renounceRole(bytes32,address) returns()": [
            [
                "EQ",
                [
                    "account"
                ],
                [
                    "_msgSender()",
                    "msg.sender"
                ],
                "#High#ERROR_MSG:AccessControl: can only renounce roles for self"
            ]
        ]
    },
    "Governor._executor() returns(address)": {
        "Governor.receive() returns()": []
    },
    "Governor._voteSucceeded(uint256) returns(bool)": {
        "Governor.state(uint256) returns(IGovernor.ProposalState)": [
            [
                "EQ",
                [
                    "0"
                ],
                [
                    "proposalSnapshot(proposalId)",
                    "REF_1872",
                    "voteStart@Governor._proposals@Governor.proposalSnapshot(uint256).proposalId",
                    "Governor.state(uint256).snapshot",
                    "Governor.state(uint256).snapshot"
                ],
                "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
            ]
        ]
    },
    "ERC721._ownerOf(uint256) returns(address)": {
        "ERC721.ownerOf(uint256) returns(address)": []
    },
    "GovernorVotesQuorumFraction._updateQuorumNumerator(uint256) returns()": {
        "GovernorVotesQuorumFraction.updateQuorumNumerator(uint256) returns()": [
            [
                "onlyGovernance",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "_executor()",
                        "address(this)"
                    ]
                ],
                "#High#ERROR_MSG:Governor: onlyGovernance"
            ]
        ]
    },
    "ERC721._isApprovedOrOwner(address,uint256) returns(bool)": {},
    "AccessControl._grantRole(bytes32,address) returns()": {
        "AccessControl.grantRole(bytes32,address) returns()": []
    },
    "EIP712._domainSeparatorV4() returns(bytes32)": {
        "Votes.DOMAIN_SEPARATOR() returns(bytes32)": [],
        "ERC20Permit.DOMAIN_SEPARATOR() returns(bytes32)": []
    },
    "ERC4626._deposit(address,address,uint256,uint256) returns()": {
        "ERC4626.deposit(uint256,address) returns(uint256)": [
            [
                "MsgSender",
                [
                    "_msgSender()",
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ],
        "ERC4626.mint(uint256,address) returns(uint256)": [
            [
                "MsgSender",
                [
                    "_msgSender()",
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ]
    },
    "EIP712._hashTypedDataV4(bytes32) returns(bytes32)": {
        "Governor.castVoteBySig(uint256,uint8,uint8,bytes32,bytes32) returns(uint256)": [],
        "Governor.castVoteWithReasonAndParamsBySig(uint256,uint8,string,bytes,uint8,bytes32,bytes32) returns(uint256)": [],
        "Votes.delegateBySig(address,uint256,uint256,uint8,bytes32,bytes32) returns()": [
            [
                "LTE",
                [
                    "block.timestamp"
                ],
                [
                    "expiry"
                ],
                "#Medium#ERROR_MSG:Votes: signature expired"
            ]
        ],
        "MinimalForwarder.verify(MinimalForwarder.ForwardRequest,bytes) returns(bool)": [],
        "EIP712Verifier.verify(bytes,address,address,string) returns()": [],
        "ERC20VotesLegacyMock.delegateBySig(address,uint256,uint256,uint8,bytes32,bytes32) returns()": [
            [
                "LTE",
                [
                    "block.timestamp"
                ],
                [
                    "expiry"
                ],
                "#Medium#ERROR_MSG:ERC20Votes: signature expired"
            ]
        ],
        "ERC20Permit.permit(address,address,uint256,uint256,uint8,bytes32,bytes32) returns()": [],
        "ERC20Votes.delegateBySig(address,uint256,uint256,uint8,bytes32,bytes32) returns()": [
            [
                "LTE",
                [
                    "block.timestamp"
                ],
                [
                    "expiry"
                ],
                "#Medium#ERROR_MSG:ERC20Votes: signature expired"
            ]
        ]
    },
    "Initializable._disableInitializers() returns()": {
        "ReinitializerMock.disableInitializers() returns()": []
    },
    "ERC1820Implementer._registerInterfaceForAddress(bytes32,address) returns()": {
        "ERC777SenderRecipientMock.senderFor(address) returns()": [],
        "ERC777SenderRecipientMock.recipientFor(address) returns()": []
    },
    "ERC721._baseURI() returns(string)": {
        "ERC721.tokenURI(uint256) returns(string)": [],
        "ERC721URIStorage.tokenURI(uint256) returns(string)": []
    },
    "Ownable._transferOwnership(address) returns()": {
        "Ownable.renounceOwnership() returns()": [],
        "Ownable.transferOwnership(address) returns()": [
            [
                "NEQ",
                [
                    "newOwner"
                ],
                [
                    "address(0)"
                ],
                "#Low#ERROR_MSG:Ownable: new owner is the zero address"
            ]
        ]
    },
    "ERC721._transfer(address,address,uint256) returns()": {
        "ERC721.transferFrom(address,address,uint256) returns()": [
            [
                [
                    "_isApprovedOrOwner(_msgSender(),tokenId)",
                    "_isApprovedOrOwner(msgsender,tokenId)",
                    [
                        "EQ",
                        [
                            "_msgSender()",
                            "spender"
                        ],
                        [
                            "ownerOf(tokenId)",
                            "owner"
                        ]
                    ],
                    "isApprovedForAll(_msgSender(),tokenId)",
                    "isApprovedForAll(msgsender,tokenId)",
                    "_operatorApprovals@_msgSender()@tokenId",
                    "_operatorApprovals@msgsender@tokenId",
                    [
                        "EQ",
                        "getApproved(tokenId)",
                        [
                            "_msgSender()",
                            "msgsender"
                        ]
                    ]
                ],
                "#High#ERROR_MSG:ERC721: caller is not token owner or approved"
            ],
            [
                "NEQ",
                [
                    "_ownerOf(tokenId)",
                    "_owners@tokenId",
                    "_owners@firstTokenId",
                    "owner"
                ],
                [
                    "address(0)"
                ],
                "#Low#ERROR_MSG:ERC721: invalid token ID"
            ]
        ]
    },
    "ERC721._burn(uint256) returns()": {
        "ERC721Burnable.burn(uint256) returns()": [
            [
                [
                    "_isApprovedOrOwner(_msgSender(),tokenId)",
                    "_isApprovedOrOwner(msgsender,tokenId)",
                    [
                        "EQ",
                        [
                            "_msgSender()",
                            "spender"
                        ],
                        [
                            "ownerOf(tokenId)",
                            "owner"
                        ]
                    ],
                    "isApprovedForAll(_msgSender(),tokenId)",
                    "isApprovedForAll(msgsender,tokenId)",
                    "_operatorApprovals@_msgSender()@tokenId",
                    "_operatorApprovals@msgsender@tokenId",
                    [
                        "EQ",
                        "getApproved(tokenId)",
                        [
                            "_msgSender()",
                            "msgsender"
                        ]
                    ]
                ],
                "#High#ERROR_MSG:ERC721: caller is not token owner or approved"
            ],
            [
                "NEQ",
                [
                    "_ownerOf(tokenId)",
                    "_owners@tokenId",
                    "_owners@firstTokenId",
                    "owner"
                ],
                [
                    "address(0)"
                ],
                "#Low#ERROR_MSG:ERC721: invalid token ID"
            ]
        ],
        "ERC721Wrapper.withdrawTo(address,uint256[]) returns(bool)": [
            [
                [
                    "_isApprovedOrOwner(_msgSender(),tokenId)",
                    "_isApprovedOrOwner(msgsender,tokenId)",
                    [
                        "EQ",
                        [
                            "_msgSender()",
                            "spender"
                        ],
                        [
                            "ownerOf(tokenId)",
                            "owner"
                        ]
                    ],
                    "isApprovedForAll(_msgSender(),tokenId)",
                    "isApprovedForAll(msgsender,tokenId)",
                    "_operatorApprovals@_msgSender()@tokenId",
                    "_operatorApprovals@msgsender@tokenId",
                    [
                        "EQ",
                        "getApproved(tokenId)",
                        [
                            "_msgSender()",
                            "msgsender"
                        ]
                    ]
                ],
                "#High#ERROR_MSG:ERC721Wrapper: caller is not token owner or approved"
            ],
            [
                "NEQ",
                [
                    "_ownerOf(tokenId)",
                    "_owners@tokenId",
                    "_owners@tokenIds@i",
                    "_owners@firstTokenId",
                    "owner"
                ],
                [
                    "address(0)"
                ],
                "#Low#ERROR_MSG:ERC721: invalid token ID"
            ]
        ]
    },
    "ERC4626._decimalsOffset() returns(uint8)": {
        "ERC4626.decimals() returns(uint8)": []
    },
    "Math.max(uint256,uint256) returns(uint256)": {
        "GovernorPreventLateQuorum.proposalDeadline(uint256) returns(uint256)": []
    },
    "ERC20Votes._delegate(address,address) returns()": {
        "ERC20Votes.delegate(address) returns()": [
            [
                "MsgSender",
                [
                    "_msgSender()",
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ],
        "ERC20Votes.delegateBySig(address,uint256,uint256,uint8,bytes32,bytes32) returns()": [
            [
                "EQ",
                [
                    "nonce"
                ],
                [
                    "_useNonce(signer)"
                ],
                "#Medium#ERROR_MSG:ERC20Votes: invalid nonce"
            ]
        ]
    },
    "Governor._beforeExecute(uint256,address[],uint256[],bytes[],bytes32) returns()": {
        "Governor.execute(address[],uint256[],bytes[],bytes32) returns(uint256)": [
            [
                [
                    [
                        "EQ",
                        [
                            "state(proposalId)",
                            "currentState"
                        ],
                        [
                            "Succeeded@IGovernor.ProposalState"
                        ]
                    ],
                    [
                        "EQ",
                        [
                            "state(proposalId)",
                            "currentState"
                        ],
                        [
                            "Queued@IGovernor.ProposalState"
                        ]
                    ]
                ],
                "#Medium#ERROR_MSG:Governor: proposal not successful"
            ],
            [
                "EQ",
                [
                    "0"
                ],
                [
                    "proposalSnapshot(proposalId)",
                    "REF_1872",
                    "voteStart@_proposals@proposalId",
                    "snapshot",
                    "voteStart@_proposals@targets",
                    "voteStart@_proposals@calldatas",
                    "voteStart@_proposals@descriptionHash",
                    "voteStart@_proposals@hashProposal(targets,values,calldatas,descriptionHash)",
                    "voteStart@_proposals@",
                    "voteStart@_proposals@values",
                    "voteStart@proposal",
                    "voteStart@_proposals@encode(targets,values,calldatas,descriptionHash)))"
                ],
                "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
            ]
        ]
    },
    "SampleHuman.__SampleHuman_init() returns()": {
        "SampleHuman.initialize() returns()": [
            [
                [
                    [
                        [
                            [
                                [
                                    "! _initializing",
                                    "isTopLevelCall"
                                ],
                                [
                                    "LT",
                                    [
                                        "_initialized",
                                        "uint8"
                                    ],
                                    [
                                        "1"
                                    ]
                                ]
                            ]
                        ],
                        [
                            [
                                [
                                    "NOT",
                                    [
                                        "isContract(address(this))"
                                    ]
                                ],
                                [
                                    "EQ",
                                    [
                                        "_initialized",
                                        "uint8"
                                    ],
                                    [
                                        "1"
                                    ]
                                ]
                            ]
                        ]
                    ],
                    "#High#ERROR_MSG:Initializable: contract is already initialized"
                ]
            ],
            "initializer"
        ]
    },
    "ERC1155._safeTransferFrom(address,address,uint256,uint256,bytes) returns()": {
        "ERC1155.safeTransferFrom(address,address,uint256,uint256,bytes) returns()": [
            [
                [
                    [
                        "EQ",
                        [
                            "from"
                        ],
                        [
                            "_msgSender()",
                            "msg.sender"
                        ]
                    ],
                    [
                        "isApprovedForAll(from,_msgSender())",
                        [
                            "_operatorApprovals@isApprovedForAll(address,address).account@isApprovedForAll(address,address).operator"
                        ]
                    ]
                ],
                "#High#ERROR_MSG:ERC1155: caller is not token owner or approved"
            ]
        ]
    },
    "ERC777._send(address,address,uint256,bytes,bytes,bool) returns()": {
        "ERC777.send(address,uint256,bytes) returns()": [
            [
                "MsgSender",
                [
                    "_msgSender()",
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ],
        "ERC777.transfer(address,uint256) returns(bool)": [
            [
                "MsgSender",
                [
                    "_msgSender()",
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ],
        "ERC777.operatorSend(address,address,uint256,bytes,bytes) returns()": [
            [
                "isOperatorFor(_msgSender(),sender)",
                [
                    [
                        [
                            [
                                [
                                    "EQ",
                                    [
                                        "operator"
                                    ],
                                    [
                                        "tokenHolder"
                                    ]
                                ],
                                [
                                    [
                                        [
                                            "_defaultOperators@operator"
                                        ],
                                        [
                                            "NOT",
                                            [
                                                "_revokedDefaultOperators@tokenHolder@operator"
                                            ]
                                        ]
                                    ]
                                ]
                            ]
                        ],
                        [
                            "ERC777._operators@tokenHolder@operator"
                        ]
                    ]
                ],
                "#High#ERROR_MSG:ERC777: caller is not an operator for holder"
            ]
        ],
        "ERC777.transferFrom(address,address,uint256) returns(bool)": [
            [
                "GTE",
                [
                    "allowance(owner,spender)",
                    "_allowances@holder@spender",
                    "_allowances@holder@_msgSender()",
                    "currentAllowance",
                    "_allowances@holder@msgsender"
                ],
                [
                    "amount",
                    "uint256_1"
                ],
                "#High#ERROR_MSG:ERC777: insufficient allowance"
            ],
            [
                "NEQ",
                [
                    "from",
                    "to",
                    "holder",
                    "account",
                    "address_1",
                    "address_2",
                    "owner",
                    "recipient"
                ],
                [
                    "address(0)"
                ],
                "#Low#ERROR_MSG:ERC777: approve from the zero address"
            ],
            [
                "NEQ",
                [
                    "spender",
                    "_msgSender()",
                    "msgsender"
                ],
                [
                    "address(0)"
                ],
                "#Medium#ERROR_MSG:ERC777: approve to the zero address"
            ]
        ]
    },
    "Votes._getTotalSupply() returns(uint256)": {
        "VotesMock.getTotalSupply() returns(uint256)": []
    },
    "SafeCast.toUint96(uint256) returns(uint96)": {
        "ERC20VotesComp.getCurrentVotes(address) returns(uint96)": [],
        "ERC20VotesComp.getPriorVotes(address,uint256) returns(uint96)": [
            [
                "LT",
                [
                    "timepoint",
                    "blockNumber"
                ],
                [
                    "clock()",
                    "number)"
                ],
                "#Meidum#ERROR_MSG:ERC20Votes: future lookup"
            ],
            [
                "LTE",
                [
                    "value",
                    "number"
                ],
                [
                    "max@type()(uint48)"
                ],
                "#Meidum#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
            ]
        ]
    },
    "ERC1155._setApprovalForAll(address,address,bool) returns()": {
        "ERC1155.setApprovalForAll(address,bool) returns()": [
            [
                "MsgSender",
                [
                    "_msgSender()",
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ]
    },
    "SafeCast.toUint64(uint256) returns(uint64)": {
        "Governor.propose(address[],uint256[],bytes[],string) returns(uint256)": [
            [
                "_isValidDescriptionForProposer(proposer,description)",
                "#High#ERROR_MSG:Governor: proposer restricted"
            ],
            [
                "GTE",
                [
                    "getVotes(proposer,currentTimepoint - 1)",
                    "_getVotes(account,timepoint,_defaultParams())"
                ],
                [
                    "proposalThreshold()",
                    "0"
                ],
                "#Meidum#ERROR_MSG:Governor: proposer votes below proposal threshold"
            ],
            [
                "EQ",
                [
                    "length@targets"
                ],
                [
                    "length@values"
                ],
                "#Meidum#ERROR_MSG:Governor: invalid proposal length"
            ],
            [
                "EQ",
                [
                    "length@targets"
                ],
                [
                    "length@calldatas"
                ],
                "#Low#ERROR_MSG:Governor: invalid proposal length"
            ],
            [
                "GT",
                [
                    "length@targets"
                ],
                [
                    "0"
                ],
                "#Low#ERROR_MSG:Governor: empty proposal"
            ],
            [
                "EQ",
                [
                    "voteStart@_proposals@hashProposal(targets,values,calldatas,keccak256(bytes)(bytes(description)))",
                    "voteStart@_proposals@uint256(keccak256(bytes)(abi.encode(targets,values,calldatas,descriptionHash)))",
                    "voteStart@_proposals@proposalId",
                    "voteStart@_proposals@proposalId"
                ],
                [
                    "0"
                ],
                "#Medium#ERROR_MSG:Governor: proposal already exists"
            ]
        ],
        "GovernorTimelockCompound.queue(address[],uint256[],bytes[],bytes32) returns(uint256)": [
            [
                "EQ",
                [
                    "state(proposalId)"
                ],
                [
                    "Succeeded@ProposalState"
                ],
                "#High#ERROR_MSG:Governor: proposal not successful"
            ],
            [
                "EQ",
                [
                    "0"
                ],
                [
                    "proposalSnapshot(proposalId)",
                    "REF_2545",
                    "voteStart@_proposals@encode(targets,values,calldatas,descriptionHash)))",
                    "voteStart@_proposals@proposalId",
                    "voteStart@_proposals@hashProposal(targets,values,calldatas,descriptionHash)",
                    "snapshot",
                    "voteStart@proposal"
                ],
                "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
            ]
        ]
    },
    "ReentrancyGuard._reentrancyGuardEntered() returns(bool)": {
        "ReentrancyMock.guardedCheckEntered() returns()": [],
        "ReentrancyMock.unguardedCheckNotEntered() returns()": []
    },
    "SafeCast.toUint48(uint256) returns(uint48)": {
        "GovernorVotes.clock() returns(uint48)": [],
        "GovernorVotesComp.clock() returns(uint48)": [
            [
                "LTE",
                [
                    "uint256_1",
                    "value",
                    "number"
                ],
                [
                    "max@type()(uint48)"
                ],
                "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
            ]
        ],
        "Votes.clock() returns(uint48)": [],
        "ERC20VotesTimestampMock.clock() returns(uint48)": [],
        "ERC20VotesCompTimestampMock.clock() returns(uint48)": [],
        "ERC721VotesTimestampMock.clock() returns(uint48)": [],
        "ERC20Votes.clock() returns(uint48)": []
    },
    "SafeCast.toUint32(uint256) returns(uint32)": {
        "GovernorVotesQuorumFraction.quorumNumerator(uint256) returns(uint256)": [],
        "Votes.getPastVotes(address,uint256) returns(uint256)": [
            [
                "LT",
                [
                    "timepoint"
                ],
                [
                    "clock()",
                    "toUint48(block.number)"
                ],
                "#Medium#ERROR_MSG:Votes: future lookup"
            ],
            [
                "LTE",
                [
                    "value",
                    "number"
                ],
                [
                    "max@type()(uint48)"
                ],
                "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
            ]
        ],
        "Votes.getPastTotalSupply(uint256) returns(uint256)": [
            [
                "LT",
                [
                    "Votes.getPastTotalSupply(uint256).timepoint"
                ],
                [
                    "clock()",
                    "SafeCast.toUint48(block.number)"
                ],
                "#Medium#ERROR_MSG:Votes: future lookup"
            ],
            [
                "LTE",
                [
                    "value",
                    "number"
                ],
                [
                    "max@type()(uint48)"
                ],
                "#Medium#ERROR_MSG:SafeCast: value doesn't fit in 48 bits"
            ]
        ],
        "ERC20VotesLegacyMock.numCheckpoints(address) returns(uint32)": [],
        "ERC20Votes.numCheckpoints(address) returns(uint32)": []
    },
    "Initializable._getInitializedVersion() returns(uint8)": {
        "ReinitializerMock.getInitializedVersion() returns(uint8)": []
    },
    "Votes._delegate(address,address) returns()": {
        "Votes.delegate(address) returns()": [
            [
                "MsgSender",
                [
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ],
        "Votes.delegateBySig(address,uint256,uint256,uint8,bytes32,bytes32) returns()": [
            [
                "EQ",
                [
                    "nonce"
                ],
                [
                    "_useNonce(signer)"
                ],
                "#High#ERROR_MSG:Votes: invalid nonce"
            ]
        ],
        "VotesMock.delegate(address,address) returns()": []
    },
    "GovernorPreventLateQuorum._setLateQuorumVoteExtension(uint64) returns()": {
        "GovernorPreventLateQuorum.setLateQuorumVoteExtension(uint64) returns()": [
            [
                "onlyGovernance",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "_executor()",
                        "address(this)"
                    ]
                ],
                "#High#ERROR_MSG:Governor: onlyGovernance"
            ]
        ]
    },
    "SampleGramps.__SampleGramps_init(string) returns()": {
        "SampleGramps.initialize(string) returns()": [
            [
                [
                    [
                        [
                            [
                                [
                                    "! _initializing",
                                    "isTopLevelCall"
                                ],
                                [
                                    "LT",
                                    [
                                        "_initialized",
                                        "uint8"
                                    ],
                                    [
                                        "1"
                                    ]
                                ]
                            ]
                        ],
                        [
                            [
                                [
                                    "NOT",
                                    [
                                        "isContract(address(this))"
                                    ]
                                ],
                                [
                                    "EQ",
                                    [
                                        "_initialized",
                                        "uint8"
                                    ],
                                    [
                                        "1"
                                    ]
                                ]
                            ]
                        ]
                    ],
                    "#High#ERROR_MSG:Initializable: contract is already initialized"
                ]
            ],
            "initializer"
        ]
    },
    "ERC721._setApprovalForAll(address,address,bool) returns()": {
        "ERC721.setApprovalForAll(address,bool) returns()": [
            [
                "MsgSender",
                [
                    "_msgSender()",
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ]
    },
    "SampleFather.__SampleFather_init(string,uint256) returns()": {
        "SampleFather.initialize(string,uint256) returns()": [
            [
                [
                    [
                        [
                            [
                                [
                                    "! _initializing",
                                    "isTopLevelCall"
                                ],
                                [
                                    "LT",
                                    [
                                        "_initialized",
                                        "uint8"
                                    ],
                                    [
                                        "1"
                                    ]
                                ]
                            ]
                        ],
                        [
                            [
                                [
                                    "NOT",
                                    [
                                        "isContract(address(this))"
                                    ]
                                ],
                                [
                                    "EQ",
                                    [
                                        "_initialized",
                                        "uint8"
                                    ],
                                    [
                                        "1"
                                    ]
                                ]
                            ]
                        ]
                    ],
                    "#High#ERROR_MSG:Initializable: contract is already initialized"
                ]
            ],
            "initializer"
        ]
    },
    "SampleChild.__SampleChild_init(uint256,string,uint256,uint256) returns()": {
        "SampleChild.initialize(uint256,string,uint256,uint256) returns()": [
            [
                [
                    [
                        [
                            [
                                [
                                    "! _initializing",
                                    "isTopLevelCall"
                                ],
                                [
                                    "LT",
                                    [
                                        "_initialized",
                                        "uint8"
                                    ],
                                    [
                                        "1"
                                    ]
                                ]
                            ]
                        ],
                        [
                            [
                                [
                                    "NOT",
                                    [
                                        "isContract(address(this))"
                                    ]
                                ],
                                [
                                    "EQ",
                                    [
                                        "_initialized",
                                        "uint8"
                                    ],
                                    [
                                        "1"
                                    ]
                                ]
                            ]
                        ]
                    ],
                    "#High#ERROR_MSG:Initializable: contract is already initialized"
                ]
            ],
            "initializer"
        ]
    },
    "GovernorSettings._setVotingDelay(uint256) returns()": {
        "GovernorSettings.setVotingDelay(uint256) returns()": [
            [
                "onlyGovernance",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "_executor()",
                        "address(this)"
                    ]
                ],
                "#High#ERROR_MSG:Governor: onlyGovernance"
            ]
        ]
    },
    "GovernorSettings._setVotingPeriod(uint256) returns()": {
        "GovernorSettings.setVotingPeriod(uint256) returns()": [
            [
                "onlyGovernance",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "_executor()",
                        "address(this)"
                    ]
                ],
                "#High#ERROR_MSG:Governor: onlyGovernance"
            ]
        ]
    },
    "Ownable2Step._transferOwnership(address) returns()": {
        "Ownable2Step.acceptOwnership() returns()": [
            [
                "EQ",
                [
                    "pendingOwner()",
                    [
                        "Ownable2Step._pendingOwner",
                        "_pendingOwner"
                    ]
                ],
                [
                    "_msgSender()",
                    "msg.sender",
                    "sender"
                ],
                "#High#ERROR_MSG:Ownable2Step: caller is not the new owner"
            ],
            [
                "MsgSender",
                [
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ]
    },
    "ERC20Permit._useNonce(address) returns(uint256)": {
        "ERC20VotesLegacyMock.delegateBySig(address,uint256,uint256,uint8,bytes32,bytes32) returns()": [],
        "ERC20Permit.permit(address,address,uint256,uint256,uint8,bytes32,bytes32) returns()": [
            [
                "LTE",
                [
                    "block.timestamp"
                ],
                [
                    "ERC20Permit.permit(address,address,uint256,uint256,uint8,bytes32,bytes32).deadline"
                ],
                "#Medium#ERROR_MSG:ERC20Permit: expired deadline"
            ]
        ],
        "ERC20Votes.delegateBySig(address,uint256,uint256,uint8,bytes32,bytes32) returns()": [
            [
                "EQ",
                [
                    "InvalidSignature@RecoverError"
                ],
                [
                    "error"
                ],
                "#Medium#ERROR_MSG:(ECDSA: invalid signature)"
            ],
            [
                "EQ",
                [
                    "InvalidSignatureLength@RecoverError"
                ],
                [
                    "error"
                ],
                "#Medium#ERROR_MSG:(ECDSA: invalid signature length)"
            ],
            [
                "EQ",
                [
                    "InvalidSignatureS@RecoverError"
                ],
                [
                    "error"
                ],
                "#Medium#ERROR_MSG:(ECDSA: invalid signature 's' value)"
            ]
        ]
    },
    "CrossChainEnabledPolygonChild._isCrossChain() returns(bool)": {
        "CrossChainEnabledPolygonChild.processMessageFromRoot(uint256,address,bytes) returns()": []
    },
    "Governor._castVote(uint256,address,uint8,string,bytes) returns(uint256)": {
        "Governor.castVoteWithReasonAndParams(uint256,uint8,string,bytes) returns(uint256)": [
            [
                "MsgSender",
                [
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ],
        "Governor.castVoteWithReasonAndParamsBySig(uint256,uint8,string,bytes,uint8,bytes32,bytes32) returns(uint256)": [
            [
                "EQ",
                [
                    "InvalidSignature@RecoverError"
                ],
                [
                    "error"
                ],
                "#Medium#ERROR_MSG:(ECDSA: invalid signature)"
            ],
            [
                "EQ",
                [
                    "InvalidSignatureLength@RecoverError"
                ],
                [
                    "error"
                ],
                "#Medium#ERROR_MSG:(ECDSA: invalid signature length)"
            ],
            [
                "EQ",
                [
                    "InvalidSignatureS@RecoverError"
                ],
                [
                    "error"
                ],
                "#Medium#ERROR_MSG:(ECDSA: invalid signature 's' value)"
            ]
        ]
    },
    "Proxy._fallback() returns()": {
        "Proxy.fallback() returns()": [],
        "Proxy.receive() returns()": []
    },
    "UUPSUpgradeableLegacyMock._upgradeToAndCallSecureLegacyV1(address,bytes,bool) returns()": {
        "UUPSUpgradeableLegacyMock.upgradeTo(address) returns()": [],
        "UUPSUpgradeableLegacyMock.upgradeToAndCall(address,bytes) returns()": []
    },
    "Governor._getVotes(address,uint256,bytes) returns(uint256)": {
        "Governor.getVotes(address,uint256) returns(uint256)": [],
        "Governor.getVotesWithParams(address,uint256,bytes) returns(uint256)": []
    },
    "ERC1967Upgrade._upgradeToAndCallUUPS(address,bytes,bool) returns()": {
        "UUPSUpgradeable.upgradeTo(address) returns()": [],
        "UUPSUpgradeable.upgradeToAndCall(address,bytes) returns()": []
    },
    "GovernorSettings._setProposalThreshold(uint256) returns()": {
        "GovernorSettings.setProposalThreshold(uint256) returns()": [
            [
                "onlyGovernance",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "_executor()",
                        "address(this)"
                    ]
                ],
                "#High#ERROR_MSG:Governor: onlyGovernance"
            ]
        ]
    },
    "ERC1155._burnBatch(address,uint256[],uint256[]) returns()": {
        "ERC1155Burnable.burnBatch(address,uint256[],uint256[]) returns()": [
            [
                [
                    [
                        "EQ",
                        [
                            "account"
                        ],
                        [
                            "_msgSender()",
                            "msg.sender"
                        ]
                    ],
                    [
                        "isApprovedForAll(account,_msgSender())",
                        [
                            "_operatorApprovals@account@operator"
                        ]
                    ]
                ],
                "#High#ERROR_MSG:ERC1155: caller is not token owner or approved"
            ]
        ]
    },
    "SafeERC20.safeTransfer(IERC20,address,uint256) returns()": {
        "PaymentSplitter.release(IERC20,address) returns()": [
            [
                "GT",
                [
                    "account"
                ],
                [
                    "0"
                ],
                "#Lower#ERROR_MSG:PaymentSplitter: account has no shares"
            ],
            [
                "NEQ",
                [
                    "releasable(token,account)",
                    "payment"
                ],
                [
                    "0"
                ],
                "#Lower#ERROR_MSG:PaymentSplitter: account is not due payment"
            ]
        ],
        "VestingWallet.release(address) returns()": [],
        "ERC20Wrapper.withdrawTo(address,uint256) returns(bool)": [
            [
                "NEQ",
                [
                    "sender",
                    "from",
                    "account",
                    "address_1"
                ],
                [
                    "address(0)"
                ],
                "#Lower#ERROR_MSG:ERC20: transfer from the zero address"
            ],
            [
                "GTE",
                [
                    "_balances@sender",
                    "_balances@from",
                    "_balances@account",
                    "accountBalance"
                ],
                [
                    "amount",
                    "uint256_1",
                    "value"
                ],
                "#Medium#ERROR_MSG:ERC20: transfer amount exceeds balance"
            ]
        ],
        "TokenTimelock.release() returns()": [
            [
                "GTE",
                [
                    "block.timestamp"
                ],
                [
                    "releaseTime()",
                    [
                        "TokenTimelock._releaseTime",
                        "_releaseTime"
                    ]
                ],
                "#Medium#ERROR_MSG:TokenTimelock: current time is before release time"
            ],
            [
                "GT",
                [
                    "token().balanceOf(address(this))",
                    "TokenTimelock.release().amount",
                    "TokenTimelock.release().amount"
                ],
                [
                    "0"
                ],
                "#Medium#ERROR_MSG:TokenTimelock: no tokens to release"
            ]
        ]
    },
    "SafeERC20.safeTransferFrom(IERC20,address,address,uint256) returns()": {
        "ERC20Wrapper.depositFor(address,uint256) returns(bool)": [
            [
                "NEQ",
                [
                    "_msgSender()",
                    "msg.sender",
                    "sender"
                ],
                [
                    "address(this)"
                ],
                "#Low#ERROR_MSG:ERC20Wrapper: wrapper can't deposit"
            ],
            [
                "MsgSender",
                [
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ]
    },
    "ShortStrings.toStringWithFallback(ShortString,string) returns(string)": {
        "EIP712.eip712Domain() returns(bytes1,string,string,uint256,address,bytes32,uint256[])": []
    },
    "Governor._defaultParams() returns(bytes)": {
        "Governor.getVotes(address,uint256) returns(uint256)": []
    },
    "ERC4626Fees._entryFeeBasePoint() returns(uint256)": {
        "ERC4626Fees.previewDeposit(uint256) returns(uint256)": [],
        "ERC4626Fees.previewMint(uint256) returns(uint256)": [
            [
                "GT",
                [
                    "denominator",
                    "100000"
                ],
                [
                    "prod1"
                ],
                "#Medium#ERROR_MSG:Math: mulDiv overflow"
            ]
        ]
    },
    "ERC4626Fees._exitFeeBasePoint() returns(uint256)": {
        "ERC4626Fees.previewWithdraw(uint256) returns(uint256)": [],
        "ERC4626Fees.previewRedeem(uint256) returns(uint256)": [
            [
                "GT",
                [
                    "denominator"
                ],
                [
                    "prod1"
                ],
                "#Medium#ERROR_MSG:Math: mulDiv overflow"
            ]
        ]
    },
    "TimelockController._execute(address,uint256,bytes) returns()": {
        "TimelockController.execute(address,uint256,bytes,bytes32,bytes32) returns()": [
            [
                [
                    "isOperationReady(id)"
                ],
                "#Medium#ERROR_MSG:TimelockController: operation is not ready"
            ],
            [
                [
                    [
                        "EQ",
                        [
                            "predecessor",
                            "id",
                            "hashOperation(target,value,payload,predecessor,salt)",
                            "encode(target,value,data,predecessor,salt))"
                        ],
                        [
                            "bytes32(0)"
                        ]
                    ],
                    [
                        "isOperationDone(predecessor)",
                        [
                            "EQ",
                            [
                                "getTimestamp(id)",
                                [
                                    "_timestamps@predecessor",
                                    "_timestamps@id",
                                    "timestamp",
                                    "_timestamps@hashOperation(target,value,payload,predecessor,salt)",
                                    "_timestamps@encode(target,value,data,predecessor,salt))",
                                    "getTimestamp(id)"
                                ]
                            ],
                            [
                                "_DONE_TIMESTAMP",
                                "uint256(1)",
                                "uint256"
                            ]
                        ]
                    ]
                ],
                "#Medium#ERROR_MSG:TimelockController: missing dependency"
            ]
        ],
        "TimelockController.executeBatch(address[],uint256[],bytes[],bytes32,bytes32) returns()": [
            [
                [
                    "isOperationReady(id)"
                ],
                "#Medium#ERROR_MSG:TimelockController: operation is not ready"
            ]
        ]
    },
    "Governor._isValidDescriptionForProposer(address,string) returns(bool)": {
        "Governor.propose(address[],uint256[],bytes[],string) returns(uint256)": [
            [
                "MsgSender",
                [
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ]
    },
    "Governor._afterExecute(uint256,address[],uint256[],bytes[],bytes32) returns()": {
        "Governor.execute(address[],uint256[],bytes[],bytes32) returns(uint256)": [
            [
                [
                    [
                        "EQ",
                        [
                            "state(proposalId)",
                            "Governor.execute(address[],uint256[],bytes[],bytes32).currentState",
                            "Governor.execute(address[],uint256[],bytes[],bytes32).currentState"
                        ],
                        [
                            "Succeeded@IGovernor.ProposalState"
                        ]
                    ],
                    [
                        "EQ",
                        [
                            "state(proposalId)",
                            "Governor.execute(address[],uint256[],bytes[],bytes32).currentState",
                            "Governor.execute(address[],uint256[],bytes[],bytes32).currentState"
                        ],
                        [
                            "Queued@IGovernor.ProposalState"
                        ]
                    ]
                ],
                "#Medium#ERROR_MSG:Governor: proposal not successful"
            ],
            [
                "EQ",
                [
                    "0"
                ],
                [
                    "proposalSnapshot(proposalId)",
                    "REF_1872",
                    "voteStart@_proposals@proposalId",
                    "snapshot",
                    "voteStart@_proposals@targets",
                    "voteStart@_proposals@calldatas",
                    "voteStart@_proposals@descriptionHash",
                    "voteStart@_proposals@hashProposal(targets,values,calldatas,descriptionHash)",
                    "voteStart@_proposals@",
                    "voteStart@_proposals@values",
                    "voteStart@proposal",
                    "voteStart@_proposals@encode(targets,values,calldatas,descriptionHash)))"
                ],
                "#Medium#ERROR_MSG:(Governor: unknown proposal id)"
            ]
        ]
    },
    "ERC20FlashMint._flashFee(address,uint256) returns(uint256)": {
        "ERC20FlashMint.flashFee(address,uint256) returns(uint256)": [
            [
                "EQ",
                [
                    "token"
                ],
                [
                    "address(this)"
                ],
                "#Low#ERROR_MSG:ERC20FlashMint: wrong token"
            ]
        ]
    },
    "ERC721._approve(address,uint256) returns()": {
        "ERC721.approve(address,uint256) returns()": [
            [
                [
                    [
                        "EQ",
                        [
                            "_msgSender()",
                            "msg.sender"
                        ],
                        [
                            "ownerOf(tokenId)",
                            "owner"
                        ]
                    ],
                    [
                        "isApprovedForAll(owner,_msgSender())",
                        [
                            "_operatorApprovals@owner@operator"
                        ]
                    ]
                ],
                "#High#ERROR_MSG:ERC721: approve caller is not token owner or approved for all"
            ]
        ]
    },
    "ERC20FlashMint._flashFeeReceiver() returns(address)": {
        "ERC20FlashMint.flashLoan(IERC3156FlashBorrower,address,uint256,bytes) returns(bool)": [
            [
                "EQ",
                [
                    "receiver.onFlashLoan(msg.sender,token,amount,fee,data)"
                ],
                [
                    "ERC20FlashMint._RETURN_VALUE",
                    "bytes32"
                ],
                "#High#ERROR_MSG:ERC20FlashMint: invalid return value"
            ],
            [
                "NEQ",
                [
                    "to",
                    "account",
                    "flashFeeReceiver",
                    "_flashFeeReceiver()",
                    "address(0)"
                ],
                [
                    "address(0)"
                ],
                "#Lower#ERROR_MSG:ERC20: mint to the zero address"
            ]
        ]
    },
    "ERC1155._safeBatchTransferFrom(address,address,uint256[],uint256[],bytes) returns()": {
        "ERC1155.safeBatchTransferFrom(address,address,uint256[],uint256[],bytes) returns()": [
            [
                [
                    [
                        "EQ",
                        [
                            "from"
                        ],
                        [
                            "_msgSender()",
                            "msg.sender"
                        ]
                    ],
                    [
                        "isApprovedForAll(from,_msgSender())",
                        [
                            "_operatorApprovals@account@operator"
                        ]
                    ]
                ],
                "#High#ERROR_MSG:ERC1155: caller is not token owner or approved"
            ]
        ]
    },
    "AccessControlDefaultAdminRules._acceptDefaultAdminTransfer() returns()": {
        "AccessControlDefaultAdminRules.acceptDefaultAdminTransfer() returns()": [
            [
                "EQ",
                [
                    "_msgSender()",
                    "msg.sender"
                ],
                [
                    "AccessControlDefaultAdminRules.acceptDefaultAdminTransfer().newDefaultAdmin"
                ],
                "#Medium#ERROR_MSG:AccessControl: pending admin must accept"
            ]
        ]
    },
    "AccessControlDefaultAdminRules._changeDefaultAdminDelay(uint48) returns()": {
        "AccessControlDefaultAdminRules.changeDefaultAdminDelay(uint48) returns()": []
    },
    "ERC777._burn(address,uint256,bytes,bytes) returns()": {
        "ERC777.burn(uint256,bytes) returns()": [
            [
                "MsgSender",
                [
                    "_msgSender()",
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ],
        "ERC777.operatorBurn(address,uint256,bytes,bytes) returns()": [
            [
                "isOperatorFor(_msgSender(),account)",
                [
                    [
                        [
                            [
                                [
                                    "EQ",
                                    [
                                        "operator"
                                    ],
                                    [
                                        "tokenHolder"
                                    ]
                                ],
                                [
                                    [
                                        [
                                            "_defaultOperators@operator"
                                        ],
                                        [
                                            "NOT",
                                            [
                                                "_revokedDefaultOperators@tokenHolder@operator"
                                            ]
                                        ]
                                    ]
                                ]
                            ]
                        ],
                        [
                            "_operators@tokenHolder@operator"
                        ]
                    ]
                ],
                "#High#ERROR_MSG:ERC777: caller is not an operator for holder"
            ]
        ]
    },
    "AccessControlDefaultAdminRules._rollbackDefaultAdminDelay() returns()": {
        "AccessControlDefaultAdminRules.rollbackDefaultAdminDelay() returns()": []
    },
    "ERC777._approve(address,address,uint256) returns()": {
        "ERC777.approve(address,uint256) returns(bool)": [
            [
                "MsgSender",
                [
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ]
    },
    "ERC777._spendAllowance(address,address,uint256) returns()": {
        "ERC777.transferFrom(address,address,uint256) returns(bool)": [
            [
                "MsgSender",
                [
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ]
    },
    "UUPSUpgradeable._authorizeUpgrade(address) returns()": {
        "UUPSUpgradeable.upgradeTo(address) returns()": [
            [
                [
                    "NEQ",
                    [
                        "address(this)"
                    ],
                    [
                        "__self",
                        "address"
                    ],
                    "#Medium#ERROR_MSG:Function must be called through delegatecall"
                ],
                [
                    "EQ",
                    [
                        "_getImplementation()",
                        [
                            "value@getAddressSlot(_IMPLEMENTATION_SLOT)"
                        ]
                    ],
                    [
                        "__self",
                        "address"
                    ],
                    "#Medium#ERROR_MSG:Function must be called through active proxy"
                ]
            ],
            [
                "onlyproxy",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ],
        "UUPSUpgradeable.upgradeToAndCall(address,bytes) returns()": [
            [
                [
                    "NEQ",
                    [
                        "address(this)"
                    ],
                    [
                        "__self",
                        "address"
                    ],
                    "#Medium#ERROR_MSG:Function must be called through delegatecall"
                ],
                [
                    "EQ",
                    [
                        "_getImplementation()",
                        [
                            "value@getAddressSlot(_IMPLEMENTATION_SLOT)"
                        ]
                    ],
                    [
                        "__self",
                        "address"
                    ],
                    "#Medium#ERROR_MSG:Function must be called through active proxy"
                ]
            ],
            [
                "onlyproxy",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "owner",
                        "admin",
                        "auth"
                    ]
                ]
            ],
            "#High#ERROR_MSG: caller is not the owner"
        ]
    },
    "ERC1155._mintBatch(address,uint256[],uint256[],bytes) returns()": {
        "ERC1155PresetMinterPauser.mintBatch(address,uint256[],uint256[],bytes) returns()": [
            [
                [
                    "hasRole(MINTER_ROLE,_msgSender())",
                    [
                        "members@_roles@role@account"
                    ],
                    "OnlyRole",
                    [
                        "EQ",
                        [
                            "msgsender",
                            "_msgSender()"
                        ],
                        [
                            "owner",
                            "admin",
                            "auth",
                            "gov"
                        ]
                    ]
                ],
                "#High#ERROR_MSG:ERC1155PresetMinterPauser: must have minter role to mint"
            ]
        ]
    },
    "ERC2981._feeDenominator() returns(uint96)": {
        "ERC2981.royaltyInfo(uint256,uint256) returns(address,uint256)": []
    },
    "ECDSA.recover(bytes32,bytes) returns(address)": {
        "MinimalForwarder.verify(MinimalForwarder.ForwardRequest,bytes) returns(bool)": [],
        "EIP712Verifier.verify(bytes,address,address,string) returns()": [],
        "ERC1271WalletMock.isValidSignature(bytes32,bytes) returns(bytes4)": []
    },
    "ECDSA.recover(bytes32,uint8,bytes32,bytes32) returns(address)": {
        "Governor.castVoteBySig(uint256,uint8,uint8,bytes32,bytes32) returns(uint256)": [],
        "Governor.castVoteWithReasonAndParamsBySig(uint256,uint8,string,bytes,uint8,bytes32,bytes32) returns(uint256)": [],
        "Votes.delegateBySig(address,uint256,uint256,uint8,bytes32,bytes32) returns()": [],
        "ERC20VotesLegacyMock.delegateBySig(address,uint256,uint256,uint8,bytes32,bytes32) returns()": [],
        "ERC20Permit.permit(address,address,uint256,uint256,uint8,bytes32,bytes32) returns()": [],
        "ERC20Votes.delegateBySig(address,uint256,uint256,uint8,bytes32,bytes32) returns()": []
    },
    "ERC4626._withdraw(address,address,address,uint256,uint256) returns()": {
        "ERC4626.withdraw(uint256,address,address) returns(uint256)": [
            [
                "MsgSender",
                [
                    "_msgSender()",
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ],
        "ERC4626.redeem(uint256,address,address) returns(uint256)": [
            [
                "MsgSender",
                [
                    "_msgSender()",
                    "msg.sender"
                ],
                "#High#Para Need to be MsgSender"
            ]
        ]
    },
    "CompTimelock.getBlockTimestamp() returns(uint256)": {
        "CompTimelock.queueTransaction(address,uint256,string,bytes,uint256) returns(bytes32)": [
            [
                "EQ",
                [
                    "msg.sender"
                ],
                [
                    "CompTimelock.admin",
                    "address"
                ],
                "#High#ERROR_MSG:Timelock::queueTransaction: Call must come from admin."
            ]
        ],
        "CompTimelock.executeTransaction(address,uint256,string,bytes,uint256) returns(bytes)": [
            [
                "EQ",
                [
                    "msg.sender"
                ],
                [
                    "CompTimelock.admin",
                    "address"
                ],
                "#High#ERROR_MSG:Timelock::executeTransaction: Call must come from admin."
            ],
            [
                "CompTimelock.queuedTransactions@keccak256(bytes)(abi.encode(target,value,signature,data,eta))",
                "CompTimelock.queuedTransactions@CompTimelock.executeTransaction(address,uint256,string,bytes,uint256).txHash",
                "CompTimelock.queuedTransactions@CompTimelock.executeTransaction(address,uint256,string,bytes,uint256).txHash",
                "#High#ERROR_MSG:Timelock::executeTransaction: Transaction hasn't been queued."
            ]
        ]
    },
    "VestingWallet._vestingSchedule(uint256,uint64) returns(uint256)": {
        "VestingWallet.vestedAmount(uint64) returns(uint256)": [],
        "VestingWallet.vestedAmount(address,uint64) returns(uint256)": []
    },
    "Address.sendValue(address,uint256) returns()": {},
    "Address.functionCall(address,bytes) returns(bytes)": {
        "ERC20Reentrant.functionCall(address,bytes) returns(bytes)": [],
        "ERC3156FlashBorrowerMock.onFlashLoan(address,address,uint256,uint256,bytes) returns(bytes32)": [
            [
                "EQ",
                [
                    "msg.sender"
                ],
                [
                    "ERC3156FlashBorrowerMock.onFlashLoan(address,address,uint256,uint256,bytes).token"
                ],
                "#High#ERROR_MSG:None"
            ]
        ],
        "TimelockReentrant.reenter() returns()": []
    },
    "Address.functionDelegateCall(address,bytes) returns(bytes)": {
        "Multicall.multicall(bytes[]) returns(bytes[])": []
    },
    "Address.functionDelegateCall(address,bytes,string) returns(bytes)": {
        "CrossChainEnabledPolygonChild.processMessageFromRoot(uint256,address,bytes) returns()": [
            [
                "NOT",
                [
                    "_isCrossChain()",
                    [
                        "EQ",
                        [
                            "msg.sender"
                        ],
                        [
                            "CrossChainEnabledPolygonChild._fxChild",
                            "address"
                        ]
                    ]
                ],
                "#HIgh#ERROR_MSG:NotCrossChainCall()()"
            ]
        ]
    },
    "Address.verifyCallResultFromTarget(address,bool,bytes,string) returns(bytes)": {
        "BaseRelayMock.relayAs(address,bytes,address) returns()": []
    },
    "ERC1155._mint(address,uint256,uint256,bytes) returns()": {
        "ERC1155PresetMinterPauser.mint(address,uint256,uint256,bytes) returns()": [
            [
                [
                    "hasRole(MINTER_ROLE,_msgSender())",
                    [
                        "members@_roles@role@account"
                    ],
                    "OnlyRole",
                    [
                        "EQ",
                        [
                            "msg.sender",
                            "msgsender"
                        ],
                        [
                            "owner",
                            "admin"
                        ]
                    ]
                ],
                "#High#ERROR_MSG:ERC1155PresetMinterPauser: must have minter role to mint"
            ]
        ]
    },
    "ERC1155._burn(address,uint256,uint256) returns()": {
        "ERC1155Burnable.burn(address,uint256,uint256) returns()": [
            [
                [
                    [
                        "EQ",
                        [
                            "account"
                        ],
                        [
                            "_msgSender()",
                            "msg.sender"
                        ]
                    ],
                    [
                        "isApprovedForAll(account,_msgSender())",
                        [
                            "_operatorApprovals@Eaccount@operator"
                        ]
                    ]
                ],
                "#High#ERROR_MSG:ERC1155: caller is not token owner or approved"
            ]
        ]
    },
    "SampleMother.__SampleMother_init(uint256) returns()": {
        "SampleMother.initialize(uint256) returns()": [
            [
                [
                    [
                        [
                            "! _initializing",
                            "isTopLevelCall"
                        ],
                        [
                            "LT",
                            [
                                "_initialized",
                                "uint8"
                            ],
                            [
                                "1"
                            ]
                        ]
                    ],
                    [
                        [
                            "NOT",
                            [
                                "isContract(address(this))"
                            ]
                        ],
                        [
                            "EQ",
                            [
                                "_initialized",
                                "uint8"
                            ],
                            [
                                "1"
                            ]
                        ]
                    ]
                ],
                "#High#ERROR_MSG:Initializable: contract is already initialized"
            ],
            "initializer"
        ]
    },
    "Strings.toString(uint256) returns(string)": {
        "ERC721.tokenURI(uint256) returns(string)": []
    },
    "AccessControlDefaultAdminRules._beginDefaultAdminTransfer(address) returns()": {
        "AccessControlDefaultAdminRules.beginDefaultAdminTransfer(address) returns()": []
    },
    "AccessControlDefaultAdminRules._cancelDefaultAdminTransfer() returns()": {
        "AccessControlDefaultAdminRules.cancelDefaultAdminTransfer() returns()": []
    },
    "Address.verifyCallResult(bool,bytes,string) returns(bytes)": {
        "Governor.relay(address,uint256,bytes) returns()": [
            [
                "onlyGovernance",
                [
                    "EQ",
                    [
                        "_msgSender()",
                        "msgsender"
                    ],
                    [
                        "_executor()",
                        "address(this)"
                    ]
                ],
                "#High#ERROR_MSG:Governor: onlyGovernance"
            ]
        ]
    },
    "Arrays.findUpperBound(uint256[],uint256) returns(uint256)": {
        "Uint256ArraysMock.findUpperBound(uint256) returns(uint256)": []
    }
}